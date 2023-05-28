from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Student , School
from .serializers import StudentSerializer, SchoolSerializer, OnlyStudentSerializer
from rest_framework import status

# Create your views here.


class StudentDetailsListView(APIView):
    def get(self , request):
        students = Student.objects.all()
        serializer = OnlyStudentSerializer(students,many = True) 
        return Response({"msg":"Retrived Data","data":serializer.data})
    

    def post(self , request):
        serializer = OnlyStudentSerializer(data = request.data)
        # obj = School.objects.all()
        # obj_ser = SchoolSerializer(obj,many=True)

        if serializer.is_valid():
            print(serializer.data)
            return Response({"msg":"Method Wroking","ser":serializer.data})
    
        return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)



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