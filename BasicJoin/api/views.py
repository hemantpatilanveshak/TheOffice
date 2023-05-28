from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Student , School
from .serializers import StudentSerializer, SchoolSerializer

# Create your views here.


class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.select_related('school')
        # queryset = School.objects.select_related('student')
        return queryset
    
    # def list(self, request , *args , **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset,many= True)

    #     return Response(serializer.data)