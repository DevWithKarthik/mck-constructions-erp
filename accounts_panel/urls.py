from django.urls import path
from . import views

urlpatterns = [
    path('accounts-dashboard/', views.accounts_dashboard, name='accounts_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-income/', views.add_income, name='add_income'),
]