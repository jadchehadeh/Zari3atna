from django.contrib import admin
from django.urls import path
from LandingAuth.views.landing.landing_page import *
from LandingAuth.views.auth.new_user_auth import * 

urlpatterns = [
     path('', loadLandingPage,name="landing-page"),
     path('new-user-auth-reg/',view_user_registration,name="user-auth-registration"),
     path('form_submit/',register_user,name="user_registrations")

    ]