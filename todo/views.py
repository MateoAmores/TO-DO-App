from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# CRUD - Create, Retrieve, Update, Delete, List

# List
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list" : todos
    }
    return render(request, "todo/todo_list.html", context)

# Retrieve
def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo" : todo
    }
    return render(request, "todo/todo_detail.html", context)

# Create
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        #print(form.clean_data)
        #name = form.cleaned_data['name']
        #due_date = form.cleaned_data['due_date']
        #print(name, due_date)

        # create a todo object
        #new_todo = Todo.objects.create(name=name, due_date=due_date)

        form.save()
        return redirect('/')
        pass
    context = {
        "form" : form
    }
    return render(request, "todo/todo_create.html", context)


# Update
def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
        pass
    context = {
        "form" : form
    }
    return render(request, "todo/todo_update.html", context)


# Delete
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
