from django.urls import path
from todo import views

urlpatterns = [
    path(r'', views.todo_list, name='todo_list'),
    path(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    path(r'^post/new/$', views.todo_new, name='todo_new'),
    path(r'^post/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
]
