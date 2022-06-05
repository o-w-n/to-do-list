from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import ToDoList
from .forms import ToDoListForm, ToDoItemForm


def list_view(request):
    all_todo_list = ToDoList.objects.all()
    create_list_form = ToDoListForm()
    create_item_form = ToDoItemForm()

    return render(request, 'home.html', {'all_todo_list': all_todo_list,
                                         'create_list_form': create_list_form,
                                         'create_item_form': create_item_form,
                                         })


def create_list(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)

    return redirect("todo_app:home")


def create_item(request, pk):
    if request.method == "POST":
        instance = get_object_or_404(ToDoList, id=pk)
        form = ToDoItemForm(request.POST, instance=instance)
        if form.is_valid():
            new_form = form.save(commit=False)
    return redirect("todo_app:home")
