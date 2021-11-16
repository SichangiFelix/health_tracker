from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "screens/home.html")

def register(request):
    return render(request, "screens/register.html")

def land(request):
    return render(request, "screens/landing.html")