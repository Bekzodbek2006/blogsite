import email
from pydoc import classname
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ImageField
from django.shortcuts import render

class MyUser(AbstractUser):
    pass

class Contact(models.Model):
    Name = models.CharField(max_length=75)
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    YourMassage = models.TextField(max_length=700)
    
    def __str__(self):
        return self.Name

class Chart(models.Model):
    country = models.CharField(max_length=50)
    visits = models.IntegerField(default=10)

    def __str__(self):
        return self.country
    
    
class Pro(models.Model):
    Name = models.CharField(max_length=20)
    howMuch = models.IntegerField(default=5)
    aboute = models.TextField(max_length=700)

    def __str__(self):
        return self.Name
    
class Team(models.Model):
    img = models.ImageField()
    Name = models.CharField(max_length=15)
    Aboute = models.TextField(max_length=700)
    
    def __str__(self):
        return self.Name