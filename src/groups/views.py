from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import GroupSerializer, CategorySerializer
from rest_framework.response import Response
from .models import Group, Category
import json

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Listgroups(viewsets.ViewSet):

    def list(self, request, format=None):
        obj = Category.objects.all()
        return Response(obj.groups.all())

# Normal views

def categoryList(request):
    
    obj = Category.objects.all()

    for o in obj:
        context = {
            'title':o.name,
        }
    print(context)
    return  render(request, 'group-list.html', context = context)
