from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserDetail
        fields = ['user', 'photo']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user_detail = UserDetail.objects.create(user=user, **validated_data)
        return user_detail
