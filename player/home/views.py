from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from home.models import Contact


# password = arsh**##00
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, "index.html")
    
def loginUser(request):
    if request.method == "POST":
        #  check if user has enetered correct credential
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request, "login.html")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email = email, number=number, desc=desc,date =  datetime.today())
        contact.save()
        
    return render(request, "contact.html")
