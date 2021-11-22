from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, "screens/registration.html", context)

def home(request):
    return render(request, "screens/home.html")

def register(request):
    return render(request, "screens/register.html")

def land(request):
    return render(request, "screens/landing.html")