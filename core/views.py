from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q 
from .models import Employee, Employer
from .forms import EmployeeForm, EmployerForm

# --- Helper Functions ---

def is_admin(user):
    return user.is_superuser

# --- Authentication Views ---

def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password_confirm')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match / Amagambo y'ibanga ntabwo ahura")
            return redirect('signup') 
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken / Izina ryarafashwe")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, password=pass1)
            user.save()
            login(request, user)
            messages.success(request, "Account created! / Konti yaremwe!")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('signup')

    return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Murakaza neza, {username}!")
                
                # --- FIX STARTS HERE ---
                next_url = request.POST.get('next')
                if next_url: # Only redirect if next_url is NOT empty
                    return redirect(next_url)
                # --- FIX ENDS HERE ---
                
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "Murabeho! (Logged out successfully)")
    return redirect('home')

# --- Main Views ---

def home(request):
    return render(request, "home.html")

@login_required(login_url='home') 
def worker(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_worker')
    else:
        form = EmployeeForm()
    return render(request, "worker.html", {'form': form})

@login_required(login_url='home')
def employer(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_employers')
    else:
        form = EmployerForm()
    return render(request, "employer.html", {'form': form})

# --- Search Enabled List Views ---

@login_required(login_url='home')
def view_worker(request):
    employees = Employee.objects.all().order_by('-id')

    # Search Logic
    category_query = request.GET.get('category')
    search_query = request.GET.get('search')

    if category_query:
        employees = employees.filter(position__icontains=category_query)
    
    if search_query:
        employees = employees.filter(
            Q(name__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(position__icontains=search_query)
        )

    return render(request, "view_worker.html", {"employees": employees})

@login_required(login_url='home')
def view_employers(request):
    employers = Employer.objects.all().order_by('-id')

    # Search Logic
    category_query = request.GET.get('category')
    location_query = request.GET.get('location')
    company_query = request.GET.get('company')

    if category_query:
        employers = employers.filter(position__icontains=category_query)
    
    if location_query:
        employers = employers.filter(location__icontains=location_query)

    if company_query:
        employers = employers.filter(company__icontains=company_query)

    return render(request, "view_employers.html", {"employers": employers})

# --- Static Pages ---

@login_required(login_url='home')
def what_we_do(request):
    return render(request, "what_we_do.html")

@login_required(login_url='home')
def announcements(request):
    return render(request, "announcements.html")

@login_required(login_url='home')
def contact(request):
    return render(request, "contact.html")

# --- Edit Views (Accessible to logged-in users) ---

@login_required(login_url='home')
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_worker')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "edit_worker.html", {'form': form, 'employee': employee})

@login_required(login_url='home')
def edit_employer(request, employer_id):
    employer = get_object_or_404(Employer, id=employer_id)
    if request.method == 'POST':
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect('view_employers')
    else:
        form = EmployerForm(instance=employer)
    return render(request, "edit_employer.html", {'form': form, 'employer': employer})

# --- Delete Views (ADMIN ONLY) ---

@user_passes_test(is_admin) # Only superusers can access this
def delete_employee(request, employee_id):
    if request.method == 'POST' or request.method == 'GET': 
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            messages.success(request, "Employee deleted successfully (Admin Action)")
        except Employee.DoesNotExist:
            messages.error(request, "Employee not found")
    return redirect('view_worker')

@user_passes_test(is_admin) # Only superusers can access this
def delete_employer(request, employer_id):
    if request.method == 'POST' or request.method == 'GET':
        try:
            employer = Employer.objects.get(id=employer_id)
            employer.delete()
            messages.success(request, "Employer deleted successfully (Admin Action)")
        except Employer.DoesNotExist:
            messages.error(request, "Employer not found")
    return redirect('view_employers')