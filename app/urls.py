from django.urls import path
from .views import create, register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('create/', create, name='create'),
]