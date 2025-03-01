from django.shortcuts import render
from .models import tasks
from .forms import TaskForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def index(request):
    return render(request, 'tasks/tasks_list.html') #rendering the tasks_list.html file



def tasks_list(request):
    task_list = tasks.objects.all()  # Retrieve all tasks from the database
    return render(request, 'tasks/task_haru.html', {'tasks': task_list})  # Pass tasks to the template


# creating the tasks

def task_create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form':form})