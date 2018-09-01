from django.urls import re_path
from database import views


urlpatterns = [
    re_path(r'^recourse/$', views.recourse_list),
    re_path(r'^recourse/(?P<pk>[0-9]+)/$', views.recourse_detail),
]
