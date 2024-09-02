from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserSignup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        existing_user = CustomUser.objects.filter(email=email).exists() #or CustomUser.objects.filter(username = username).exists()
        if existing_user:
            return Response("User exists")
        serializer=UserSignupSerializers(data = request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        return Response('Registration Failed' + str(serializer.errors))
    
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]

    
          
    

# class UserLogin(APIView):
#     def post(self, request):
#         data =UserLoginSerializers(request.data)
#         username = data.data['username']
#         password = data.data['password']
#         # user = User.objects.filter(username=username)

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             return Response({
#                 "username": user.username,
#                 "email": user.email,
#                 "status": 501
#             })
#         else:
#             return Response("Wrong Password")

#         #     return User.username, User.email
#         # else: 
#         #     return Response('User do not exist')
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticated]
        
class UserLogin(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, requset):
        user=requset.user
        data={
            "username: ": user.username,
            "email: ": user.email,
            "Status: ": "verified",

        }

        return Response(data)