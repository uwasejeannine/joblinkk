from django.urls.conf import include, path
from rest_framework import routers
# from .views import CourseViewSet, EventViewSet, StudentViewSet, TrainerViewSet

router= routers.DefaultRouter()


urlpatterns=[
    path("", include(router.urls)),
]