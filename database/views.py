from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from database.models import Recourse
from database.serializers import RecourseSerializer
from .models import Recourse


@csrf_exempt
def recourse_list(request):
    """
    List all code recourses, or create a new recourse.
    """
    if request.method == 'GET':
        recourse = Recourse.objects.all()
        serializer = RecourseSerializer(recourse, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recourse_detail(request, pk):
    """
    Retrieve, update or delete a code recourse.
    """
    try:
        recourse = Recourse.objects.get(pk=pk)
    except Recourse.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RecourseSerializer(recourse)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecourseSerializer(recourse, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recourse.delete()
        return HttpResponse(status=204)

# def database_list(request):
#     database = Recourse.objects.all().order_by('created_date')
#
#     return render(request, 'database/database_list.html', {'database_list': database})
