from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.cache import never_cache


@login_required
@never_cache
def project_dashboard(request):
    if request.user.role != 'project':
        return redirect('login')

    projects = Project.objects.all()

    # Calculate stats
    total_projects = projects.count()
    completed_projects = projects.filter(status='completed').count()
    active_projects = projects.filter(status='ongoing').count()

    # Add progress calculation
    project_data = []

    for p in projects:
        total_tasks = p.tasks.count()
        completed_tasks = p.tasks.filter(status='completed').count()

        progress = 0
        if total_tasks > 0:
            progress = int((completed_tasks / total_tasks) * 100)

        project_data.append({
            'project': p,
            'progress': progress
        })

    return render(request, 'project_panel/dashboard.html', {
        'project_data': project_data,
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'active_projects': active_projects
    })
    
@login_required
def user_logout(request):
    logout(request)          
    request.session.flush()  
    return redirect('login')


@login_required
def add_project(request):
    if request.method == "POST":
        Project.objects.create(
            name=request.POST['name'],
            location=request.POST['location'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            status=request.POST['status']
        )
        return redirect('project_dashboard')


@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.tasks.all()

    return render(request, 'project_panel/detail.html', {
        'project': project,
        'tasks': tasks
    })


@login_required
def add_task(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        Task.objects.create(
            project=project,
            title=request.POST['title']
        )
        return redirect('project_detail', id=id)


@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.status = request.POST['status']
        task.save()

        return redirect('project_detail', id=task.project.id)