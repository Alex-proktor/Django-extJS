from django.urls import path, re_path
from database import views

urlpatterns = [
    re_path(r'', views.database_list, name='database_list'),
]