from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError, UniqueValidator

class UserSignupSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username', 'email', 'password']

    def create():
        return User.objects.create()
            
