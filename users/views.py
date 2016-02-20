from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from splash.forms import RegisterForm, loginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as poop_login
from django.contrib.auth import logout as poop_logout
# Create your views here.

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=email).exists():
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                poop_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Error")

        else:
            registrationForm = RegisterForm()
            loginform = loginForm()
            return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid password'})

    else:
        registrationForm = RegisterForm()
        loginform = loginForm()
        return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid email address'})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(data['fl_name']) > 50:
                registrationForm = RegisterForm()
                loginform = loginform()
                return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Name too long'})

            if len(data['password']) > 50:
                registrationForm = RegisterForm()
                loginform = loginform()
                return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Password too long'})

            if data['password'] == data['password_confirmation']:
                if User.objects.filter(username=data['email']).exists():
                    registrationForm = RegisterForm()
                    loginform = loginForm()
                    return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Account with this email already exists!'})
                else:
                    user = User.objects.create_user(data['email'], '', data['password'], first_name=data['fl_name'])
                    user = authenticate(username=data['email'], password=data['password'])
                    poop_login(request, user)
                    return HttpResponseRedirect('/')
            else:
                registrationForm = RegisterForm()
                loginform = loginForm()
                return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Passwords do not match'})

        else:
            registrationForm = RegisterForm()
            loginform  = loginForm()
            return render(request, 'index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Name too short'})

    return HttpResponseRedirect('/')
    
def logout(request):
    poop_logout(request)
    return HttpResponseRedirect('/')