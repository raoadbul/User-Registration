from rest_framework import serializers
from .models import Dish,Recipie

class DishSerializers(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields='__all__'

class RecipieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Recipie
        fields='__all__'