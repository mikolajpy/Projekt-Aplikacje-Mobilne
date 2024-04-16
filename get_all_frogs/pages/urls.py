from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visited', views.visited_zabkas, name='visited'),
]