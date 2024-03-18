from django.shortcuts import render
from django.http import JsonResponse #mozemy tez uzyc http response niby
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET']) #To odpowiada za to co będziemy mogli zrobić z API, w naszym przypadku GET - otrzymanie strony i POST, dla tokenów czy co tam w końcu damy
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])    
def advocate_list(request):
    data = ['Mikolaj', 'Jedrek', 'Tomek']
    return Response(data) 
 
@api_view(['GET', 'POST'])
def advocate_detail(request, username):
    data = username
    return Response(data)

