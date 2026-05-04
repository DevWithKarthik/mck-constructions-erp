from django.shortcuts import render, redirect
from .models import DailyTask, WeeklyExpense, MonthlySalary
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



@never_cache  
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')

    daily = DailyTask.objects.all().order_by('-date')
    weekly = WeeklyExpense.objects.all().order_by('-date')
    monthly = MonthlySalary.objects.all()

    return render(request, 'admin_panel/dashboard.html', {
        'daily': daily,
        'weekly': weekly,
        'monthly': monthly
    })


# ✅ Proper logout view
@login_required
def user_logout(request):
    logout(request)          # Clears the session from DB/cache
    request.session.flush()  # Extra safety: destroys session data
    return redirect('login')


# ADD Daily Task
@login_required
def add_daily(request):
    if request.method == "POST":
        name = request.POST['employee_name']
        present = request.POST.get('present') == 'on'
        DailyTask.objects.create(employee_name=name, present=present)
        return redirect('admin_dashboard')


# ADD Weekly Expense
@login_required
def add_weekly(request):
    if request.method == "POST":
        WeeklyExpense.objects.create(
            title=request.POST['title'],
            person_name=request.POST['person_name'],
            amount=request.POST['amount'],
            description=request.POST['description']
        )
        return redirect('admin_dashboard')


# ADD Monthly Salary
@login_required
def add_monthly(request):
    if request.method == "POST":
        MonthlySalary.objects.create(
            employee_name=request.POST['employee_name'],
            salary=request.POST['salary'],
            month=request.POST['month'],
            paid=request.POST.get('paid') == 'on'
        )
        return redirect('admin_dashboard')