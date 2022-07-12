from django.urls import path
from .views import index

urlpatterns = [
    # path('view/', LinksView.as_view()),
    path('resize/', index)
]