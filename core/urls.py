from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('worker/', views.worker, name='worker'),
    path('employer/', views.employer, name='employer'),
    path('view-worker/', views.view_worker, name='view_worker'),
    path('view-employers/', views.view_employers, name='view_employers'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('announcements/', views.announcements, name='announcements'),
    path('contact/', views.contact, name='contact'),
    
    # New URLs for edit and delete functionality
    path('edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('edit-employer/<int:employer_id>/', views.edit_employer, name='edit_employer'),
    path('delete-employer/<int:employer_id>/', views.delete_employer, name='delete_employer'),
]

# Add this if you're using file uploads
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)