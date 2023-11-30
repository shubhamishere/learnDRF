from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse
from .models import Student
# Create your views here.
#Model object - single student data

#function base view
def student_detail(request, pk):
    #this wil fetch the first studnet object of id 1 from the DB
    #stu = Student.objects.get(id = 1)

    #this wil fetch the student object of given id
    #-in the url from the DB
    #i.e http://127.0.0.1:8000/stuinfo/2
    #i.e http://127.0.0.1:8000/stuinfo/1
    #i.e http://127.0.0.1:8000/stuinfo/3
    stu = Student.objects.get(id = pk)

    # print("stu thing is: ")
    # print(stu)
    #pass this stu object into StudentSerializer to get
    #-the serialized object of stu model object


    serializer = StudentSerializer(stu)
    # print("serializer thing is this: " )
    # print(serializer)

    #OneWay (shorter way) is to:
    #now we need to convert this serialised python datatype of stu object
    #-into frontend understandable JSON format
    #json_data = JSONRenderer().render(serializer.data)
    #returning json format data to the client
    #return HttpResponse(json_data, content_type='application/json')

    #AnotherWay is to: 
    return JsonResponse(serializer.data)







def student_list(request):
    #this wil fetch the first studnet object of id 1 from the DB
    #stu = Student.objects.get(id = 1)

    #to get all the objects as queryset
    stu = Student.objects.all()

    #pass this stu object into StudentSerializer to get
    #-the serialized dictionary object of stu model objects

    serializer = StudentSerializer(stu, many=True)
    # print("serializer thing is this: " )
    # print(serializer)
    #now we need to convert this serialised python datatype of stu object
    #-into frontend understandable JSON format
    #json_data = JSONRenderer().render(serializer.data)
    #returning json format data to the client
    #return HttpResponse(json_data, content_type='application/json')

    #AnotherWay : since data is of dict type, we need to set safe as False
    return JsonResponse(serializer.data, safe=False)