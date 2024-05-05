from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

#Главная страница
def home(request):
    return render(request, 'crnote/home.html')

#Регистрация пользователя
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'crnote/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttask')

            except IntegrityError:
                return render(request, 'crnote/signupuser.html', {'form':UserCreationForm(), 'error':'Данный пользователь уже существует'})
        else:
            return render(request, 'crnote/signupuser.html', {'form':UserCreationForm(), 'error':'Введенные пароли не совпадают'})

#Вход пользователя
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'crnote/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'crnote/loginuser.html', {'form':AuthenticationForm(), 'error':'Ошибка! Неправильный пароль!'})
        else:
            login(request, user)
            return redirect('currenttask')

#Выход пользователя
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

#Создание задач
def currenttask(request):
    return render(request, 'crnote/currenttask.html')