from django.shortcuts import render
from django.http import HttpResponse
import requests

def view_user_registration(request):
    return render(request,"landing/authentication.html")


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name  = request.POST.get('lastName')
        password = request.POST.get('passWord')

        data = {
            'username' : username,
            'email' : email,
            'first_name' : first_name,
            'last_name' : last_name,
            'password' : password
 
        }
        print()
        response = requests.post('http://127.0.0.1:8001/api33399112222/register-and-detail/', json=data)
        if response.status_code == 404:
            return HttpResponse("Api Is Not Correct !")
        if response.status_code == 201:
            return HttpResponse("Registration Successful!")
        else:
            return HttpResponse("Error: Registration failed.")

    return render(request, 'authentication.html')



