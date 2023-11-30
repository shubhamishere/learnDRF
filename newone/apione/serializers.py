from rest_framework import serializers
from .models import Student

#the class Meta is a way to provide metadata or additional configuration options for a class. 
#-In the context of a ModelSerializer in DRF, the class Meta is used to specify some additional information
#-about how the serializer should behave when dealing with a particular model.


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

def create(self, validate_data):
    return Student.objects.create(**validate_data)