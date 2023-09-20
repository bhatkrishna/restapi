from rest_framework import serializers
from . models import Students

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll_no = serializers.IntegerField()
    address = serializers.CharField(max_length = 100)

    def create(self,validated_data):
        return Students.objects.create(**validated_data)