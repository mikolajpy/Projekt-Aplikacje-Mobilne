from django.shortcuts import render
from django.http import JsonResponse #mozemy tez uzyc http response niby
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer

# Create your views here.
@api_view(['GET']) #To odpowiada za to co będziemy mogli zrobić z API, w naszym przypadku GET - otrzymanie strony i POST, dla tokenów czy co tam w końcu damy
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])    
def advocate_list(request):
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many = True)
    return Response(serializer.data)
 
@api_view(['GET', 'POST']) #to jest page dla osobnego user, post jest po to, zeby dalo sie wrzucic kod 
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many = False) #jest tu false, bo chcemy 1 obiekt a nie liste
    return Response(serializer.data)

