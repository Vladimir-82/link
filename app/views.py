import uuid

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Link
from .forms import AddForm, UserRegisterForm, UserLoginForm
from .utils import message


def create(request):
    '''
    Сreates a shortened link for registered users
    '''
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = AddForm()
            return render(request, 'app/create.html', {'form': form})
        else:
            return render(request, 'app/create.html', {'message': message()})
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            hash = uuid.uuid3(uuid.NAMESPACE_DNS, request.POST['link'])
            new_link = hash.__str__()[:8]
            domain = request.get_host()
            form.save()
            link = Link.objects.last()
            link.shortlink = ''.join(('https://', domain, '/', new_link))
            link.author_id = request.user.id
            link.save()
            return render(request, 'app/create.html', {'link': link})

def register(request):
    '''
    Registration of service users
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('create')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {"form": form})


def user_login(request):
    '''
    Service user logging
    '''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create')
    else:
        form = UserLoginForm()
    return render(request, 'app/login.html', {"form": form})


def user_logout(request):
    '''
    Unlogging service users
    '''
    logout(request)
    return redirect('login')



def show(request):
    '''
    Shows a list of full and shortened links for registered users
    '''
    current_user = request.user.id
    links = Link.objects.filter(author=current_user)
    if request.user.is_authenticated:
        return render(request, 'app/show.html', {"links": links})
    else:
        return render(request, 'app/show.html', {'message': message()})

