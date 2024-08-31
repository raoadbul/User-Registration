from django.shortcuts import render
from rest_framework import viewsets
from .models import Dish, Recipie
from .serializers import DishSerializers, RecipieSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class DishViewSet(viewsets.ModelViewSet):
    queryset=Dish.objects.all()
    serializer_class = DishSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes= [IsAdminUser]



class RecipieViewSet(viewsets.ModelViewSet):
    queryset = Recipie.objects.all()
    serializer_class = RecipieSerializers
    # authentication_classes= [BasicAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
