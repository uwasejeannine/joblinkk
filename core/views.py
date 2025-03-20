from django.shortcuts import render, redirect


def home(request):
  
    data = {
    }
    return render(request, "home.html", data)

def worker(request):
    # View for the worker/employee submission page
    # Add any necessary code for form handling if needed
    return render(request, "worker.html")

def employer(request):
    # View for the employer submission page
    # Add any necessary code for form handling if needed
    return render(request, "employer.html")

def view_worker(request):
    # View to display workers/employees
    # You might want to fetch employees from your database
    employees = Student.objects.all()  # Assuming Student model represents employees
    return render(request, "view_worker.html", {"employees": employees})

def view_employers(request):
    # View to display employers
    # You might want to fetch employers from your database
    # This depends on how you've structured your models
    from django.db.models import Model  # Replace with your actual employer model
    employers = Model.objects.all()  # Replace with your actual query
    return render(request, "view_employers.html", {"employers": employers})

def what_we_do(request):
    # View for the "what we do" page
    return render(request, "what_we_do.html")

def announcements(request):
    # View for announcements
    # You might want to fetch announcements from your database
    return render(request, "announcements.html")

def contact(request):
    # View for contact page
    # Add form handling for contact submissions if needed
    return render(request, "contact.html")