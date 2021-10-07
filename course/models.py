from django.db import models

class Course(models.Model):
    course_name= models.CharField(
        max_length=20, null=True
    )
    course_trainer= models.CharField(
        max_length=12, null=True
    )
    course_code= models.CharField(
        max_length=12, null=True
    )
    course_description= models.FileField(upload_to='documents/', null=True)
    course_duration= models.PositiveSmallIntegerField(null=True)
    syllabus= models.TextField(
        max_length=700, null=True
    )

# Create your models here.
