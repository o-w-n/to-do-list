from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.list_view, name="home"),
    path('create/', create_list, name="create"),
    path('add/<int:pk>', create_item, name="add"),
]
