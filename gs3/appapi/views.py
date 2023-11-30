from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import requests

# Create your views here.
def student_api(request):
    if request.method == 'GET':
        #catch the client side request data
        incoming_json_data = request.body
        stream = io.BytesIO(incoming_json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        #case 1 when some id is passed by the client
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            #only after serializing the data it can be rendered by the jsonrenderer
            #-to give the JSONresponse back to the client
            outgoing_json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(outgoing_json_data, content_type='application/json')
        
        #case 2 when nothing is passed by the client
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        outgoing_json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(outgoing_json_data, content_type='application/json')