from django.urls import path
from . import views


urlpatterns = [
    path('', views.achievments),
    path('leaderboard.html', views.leaderboard)
]