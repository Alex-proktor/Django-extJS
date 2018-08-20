from django.shortcuts import render
from django.utils import timezone
from .models import Post

def todo_list(request):
    todo = Post.objects.all().order_by('published_date')

    return render(request, 'todo/todo_list.html', {'todo_list': todo})
