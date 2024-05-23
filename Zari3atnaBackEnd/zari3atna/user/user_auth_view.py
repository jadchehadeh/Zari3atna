from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetail
from .serializers import UserDetailSerializer

class UserRegistration(generics.CreateAPIView):
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        user_detail_serializer = self.get_serializer(data=request.data)

        if user_detail_serializer.is_valid():
            user_detail_serializer.save()
            return Response(user_detail_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUser(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer