from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request,'index.html', context)

def submit(request):
    if request.method == "POST":
        User.objects.create(
            first_name = request.POST["first_name"].title(),
            last_name = request.POST["last_name"].title(),
            email_address = request.POST["email"],
            age = request.POST["age"]
        )        
        return redirect('/')
    else:
        return redirect('/')