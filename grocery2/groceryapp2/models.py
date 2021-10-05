from django.contrib.messages.api import error
from django.db import models
import re

from django.db.models.fields import BooleanField, related
from django.utils import tree

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters.'
        if len(postData['last_name']) < 2:
            errors['last_name'] =  'Last Name must be at least 2 characters.'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ('Invalid Email Address')
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if postData['password'] != postData['confirmpw']:
            errors['password'] = 'Passwords do not match'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()


class Genre(models.Model):
    named = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genre, related_name="ingredientgenre")
    menu = models.CharField(max_length=100, default="none")



