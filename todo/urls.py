from django.urls import path, re_path
from todo import views

urlpatterns = [
    re_path(r'', views.todo_list, name='todo_list'),
    re_path(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    re_path(r'^post/new/$', views.todo_new, name='todo_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
]
