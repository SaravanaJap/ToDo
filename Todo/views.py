from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Task
# Create your views here.

def addTask(request):
    if request.method == 'POST':
        task_name = request.POST['task']
        Task.objects.create(task = task_name)
        print(task_name)
    return redirect('/')

def markComplete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('/')


def markInComplete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('/')

def edit_task(request,pk):
    task = get_object_or_404(Task,pk=pk)

    if request.method== 'POST':
        new_task_name = request.POST['task']
        task.task = new_task_name
        task.save()
        return redirect('/')
    else:
        context = {
            'task':task,
        }
        return render(request,'edit_task.html',context)
    

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('/')


