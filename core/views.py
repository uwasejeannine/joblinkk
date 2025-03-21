from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Employee, Employer
from .forms import EmployeeForm, EmployerForm

def home(request):
    data = {}
    return render(request, "home.html", data)

def worker(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_worker')
    else:
        form = EmployeeForm()
    return render(request, "worker.html", {'form': form})

def employer(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_employers')
    else:
        form = EmployerForm()
    return render(request, "employer.html", {'form': form})

def view_worker(request):
    employees = Employee.objects.all()
    return render(request, "view_worker.html", {"employees": employees})

def view_employers(request):
    employers = Employer.objects.all()
    return render(request, "view_employers.html", {"employers": employers})

def what_we_do(request):
    return render(request, "what_we_do.html")

def announcements(request):
    return render(request, "announcements.html")

def contact(request):
    return render(request, "contact.html")

# Add these new views for editing and deleting employees
def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_worker')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "edit_worker.html", {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    if request.method == 'POST':
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Employee not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

# Add these new views for editing and deleting employers
def edit_employer(request, employer_id):
    employer = Employer.objects.get(id=employer_id)
    if request.method == 'POST':
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('view_employers')
    else:
        form = EmployerForm(instance=employer)
    return render(request, "edit_employer.html", {'form': form, 'employer': employer})

def delete_employer(request, employer_id):
    if request.method == 'POST':
        try:
            employer = Employer.objects.get(id=employer_id)
            employer.delete()
            return JsonResponse({'success': True})
        except Employer.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Employer not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})