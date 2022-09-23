from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Link



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput
                               (attrs={'class': 'form-control',
                                       'style': 'width:50ch'}
                                ))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput
                               (attrs={'class': 'form-control',
                                       'style': 'width:50ch'}
                                ))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Максимум 150 символов',
                               widget=forms.TextInput
                               (attrs={'class': 'form-control',
                                       'style': 'width:50ch'}
                                ))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput
                                (attrs={'class': 'form-control',
                                        'style': 'width:50ch'}
                                 ))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput
                                (attrs={'class': 'form-control',
                                        'style': 'width:50ch'}
                                 ))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput
                             (attrs={'class': 'form-control',
                                     'style': 'width:50ch'}
                              ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('link',)