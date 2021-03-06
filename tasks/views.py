from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from splash.forms import newTaskForm
from django.contrib.auth.models import User

def create(request):
    if request.method == 'POST':
        form = newTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(owner=request.user, title=data['title'], description=data['description'])
            task.save()
            if User.objects.filter(username=data['collaborator1']).exists():
                task.collaborators.add(User.objects.get(username=data['collaborator1']))
            if User.objects.filter(username=data['collaborator2']).exists():
                task.collaborators.add(User.objects.get(username=data['collaborator2']))
            if User.objects.filter(username=data['collaborator3']).exists():
                task.collaborators.add(User.objects.get(username=data['collaborator3']))                    
    return HttpResponseRedirect('/')
                
def delete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect('/')

def toggle(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            task.isComplete = True

        task.save()

    return HttpResponseRedirect('/')
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
def swag(request):
    return HttpResponse("Swag beans")
    
