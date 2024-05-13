from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["firstname","lastname","username","email","password"]

    def create(self,validate_data):
        user = User.objects.create_user(**validate_data) 
        return user
       


class UserDetailedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserDetail
        fields = ['user','photo']


