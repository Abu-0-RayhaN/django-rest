from cgitb import lookup
import imp
from this import d
from urllib import request
from django.http import response
from .models import Status #Model
from .serializers import StatusSerializers #serializer based on Status Model
from rest_framework.views import APIView

from rest_framework import generics,parsers
  
class StatusListCreateView(generics.ListCreateAPIView):
    queryset =Status.objects.all()
    serializer_class = StatusSerializers
    parser_classes=[parsers.FormParser, parsers.MultiPartParser]
   
class StatusDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    lookup_field = "id"
    parsers_classes=[parsers.FormParser,parsers.MultiPartParser]
    
    
    