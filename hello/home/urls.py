from sre_constants import SUCCESS
from unicodedata import name
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from home import views
from .views import select_slot, success
urlpatterns = [
    path('', views.index, name='home'),
    
    path("login", views.login_view, name="login"),
    path("select_slot", views.select_slot, name='select_slot'),
    # path('slot', select_slot, name='submit-slot'),
    path("payment", views.payment, name='payment'),
    path("contact", views.contact, name='contact'),
    path("logout", views.logout, name="logout"),
    path("sucess", views.success, name="success")
]
