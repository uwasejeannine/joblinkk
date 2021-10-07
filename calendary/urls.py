from django.urls  import path
from . import views
from .views import event_form

urlpatterns=[
      path("calendar/", views.CalendarView.as_view() , name='calendar'),
      path("events/", views.event, name='event'),
      path("list/", event_form, name="event_form"),
      # path("event_edit/", views.event, name='event_edit'),
      path("event_new/", views.event_form, name='event_new'),
#       path("event")
# url(r'^event/new/$', views.event, name='event_new'),
]
