from django.db import models
from django.db.models import Exists, OuterRef


# no_date=Exists(ToDoItem.objects.filter(todo_list=OuterRef('pk'),end_date__isnull=True)),

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Title')

    def __str__(self):
        return self.title

    def get_items(self):
        items = ToDoItem.objects.filter(todo_list=self.pk)
        orders_items = items.annotate(
                                      with_date=Exists(ToDoItem.objects.exclude(todo_list=OuterRef('pk'),
                                                                                end_date__isnull=True))
                                      ).order_by('with_date', 'pk')
        print(self.title)
        print(self.items.exclude(end_date__isnull=True))
        print(self.items.filter(end_date=None))

        return orders_items


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ["end_date"]
