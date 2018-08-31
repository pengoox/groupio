from django.shortcuts import render
from rest_framework import viewsets
from .serializer import GroupSerializer, CategorySerializer

from .models import Group, Category

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

