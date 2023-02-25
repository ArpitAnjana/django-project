import email
from pickle import TRUE
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.



class Contact(models.Model):
    # S_No = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone =  models.CharField(max_length=12)
    comment = models.TextField(max_length=300)
    # date = models.DateField()

    def __str__(self):
        return self.name




class Slot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    slot_name = models.CharField(max_length=100)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.slot_name


class Checkbox(models.Model):
    checkbox_text = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.checkbox_text




class Pay(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)