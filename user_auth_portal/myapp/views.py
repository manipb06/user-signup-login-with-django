from multiprocessing import context
from unicodedata import name
from django.contrib.auth import login as auth_login , logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import myform
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render( request, 'home.html')

def login(request):
    # print('working')
    if request.method == 'POST':
        # print('post request is coming')
        # import ipdb
        # ipdb.set_trace()
        name = request.POST['un']
        pswd = request.POST['pwd']
        user = authenticate(username = name , password = pswd)
        if user.is_active:
            auth_login (request, user)
            # print('login  working 123')
            return HttpResponseRedirect('/profile')
        else:
            wrngpass=("Sorry!! You are not authenticated!!! please check your User Name And Password")
            return render(request,'login.html',{'wrngpass':wrngpass})
    return render( request,'login.html')

def signup(request):
    form = myform()
    context = {'form': form}
    if request.method == 'POST':    
        form = myform(request.POST)
        if form.is_valid():
            pwd = form.data.get('password')
            confirm_pwd = form.data.get('confirm_pass')
            if pwd == confirm_pwd:
                current_obj = User()
                current_obj.first_name = form.data.get('first_name') #data fetched from user
                current_obj.last_name = form.data.get('last_name')
                current_obj.email = form.data.get('email')
                current_obj.username = form.data.get('username')
                current_obj.set_password(pwd)
                current_obj.save()
                return HttpResponseRedirect ('/login')
            else:
                context = {'msg':'your password is not matching'}
                return render(request, 'signup.html',context)
    else:
        form= myform()
        return render(request, 'signup.html',context)

def signout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def profile(request):
    print(dir(request.user))
    context = {
        'username': request.user,
        'first_name': request.user.first_name,
        'email': request.user.email,
        'last_login': request.user.last_login,
        'date_joined': request.user.date_joined,
    }
    return render(request, 'profile.html', context)    