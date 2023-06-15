from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
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
        User.objects.create_user(username=username, password=password)
        return redirect('login')  # Reemplaza 'login' con el nombre de tu URL de inicio de sesión
    else:
        return render(request, 'register.html')

def chat_list(request):
    return render(request, "chat_list.html")

def chat(request):
    return render(request, "chat.html")
