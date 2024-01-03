from django.contrib import admin
from django.urls import path
from LandingAuth.views.landing.landing_page import *

urlpatterns = [
    path('', loadLandingPage,name="landing-page"),
]