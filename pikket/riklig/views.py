from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import author, post

def placeholder(request):
    return render(request, 'index.html')

def home_page(request):
    posts = post.objects.all().order_by('-create_time')

    context = {'posts':posts}

    return render(request, 'home.html', context)

@login_required(login_url = 'login')
def my_posts(request):
    posts = post.objects.filter(author= request.user).order_by('-create_time')

    context = {'posts':posts}
    return render(request, 'home.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Неверное имя пользователя или пароль')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = Create_user_form()

    if request.method == 'POST':
        form = Create_user_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Пользователь ' + username + ' успешно зарегистрирован')

            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url = 'login')
def create_post(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        c = request.POST.get('content')

        new_post = post(title=t, content=c, author = request.user)
        new_post.save()
        return redirect('home')

    return render(request, 'newpost.html')

@login_required(login_url = 'login')
def update_post(request, pk):
    post_, = post.objects.filter(id= pk)
    context = {'post': post_}

    if request.method == 'POST':
        t = request.POST.get('title')
        c = request.POST.get('content')

        post_.title= t
        post_.content= c
        post_.save()
        return redirect('home')

    return render(request, 'update_post.html', context)

def get_post_data(request, pk):
    post_, = post.objects.filter(id= pk)
    data = {'content': post_.content,
                'title': post_.title}
    return JsonResponse(data)

@login_required(login_url = 'login')
def delete_post(request, pk):
    post_, = post.objects.filter(id= pk)
    if post_.author == request.user:
        post_.delete()
    return redirect('home')