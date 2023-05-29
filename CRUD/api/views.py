from django.shortcuts import render
from .models import Student , School
from rest_framework import status
from .serializers import StudentListSerializer , SchoolListSerializer , OnlySrudentSerialzer
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def get_student_data(request, id = None):
    
    if request.method == 'GET':
        obj = Student.objects.all()
        serializer = StudentListSerializer(obj,many = True)
        data = serializer.data
        print(data)
        return Response({"msg":"Data Fetched","data":data})
    
    
    if request.method == 'POST':
        obj = request.data
        serializer = OnlySrudentSerialzer(data= obj)


        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

        else:
            return Response({"msg":"Fields Not filled properly"})
        

        return Response({"msg":'Method is working',"data":serializer.data})
    

@csrf_exempt
@api_view(['PATCH','PUT','DELETE'])
def studentapi(request, id = None):

    if request.method == 'PATCH':
        obj = Student.objects.get(id = id)
        data = request.data
        

        serializer = OnlySrudentSerialzer(obj ,data= data,partial= True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"msg":"Following Data is not valid","data":serializer.data})

        return Response({"msg":"Patch","data":serializer.data})
    

    if request.method == 'PUT':
        obj = Student.objects.get(id = id)
        data = request.data

        serializer = OnlySrudentSerialzer(obj , data= data)

        if serializer.is_valid():
            serializer.save()
        
        return Response({"msg":"Put Method Working","Data":serializer.data})
    

    if request.method == 'DELETE':
        obj = Student.objects.get(id = id)
        obj.delete()

        return Response({"msg":"Data Deleted"})
    

@api_view(['GET','POST'])
def school_api(request,id =None):
    if request.method == 'GET':
        if id is not None:
            try:
                obj = School.objects.get(id = id)
            except:
                return Response({"msg":"Game Id Does not exists"})
            serializer = SchoolListSerializer(obj)
            data = serializer.data
            return Response({"msg":"Data Fetched By ID","data":data})
    
    
        else:
            obj = School.objects.all()
            serializer = SchoolListSerializer(obj,many = True)
            data = serializer.data
            return Response({"msg":"Data Fetched","Data":data})
            
    # return Response({"msg":"Error","status":status.HTTP_400_BAD_REQUEST})


    if request.method == 'POST':
        obj = request.data
        serializer = SchoolListSerializer(data=obj)

        if serializer.is_valid():
            serializer.save()

        return Response({"msg":"Data posted","data":serializer.data})



