from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetail

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        user_detail, created = UserDetail.objects.update_or_create(user=user, photo=validated_data.pop('photo'))
        return user_detail
