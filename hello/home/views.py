from ast import Pass
from datetime import date, datetime
import email
from http import client

from multiprocessing import context
from os import uname
from re import S
import re
from tokenize import Name
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from home.models import Checkbox
from datetime import datetime 
from .models import Pay
import razorpay


# Create your views here.
# this index is signup page
def index(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('Please check your password again!')
        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')

    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(user)
            login(request, user)
            return redirect('select_slot')

        else:
            context = {"error": "invalid username or password!"}
            return render(request, "login.html", context)
            # return HttpResponse('Your username and password is incorrect!')
            

    return render(request, "login.html")



# this one is logout
def logout(request):
    return render(request, "index.html")

# this is for home page after login u be redirected here
# home page

def success(request):
    return render(request, "success.html")

def payment(request):

    return render(request, "payment.html")
    

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        print(name, email, phone, comment)
        ins = Contact(name=name, email=email, phone=phone, comment=comment)
        ins.save()
        print("the data has been written to db")

    # return HttpResponse('this is contact')
    return render(request, "contact.html")




def select_slot(request):
    return render(request, "select_slot.html")

# @login_required

# def select_checkbox(request):
#     checkbox_id = request.POST.get('checkbox')
#     checkbox = Checkbox.objects.get(id=checkbox_id)
#     if checkbox.is_selected:
#         # if checkbox is already selected, return an error message
#         error_message = "Checkbox already selected. Please choose another."
#         return render(request, 'app_name/select_checkbox.html', {'error_message': error_message})
#     else:
#         # if checkbox is not selected, select it and save to the database
#         checkbox.is_selected = True
#         checkbox.save()
#         return redirect('payment')
        
   


#     return render(request, "select_slot.html")
    

# def viewName(request):
#    if request.method == 'POST':
#       # You have access to data inside request.POST
#       activism = request.POST.get('activism')
#       if activism:
#            pass # Activism is checked