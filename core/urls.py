from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Authentication Paths
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup'), # Required for the Signup page
    path('login/', views.login_user, name='login'),    # Required for the Login modal
    path('logout/', views.logout_user, name='logout'), # Required for the Logout button

    # Main Page Paths (Protected)
    path('worker/', views.worker, name='worker'),
    path('employer/', views.employer, name='employer'),
    path('view-worker/', views.view_worker, name='view_worker'),
    path('view-employers/', views.view_employers, name='view_employers'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('announcements/', views.announcements, name='announcements'),
    path('contact/', views.contact, name='contact'),
    
    # Edit/Delete Paths
    path('edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('edit-employer/<int:employer_id>/', views.edit_employer, name='edit_employer'),
    path('delete-employer/<int:employer_id>/', views.delete_employer, name='delete_employer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)