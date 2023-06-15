from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Room, Message 

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):
        username = 'testuser'
        password = 'testpassword'
        User.objects.create_user(username=username, password=password)

        data = {
            'username': username,
            'password': password
        }
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, '/chat/')

    def test_login_view_post_failure(self):
        data = {
            'username': 'nonexistentuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        
        error_message = response.context['error_message']
        self.assertEqual(error_message, "username or password are incorrect")
        self.assertTemplateUsed(response, 'login.html')

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.register_url, data)
        self.assertRedirects(response, self.login_url)

        
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

    def test_register_view_post_failure(self):
        data = {
            'username': 'caca', 
            'password': ''
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        
        user_exists = User.objects.filter(username='testuser').exists()
        self.assertFalse(user_exists)
 
class RoomListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin = User.objects.create_superuser(username='admin', password='adminpassword')
        self.room = Room.objects.create(name='Habitación de prueba', disponibility=True, owner=self.user)

    def test_room_list_view_with_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('room_list'), {'room_id': self.room.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Room.objects.filter(id=self.room.id).exists())

    def test_room_list_view_without_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('room_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.room.name)

    def test_room_list_view_with_admin_delete(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('room_list'), {'room_id': self.room.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Room.objects.filter(id=self.room.id).exists())

class CreateRoomViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_room(self):
        
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('create_room'), {
            'name': 'Test Room',
            'disponibility': True,
        })

        self.assertEqual(response.status_code, 302)  # Se espera una redirección
        self.assertRedirects(response, reverse('room_list'))

        # Verificar que la sala se haya creado en la base de datos
        room = Room.objects.last()
        self.assertEqual(room.name, 'Test Room')
        self.assertEqual(room.disponibility, True)
        self.assertEqual(room.owner, self.user)
