from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index,name="index"),
    path("login", views.loginUser,name="login"),
    path("logoutUser", views.logoutUser,name="logoutUser"),
    path("contact", views.contact,name="contact"),
]

# Django auth
#  check if user has enetered correct credential in google user is anonymous