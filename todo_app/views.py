from django.shortcuts import render, redirect
from todo_app.models import Task
# Create your views here.


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('todo_list')


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todo_list')


def complete_task(request, id):
    task= Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('todo_list')