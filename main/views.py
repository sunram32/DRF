from django.shortcuts import render
from main.models import *
from rest_framework import viewsets
from main.serializers import TableASerializer, TableBSerializer

# Create your views here.
class TableAViewSet(viewsets.ModelViewSet):
    queryset = TableA.objects.all()
    serializer_class = TableASerializer
    http_method_names = ['get', 'post']

class TableBViewSet(viewsets.ModelViewSet):
    queryset = TableB.objects.all()
    serializer_class = TableBSerializer
    http_method_names = ['get', 'post']