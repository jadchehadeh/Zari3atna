from django.urls import path
from .user_auth_view import UserRegistration,RetrieveUser,Registration

urlpatterns = [
    path('register-and-detail/', UserRegistration.as_view(), name='user_registration_and_detail'),
    path('retrieve-user/',RetrieveUser.as_view(),name='user_retrieve_data'),
    path('register-user/',Registration.as_view(),name = 'user_registration')
]
