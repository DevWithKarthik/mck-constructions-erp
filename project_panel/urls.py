from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.project_dashboard, name='project_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_project, name='add_project'),
    path('detail/<int:id>/', views.project_detail, name='project_detail'),
    path('add-task/<int:id>/', views.add_task, name='add_task'),
    path('update-task/<int:id>/', views.update_task, name='update_task'),
]
