from django.urls import path
from . import views
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')




urlpatterns = [
    path("login/", views.Userlogin.as_view(), name="login"),
    path("register/", views.Userregister.as_view(),name="register"),
    path('', home_view, name='home')
]