from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetail


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        # Hash the password before saving
        user = User.objects.create_user(**validated_data)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserDetail
        fields = ['user', 'photo']
