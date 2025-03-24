from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.

def addTask(request):
    if request.method == 'POST':
        task_name = request.POST['task']
        Task.objects.create(task = task_name)
        print(task_name)
    return redirect('/')

