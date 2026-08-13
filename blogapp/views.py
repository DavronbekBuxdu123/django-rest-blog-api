from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,BlogSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def user_register(request):
    serializer=UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def create_blog(request):
    user=request.user
    serializer=BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    else:
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      