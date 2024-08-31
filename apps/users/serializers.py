from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError, UniqueValidator
from django.contrib.auth.hashers import make_password

class UserSignupSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}
    

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user     
    

        # validated_data['password'] = make_password(validated_data.get('password'))
        # return super(UserSignupSerializers, self).create(validated_data)
    
class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username','password']

    # def get(self, validate_data):
    #     user=User.objects.get(**validate_data)
    #     return user
    


