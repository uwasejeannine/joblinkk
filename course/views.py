from django.shortcuts import render
from .forms import CourseForm
from django.shortcuts import render
from .models import Course

def course_form(request):
    if request.method=="POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_form')
        else:
            print(form.errors)
    else:
        form= CourseForm()
    return render(request,"course_form.html",{"form":form})

def course_list(request):
    courses= Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})
def course_profile(request,id):
    course= Course.objects.get(id=id)
    return render(request,"course_profile.html",{"course":course})

def edit_course(request, id):
    course= Course.objects.get(id=id)
    if request.method == "POST":
        form=CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
        return redirect("course_profile", id=course.id)
    else:
        form= CourseForm(instance=course)
        return render(request,"edit_course.html", {"form":form})


# Create your views here.
