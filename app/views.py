from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Blog.objects.filter(name__contains = searched)
    return render(request,'app/search.html', {"searched":searched, "keys":keys})

def register(request):
    form = CreateUserForm()
    user_not_login = "show"
    user_login = "hidden"
    context = {'form':form,"user_not_login": user_not_login, "user_login": user_login}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'app/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user or password not correct')

    user_not_login = "show"
    user_login = "hidden"
    context = {"user_not_login": user_not_login, "user_login": user_login}
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def index(request):
    context = {}
    return render(request,'app/index.html')

def about(request):
    context = {}
    return render(request,'app/about.html',context)

def blog(request):
    context = {}
    return render(request,'app/blog.html')

def blog_details(request):
    context = {}
    return render(request,'app/blog_details.html')

def categori(request):
    context = {}
    return render(request,'app/categori.html')

