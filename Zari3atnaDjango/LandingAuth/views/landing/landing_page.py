from django.shortcuts import render
def loadLandingPage(request):
    return render(request,'landing/landing.html')