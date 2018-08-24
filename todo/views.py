from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def todo_list(request):
    todo = Post.objects.all().order_by('published_date')

    return render(request, 'todo/todo_list.html', {'todo_list': todo})


def todo_detail(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})
