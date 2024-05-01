from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class MovieViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer

class StudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = StudentModel.objects.all()
	serializer_class = StudentSerializer
