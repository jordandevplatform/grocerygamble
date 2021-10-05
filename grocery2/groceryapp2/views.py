import re
from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User 
from .models import *
import bcrypt

def index(request):
    return render(request, "registration.html")


def create(request):
    errors = User.objects.basic_validator(request.POST)

    user = User.objects.filter(email=request.POST['email'])
    if user:
        messages.error(request, "Email already exists.")
        return redirect('/')

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user1 = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_pw
    )
    print(user1)
    request.session[''] = user1.id
    return redirect('/dash')


def login(request):

    user = User.objects.filter(email=request.POST['email'])
    
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/dash')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/')
    else:
        messages.error(request, "Email does not exist.")
        return redirect('/')

def addgenre(request):
    return render (request, 'addgenre.html')

def creategenre(request):
    the_user= User.objects.get(id=request.session['log_user_id'])
    Genre.objects.create(named=request.POST['genre'] )
    return redirect ('/bld')

def createing(request):
    # print(request.POST['menu'])
    Ingredient.objects.create(ingredient=request.POST['ing'], menu=request.POST['menu'])
    return redirect ('/dash')
# def breakfast(request):
#     context = {
#         'breakfastgenre' : BreakfastGenre.objects.all(),
#         'breakfasting' : BreakfastIngredient.objects.all(),
#     }
#     return render (request, 'breakfast.html', context)

def TodChoice(request):
    if request.POST['menu'] == 'Breakfast':
        request.session['menu'] = 'Breakfast'
    elif request.POST['menu'] == 'Lunch':
        pass
    else:
        pass
    return redirect ("/bld")

def user(request):
    return render(request, 'user.html')

def logout(request):
    request.session.clear()
    return redirect ("/")

def bld(request):
    if request.session['menu'] == 'Breakfast':
        ingredients=Ingredient.objects.filter(menu='Breakfast')
    elif request.session['menu'] == 'Lunch':
        ingredients=Ingredient.objects.filter(menu="Lunch")
    elif request.session['menu'] == 'Dinner':
        ingredients=Ingredient.objects.filter(menu='Dinner')
    # print(ingredients)
    context = {
        'ingredients' : ingredients,
        'genre' : Genre.objects.all()
    }
    return render(request, 'BLD.html', context)

def dash(request):
    return render(request, 'dashboard1.html')

def delete(request, theid):
    ingredient = Ingredient.objects.get(id = theid)
    if (request.method == "GET"):
        ingredient.delete()
    return redirect('/bld')