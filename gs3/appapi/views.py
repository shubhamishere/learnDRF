from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#need to exempt csrf token requirement for now 
@csrf_exempt
def student_api(request):
    #handling incoming client requests for GETting the data 
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

    #handling incoming client requests for POSTing/writing/creating new data on server side
    if request.method == 'POST':
        #catching the client side request data
        #client side JSON format data then--> python data type then--> complex data type then--> save in DB
        incoming_json_data = request.body
        stream = io.BytesIO(incoming_json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            #acknowledge the client if the data is created
            res ={'msg': 'data created'}
            outgoing_json_data = JSONRenderer().render(res)
            return HttpResponse(outgoing_json_data, content_type='application/json')
        
        #case when data was invalid, not serialised successfuly
        outgoing_json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(outgoing_json_data, content_type='application/json')
        
    #handling incoming client requests for PUTting/editing/modifying existing data on server side
    if request.method == 'PUT':
        incoming_json_data = request.body
        incoming_stream = io.BytesIO(incoming_json_data)
        #pythondata: dictionary->key value pairs
        pythondata = JSONParser().parse(incoming_stream)
        id = pythondata.get('id')
        #stu fetch the existing object data for the requested student id
        stu = Student.objects.get(id=id)
        #stu is passed to get serialized along with the updated data
        serializer = StudentSerializer(stu, data=pythondata, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated!!'}
            outgoing_json_data = JSONRenderer().render(res)
            return HttpResponse(outgoing_json_data, content_type='application/json')

        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
