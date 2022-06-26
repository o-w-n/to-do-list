from django import forms
from .models import ToDoList, ToDoItem


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        exclude = ()

class DateInput(forms.DateInput):
    input_type = 'date'

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        exclude = ['todo_list', 'status']
        widgets = {
            'end_date': DateInput(),
        }

    def save(self, **kwargs):
        todo = kwargs.pop('todo')
        todo_obj = ToDoList.objects.get(pk=todo)

        instance = super(ToDoItemForm, self).save(**kwargs)
        instance.todo_list = todo_obj
        instance.save()
        return instance

