from django.urls import path
from .views import index, linker

urlpatterns = [
    # path('', AddCreateView.as_view(), name='add'),
    path('main', index, name='main'),
    path('', linker, name='linker'),
]