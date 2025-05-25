from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
# from django.contrib.auth.models import User
from .models import User
from django.contrib import messages


def home(request):
    context = {
     
    }
    return render(request, 'home.html' , context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        # username = request.POST.get('email').lower()  ## Login By Email
        password = request.POST.get('password')

        # user = User.objects.get(username=username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Data')



    context = {
     'page':'login'
    }

    return render(request, 'login_register.html', context)

def register(request):
    form = UserCreationForm()
    # form = RegisterForm() ## Register by email
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = RegisterForm(request.POST, request.FILES) # Register By Email
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User Regsitered Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed To Register')
    context = {
     'form':form
    }
    return render(request, 'login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect("home")

@login_required(login_url='login')
def dashboard(request):
    # return render(request, 'login_register.html')
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)

# def profile(request):
#     profile = StudentProfile.objects.get(id=1)
#     context = {
#         'profile':profile
#     }
#     return render(request, 'profile.html', context)