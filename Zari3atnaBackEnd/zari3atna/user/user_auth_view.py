from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetail
from .serializers import UserDetailSerializer, UserSerializer

class UserRegistration(generics.CreateAPIView):
    serializer_class = UserDetailSerializer  # Set a default serializer_class to satisfy DRF

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data.get('user'))
        user_detail_serializer = UserDetailSerializer(data=request.data)

        if user_serializer.is_valid() and user_detail_serializer.is_valid():
            user = user_serializer.save()
            user_detail_serializer.save(user=user)
            return Response({"user": user_serializer.data, "user_detail": user_detail_serializer.data}, status=status.HTTP_201_CREATED)

        errors = {}
        if not user_serializer.is_valid():
            errors.update(user_serializer.errors)
        if not user_detail_serializer.is_valid():
            errors.update(user_detail_serializer.errors)

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class GetUser(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer

    