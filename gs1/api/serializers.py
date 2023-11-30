from rest_framework import serializers

#create subclass of Serializer class inorder 
#-to make serializer for student objects
#similar to creating a student model (in models.py)
#-also #similar to creating a student form (in django)

#serializer for student model
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
