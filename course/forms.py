from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= "__all__"