from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add-daily/', views.add_daily, name='add_daily'),
    path('add-weekly/', views.add_weekly, name='add_weekly'),
    path('add-monthly/', views.add_monthly, name='add_monthly'),
]