from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import TodoForm


def todo_list(request):
    todo = Post.objects.all().order_by('published_date')

    return render(request, 'todo/todo_list.html', {'todo_list': todo})


def todo_detail(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


@login_required
def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.published_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_edit.html', {'form': form})


@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.published_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})
