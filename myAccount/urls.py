from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('LogIn/', views.LogIn, name="LogIn"),
    path('signUp/', views.SignUp, name="signUp"),
    path('LogOut/',views.LogOut, name="LogOut"),

]