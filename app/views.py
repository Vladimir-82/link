import uuid

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Link
from .forms import AddForm, UserRegisterForm, UserLoginForm


# @login_required
def create(request):
    if request.method == 'GET':
        form = AddForm()
        return render(request, 'app/create.html', {'form': form})
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        links = Link.objects.last()
        hash = uuid.uuid3(uuid.NAMESPACE_DNS, links.link)
        new_link = hash.__str__()[:8]
        links.shortlink = ''.join(('https://', 'mydomen/', new_link))
        links.save()

        return render(request, 'app/create.html', {'links': links})


def register(request):
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
    logout(request)
    return redirect('login')


@login_required
def show(request):
    current_user = request.user.id
    links = Link.objects.filter(author=current_user)
    return render(request, 'app/show.html', {"links": links})
