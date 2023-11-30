from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        #converting this incoming_json_data to stream
        stream = io.BytesIO(json_data)

        #convert this stream of data to python data
        pythondata = JSONParser().parse(stream)

        #converting this python data to complex data (models data)
        serializer = StudentSerializer(data = pythondata)

        #validate the parsed data and send it to the client confirming that the requested data is successfuly created
        if serializer.is_valid():
            serializer.save()
            response_to_client = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(response_to_client)
            return HttpResponse(json_data, content_type='application/json')
        
        #if not then it means error occured, handling error and giving the appropriate response
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')