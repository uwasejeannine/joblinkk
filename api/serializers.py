from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendary.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= ("first_name", "last_name","age","date_of_birth","national_id","profile","nationality","nationality","gender","guardian_name","email_address","date_of_enrollment","course_name","languages","laptop_number")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Trainer
        fields=("first_name", "last_name","age","gender","bio","email_address","phone_number","salary","profile","contract","date_hired")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields=("course_name","course_trainer","course_code","course_description","course_duration","syllabus")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields=("event_name","event_task","event_duration","start_time","end_time")