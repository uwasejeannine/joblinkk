from django.urls.conf import include, path
from rest_framework import routers
from .views import CourseViewSet, EventViewSet, StudentViewSet, TrainerViewSet

router= routers.DefaultRouter()
router.register(r"student", StudentViewSet)
router.register(r"trainer", TrainerViewSet)
router.register(r"course", CourseViewSet)
router.register(r"calendary", EventViewSet)

urlpatterns=[
    path("", include(router.urls)),
]