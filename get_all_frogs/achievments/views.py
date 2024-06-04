from django.http import HttpResponse
from django.shortcuts import render
from get_all_frogs.models import AssignedAcievments
from django.contrib.auth.models import User
from django.db.models import Count

def achievments(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        achievments_list = AssignedAcievments.objects.filter(achievement_owner=user)
        return render(request, 'list.html', {'achievments_list': achievments_list})
    return render(request, 'pages/home.html')


def leaderboard(request):
    if request.user.is_authenticated:
        leaderboard = User.objects.annotate(num_achievments=Count('assignedacievments')).order_by("-num_achievments")
        return render(request, 'leaderboard.html', {'leaderboard': leaderboard})
    return render(request, 'pages/home.html')