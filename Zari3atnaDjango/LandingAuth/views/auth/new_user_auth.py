from django.shortcuts import render
from django.http import HttpResponse
import requests

def view_user_registration(request):
    return render(request,"landing/authentication.html")


from django.shortcuts import render
from django.http import HttpResponse
import requests

from django.shortcuts import render
from django.http import HttpResponse
import requests

def register_user(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST.get('userName')
        email = request.POST.get('email')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('passWord')
        profile_picture = request.FILES.get('profilePicture')

        # Prepare data for POST request
        data = {
            'user': {
                'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'password': password
            },
            'photo': profile_picture
        }

        # Make POST request to DRF API
        response = requests.post(
            'http://127.0.0.1:8001/api33399112222/register-and-detail/',
            data=data
        )

        # Handle response
        if response.status_code == 201:
            return HttpResponse("Registration Successful!")
        else:
            return HttpResponse(f"Error: {response.content.decode()}")

    return render(request, 'landing/authentication.html')





