from django.urls import path
from .user_auth_view import UserRegistration

urlpatterns = [
    path('register-and-detail/', UserRegistration.as_view(), name='user_registration_and_detail'),
]
