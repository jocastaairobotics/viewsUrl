from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('previousYear/', views.previousYear, name="previousYear"),
    path('Gate/', views.Gates, name="Gate"),
    path('EngineeringServices/', views.EngineeringServices, name="EngineeringServices"),
]