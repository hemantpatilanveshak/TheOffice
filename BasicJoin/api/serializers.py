from rest_framework import serializers
from .models import Student , School


class OnlyStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    
    class Meta:
        model = Student
        fields = ['id','name','roll','city','school']
