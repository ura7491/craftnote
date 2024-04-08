from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'crnote/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
            except IntegrityError:
                return render(request, 'crnote/signupuser.html', {'form':UserCreationForm(), 'error':'Данный пользователь уже существует'})
        else:
            return render(request, 'crnote/signupuser.html', {'form':UserCreationForm(), 'error':'Введенные пароли не совпадают'})