from django.shortcuts import render,redirect 
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from calendary.models import Event


def home(request):
    if request.user.is_authenticated:
       students= Student.objects.count()
       trainers= Trainer.objects.count()
       courses= Course.objects.count()
       events= Event.objects.count()
       data={ "students": students, "trainers": trainers, "courses":courses, "events":events}
       return render(request,"home.html", data)
    else:
        return redirect("auth_login")


   



