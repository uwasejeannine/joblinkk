from django.urls  import path
from .views import home, worker,employer,view_worker,view_employers,what_we_do,announcements,contact

urlpatterns = [
    path('',  home, name='home'),
    path('worker/', worker, name='worker'),
    path('employer/', employer, name='employer'),
    path('view-worker/', view_worker, name='view_worker'),
    path('view-employers/', view_employers, name='view_employers'),
    path('what-we-do/', what_we_do, name='what_we_do'),
    path('announcements/', announcements, name='announcements'),
    path('contact/', contact, name='contact'),
]
