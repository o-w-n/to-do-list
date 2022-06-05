from django import forms
from .models import ToDoList, ToDoItem


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ()



class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        exclude = ['todo_list']
