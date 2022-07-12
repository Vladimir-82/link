from django.urls import path
from .views import index, AddCreateView

urlpatterns = [
    path('', AddCreateView.as_view(), name='add'),
    path('main', index, name='main'),
]