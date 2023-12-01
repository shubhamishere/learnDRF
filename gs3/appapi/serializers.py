from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

#to create objects/models: client is using POST method to send data
#-we need to save it as objects then--> as models then--> in database

def create(self, validated_data):
    return Student.objects.create(**validated_data)

def update(self, instance, validated_data):
    print(instance.name)
    instance.name = validated_data.get('name', instance.name)
    print(instance.name)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance