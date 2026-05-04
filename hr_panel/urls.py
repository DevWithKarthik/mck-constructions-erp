from django.urls import path
from . import views

urlpatterns = [
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_candidate, name='add_candidate'),
    path('update/<int:id>/', views.update_stage, name='update_stage'),
]