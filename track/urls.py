from django.urls import path

from .import views

urlpatterns=[
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('land', views.land, name='land'),
    path('registration', views.registerPage, name='registration'),
    path('', views.loginPage, name='login'),
]
