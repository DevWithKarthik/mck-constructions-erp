from django.shortcuts import render, redirect
from .models import Expense, Income
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.cache import never_cache


@login_required
@never_cache
def accounts_dashboard(request):
    if request.user.role != 'accounts':
        return redirect('login')

    expenses = Expense.objects.all().order_by('-date')
    incomes = Income.objects.all().order_by('-received_on')

    total_expense = sum(e.amount for e in expenses)
    total_income = sum(i.amount for i in incomes)
    profit = total_income - total_expense

    return render(request, 'accounts_panel/dashboard.html', {
        'expenses': expenses,
        'incomes': incomes,
        'total_expense': total_expense,
        'total_income': total_income,
        'profit': profit
    })
    
@login_required
def user_logout(request):
    logout(request)          
    request.session.flush()  
    return redirect('login')


def add_expense(request):
    if request.method == "POST":
        Expense.objects.create(
            category=request.POST['category'],
            amount=request.POST['amount'],
            description=request.POST['description']
        )
        return redirect('accounts_dashboard')


def add_income(request):
    if request.method == "POST":
        Income.objects.create(
            source=request.POST['source'],
            amount=request.POST['amount']
        )
        return redirect('accounts_dashboard')