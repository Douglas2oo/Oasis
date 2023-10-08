from django.urls import path

from . import views
from Oasisback import views

urlpatterns = [
    path("Osisback/", views.UserList.as_view()),
    path("Oasisback/login/", views.UserDetail.as_view()),
    path("Oasisback/register/", views.Userregister.as_view()),
]