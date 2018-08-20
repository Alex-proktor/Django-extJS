from django.urls import path
from todo import views

urlpatterns = [
    path(r'', views.todo_list, name='post_list'),
]
