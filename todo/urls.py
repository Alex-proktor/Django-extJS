from django.urls import path
from todo import views

urlpatterns = [
    path(r'', views.todo_list, name='post_list'),
    path(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
]
