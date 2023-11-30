from rest_framework import serializers

#this is not model serializer, just the plain serializer
#EmployeeSerializer it is a child class of serializers.Serializer
class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=64)