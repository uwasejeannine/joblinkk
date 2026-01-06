from django.contrib import admin
from .models import Employee, Employer

# Configure the Employee (Worker) Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # What columns to show in the list
    list_display = ('name', 'position', 'email', 'phone', 'experience', 'created_at')
    
    # Add a search bar for these fields
    search_fields = ('name', 'position', 'email')
    
    # Add sidebar filters
    list_filter = ('position', 'experience')
    
    # Formatting
    ordering = ('-id',) # Newest first
    readonly_fields = ('created_at',) # Prevent editing the creation date

# Configure the Employer Admin
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'email', 'phone', 'location', 'rating', 'created_at')
    
    search_fields = ('company', 'position', 'email', 'location')
    
    list_filter = ('location', 'rating')
    
    ordering = ('-id',)
    readonly_fields = ('created_at',)

# Optional: Customize the Admin Site Header
admin.site.site_header = "JobLink Admin Panel"
admin.site.site_title = "JobLink Portal"
admin.site.index_title = "Welcome to JobLink Management"