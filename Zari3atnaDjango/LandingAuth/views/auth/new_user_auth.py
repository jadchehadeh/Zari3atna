from django.shortcuts import render

def new_user_auth(request):
    return render(request,"landing/authentication.html")


