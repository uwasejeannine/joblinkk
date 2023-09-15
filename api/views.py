from django.shortcuts import render
from .serializers import CourseSerializer, EventSerializer, StudentSerializer, TrainerSerializer
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendary.models import Event


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset= Trainer.objects.all()
    serializer_class= TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class= CourseSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class= EventSerializer

# Create your views here.
