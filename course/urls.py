
from django.urls import path
from .views import course_form, course_list, course_profile, edit_course

urlpatterns=[
    path("register/", course_form, name="course_form"),
    path("list/", course_list, name="course_list"),
    path("profile/<int:id>/", course_profile, name="course_profile"),
    path("edit/<int:id>/", edit_course, name="edit_course")
]
