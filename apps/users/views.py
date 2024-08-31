from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *

class UserSignup(APIView):
    usersignup=User.objects.all()
    serializer=UserSignupSerializers(usersignup, many=True)
    
    