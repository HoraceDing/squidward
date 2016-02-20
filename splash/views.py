from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import loginForm
from .forms import RegisterForm

# Create your views here.
def index(request):
    # if request.user.is_authenticated():
    #     logger.error('Something went right!')
    #     return render(request, 'splash/index.html', {'user': request.user, 'new_task': newTaskForm, 'tasks': tasks})
    # else:
        registerForm = RegisterForm()
        loginform = loginForm()
        return render(request, 'index.html', {'login': loginform, 'register': RegisterForm})
    
    


