from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfuly created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request, "screens/registration.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(request, username = username, password = Password)

        if user is not None:
            login(request, user)

            return redirect('')

    context = {}
    return render(request,"screens/login.html")

def home(request):
    return render(request, "screens/home.html")

def register(request):
    return render(request, "screens/register.html")

def land(request):
    return render(request, "screens/landing.html")