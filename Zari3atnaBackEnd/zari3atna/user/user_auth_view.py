from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetail
from .serializers import UserDetailSerializer,UserSerializer

class UserRegistration(generics.CreateAPIView):
    def post(self,request):
        user_serliazer = UserSerializer(data=request.data)
        user_detailed_serlializer = UserDetailSerializer(data = request.data)

        if(user_serliazer.is_valid() and user_detailed_serlializer.is_valid()):
            user = user_serliazer.save()
            user_detail = user_detailed_serlializer.save(user=user)
            return response({"user":user_serliazer.data, "user_detail":user_detailed_serlializer.data},status = status.HTTP_201_CREATED)


             

