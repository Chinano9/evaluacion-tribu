from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from .models import Room, Message
# Create your views here.
def index(request):
    return render(request,"index.html")

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('index')
        else:
            error_message = "username or password are incorrect"

            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if len(username) < 8 or len(password) < 8:
            error_message = "username or password are too short"
            return render(request, 'register.html', {'error_message': error_message})

        User.objects.create_user(username=username, password=password)

        return redirect('login')  
    else:
        return render(request, 'register.html')

@login_required
def room_list(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        room = Room.objects.get(id=room_id)

        if room.owner == request.user or request.user.is_superuser:
            room.delete()
            return redirect('room_list')

    query = request.GET.get('query')
    rooms = Room.objects.all()

    if query:
        rooms = rooms.filter(name__icontains=query)

    paginator = Paginator(rooms, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }

    return render(request, 'room_list.html', context)

@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        disponibility = request.POST.get('disponibility')

        room = Room(name = name, disponibility = disponibility, owner = request.user)
        room.save()

    return redirect(room_list)

@login_required
def room(request):
    return render(request, "chat.html")
