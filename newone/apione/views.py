from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

#bypassing csrf requirement using csrf_exempt
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
            response_json_data = JSONRenderer().render(response_to_client)
            return HttpResponse(response_json_data, content_type='application/json')
        
        #if not then it means error occured, handling error and giving the appropriate response
        response_json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(response_json_data, content_type='application/json')