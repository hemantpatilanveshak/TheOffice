from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.


### Function based View


def student_details(request,id=None):

    if id is not None:

        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')
    
    else:
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data, content_type='application/json')



