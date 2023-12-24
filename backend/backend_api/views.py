from rest_framework import viewsets
from django.shortcuts import render
from backend_api.serializers import StudentSerializer
from .models import Student
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()