from django.shortcuts import render, redirect, resolve_url
from .models import BreakfastGenre, BreakfastIngredient, DinnerGenre, DinnerIngredient, LunchGenre, LunchIngredient, User
import bcrypt

# Create your views here.

def index(request):
    return render(request, "registration.html")

def login(request):
    
    user= User.objects.filter(email=request.POST['email'])
    
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/dash')
        
        #  else:
        #      messages.error(request, "Invalid email or password.")
        #  messages.error(request, "Email does not exist.")
        # return redirect('/')
    return render(request, "login.html")



def dash(request):
    return render(request, "dashboard1.html")

def user(request):
    return render (request, "user.html")

def create(request):
    
    # errors = User.objects.basic_validator(request.POST)

    # user = User.objects.filter(email=request.POST['email'])
    # if user:
    #     messages.error(request, "Email already exists.")
    #     return redirect('/')

    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value, extra_tags=key)
    #     return redirect('/')

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user1 = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_pw
    )
    request.session['log_user_id'] = user1.id
    return redirect('/dash')

# def fills(request):
#     context = {
#         ''
def addbgenre(request):
    return render (request, 'addbgenre.html')

def createbgenre(request):
    TheIdG = BreakfastGenre.objects.get(id=request.session['log_user_id'])
    BreakfastGenre.objects.create(genre=request.POST['genre'], user=TheIdG)
    return redirect ('/breakfast')

def breakfast(request):
    context = {
        'breakfastgenre' : BreakfastGenre.objects.all(),
        'breakfasting' : BreakfastIngredient.objects.all(),
        'user': BreakfastGenre.objects.get(id=request.session['log_user_id'])
    }
    return render (request, 'breakfast.html', context)

def lunch (request):
    context = {
        'lunchgenre' : LunchGenre.objects.all(),
        'lunching' : LunchIngredient.objects.all()
    }
    return render (request, 'lunch.html', context)

def dinner (request):
    context = {
        'dinnergenre' : DinnerGenre.objects.all(),
        'dinnering' : DinnerIngredient.objects.all()
    }
    return render (request, "dinner.html", context)

def bdelete(request, bgenre):
    bgenre = BreakfastGenre.objects.get(bgenre)
    if (request.method == "GET"):
        bgenre.delete()
    bing = BreakfastIngredient.objects.get(bgenre)
    if (request.method == "GET"):
        bing.delete()
    return redirect ('/breakfast')