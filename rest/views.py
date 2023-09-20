from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



def my_view(request):
    abj = Students.objects.get(id = 1)
    print(abj)
    serializer = StudentSerializer(abj)
    print(serializer)
    print(serializer.data)
    abc =JSONRenderer().render(serializer.data)
    print(abc)
    return HttpResponse(abc,content_type = 'application/json')
    

def detail_view(request):
    obj = Students.objects.all()
    serializer = StudentSerializer(obj, many = True)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')





# Create your views here.
@csrf_exempt
def insert_data(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'message':'data is created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        
        json_data = JSONParser().parse(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
