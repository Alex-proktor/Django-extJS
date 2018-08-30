from django.shortcuts import render
from .models import Recourse


def database_list(request):
    database = Recourse.objects.all().order_by('created_date')

    return render(request, 'database/database_list.html', {'database_list': database})
