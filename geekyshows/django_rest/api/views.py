from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from .permission import MyPermission#custome permission
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import JackRateThrottle#customize throttling for different model
#Routable url modelviewSet | way =07 . You can use ReadOnlyModelViewSet just to show list and retrieve
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes =[] #i am not using these two line because i have added these two line in settings.py globally. these two line would be automatically implemented to every class
    permission_classes = []
    throttle_classes =[JackRateThrottle]
#Routable url |way =06
class StudentViewSet(viewsets.ViewSet):
     def List(self, request):
             stu=Student.objects.all()
             serializer=StudentSerializer(stu)
             return Response(serializer.data)
     def retrieve(self, request, pk=None):
         id =pk
         if id is not None:
             stu=Student.objects.get(id=id)
             serializer=StudentSerializer(stu)
             return Response(serializer.data)
     def create(self, request, format=None):
            serializer=StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
     def update(self, request,pk, format=None):
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':' complete Data Updated'})
            return Response(serializer.errors)
     def destroy(self, request, pk=None, format=None):
        studata=Student.objects.get(id=pk)
        studata.delete()
        return Response({'msg':'Data Deleted'})
     def partial_update(self, request, pk, format=None):
        stuDAta=Student.objects.get(id=pk)
        serializer=StudentSerializer(stuDAta,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial Data Updated'})
        return Response(serializer.errors)
#Concrete api view |way=05
class listcreate(ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
class retrieveupdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
#Generic Api view and mixin |way =04
class StudentListCreate(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class SingleStudent(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset =Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
#class based apiview |way =03
class Student_info(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
    def post(self, request, format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    def put(self, request,pk, format=None):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' complete Data Updated'})
        return Response(serializer.errors)
    def delete(self, request, pk=None, format=None):
        studata=Student.objects.get(id=pk)
        studata.delete()
        return Response({'msg':'Data Deleted'})
    def patch(self, request, pk, format=None):
        stuDAta=Student.objects.get(id=pk)
        serializer=StudentSerializer(stuDAta,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial Data Updated'})
        return Response(serializer.errors)
#function based api view |way =02
@api_view(['GET','PUT','POST','DELETE','PATCH'])
def student_api(request,id=None):
    if request.method == 'GET':
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    if request.method == 'PUT':
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' complete Data Updated'})
        return Response(serializer.errors)
    if request.method == 'PATCH':
        stuDAta=Student.objects.get(id=id)
        serializer=StudentSerializer(stuDAta,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial Data Updated'})
        return Response(serializer.errors)
    if request.method == 'DELETE':
        studata=Student.objects.get(id=id)
        studata.delete()
        return Response({'msg':'Data Deleted'})
        
# @api_view(['POST','GET'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg':' This is get request'})
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':' This is post request','data':request.data})


# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from api.models import Student
# from api.serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io
# from django.views.decorators.csrf import csrf_exempt
#way 01
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data=request.body#any thing that has been requested
#         stream=io.BytesIO(json_data)
#         pythondata =JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serialzer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serialzer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method == 'POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             # json_data=JSONRenderer().render(res)
#             # return HttpResponse(json_data,content_type='application/json')
#             return JsonResponse(res,safe=False)
#         json_data=JSONRenderer().render(serializer.errors)
#         # #when the data is not valid this would be sent.
#         # # serializer.errors is pre-defined for errors.
#         return HttpResponse(json_data,content_type='application/json')
#         #return JsonResponse(json_data,safe=False)
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata,partial=True)
#         #if we want to update data partially then we have to write
#         # partial=true or it excepts all data from front-end to update all data.if you don't write partial=True; it excepts data for every field
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Updated!'}
#             # json_data = JSONRenderer.render(data=res)
#             # return HttpResponse(json_data,content_type='application/json')
#             return JsonResponse(res,safe=False)
#         # json_data = JSONRenderer().render(data=serializer.errors)
#         # return HttpResponse(json_data,content_type='application/json')
#         return JsonResponse(res,safe=False)
#     if request.method == 'DELETE':
#         json_data=request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg':'Data Deleted!'}
#         #json_data=JSONRenderer().render(res)
#         #return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res,safe=False)
#         # you can write just one line instead of commented two lines of code.


















# from functools import partial
# import json
# from django.http import JsonResponse
# import io
# from django.http import HttpResponse
# from rest_framework.renderers import JSONRenderer
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data=request.body#any thing that has been requested
#         stream=io.BytesIO(json_data)
#         pythondata =JSONParser().parse(stream)
#         id=pythondata.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serialzer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serialzer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method == 'POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         #when the data is not valid this would be sent.
#         # serializer.errors is pre-defined for errors.
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=pythondata,partial=True)
#         #if we want to update data partially then we have to write
#         # partial=true or it excepts all data from front-end to update all data.
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Updated!'}
#             json_data = JSONRenderer.render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method == 'DELETE':
#         json_data=request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg':'Data Deleted!'}
#         # json_data=JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res,safe=False)
#         # you can write just one line instead of commented two lines of code.
    
        