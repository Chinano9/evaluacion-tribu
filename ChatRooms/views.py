from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def chat_list(request):
    return render(request, "chat_list.html")

def chat(request):
    return render(request, "chat.html")

