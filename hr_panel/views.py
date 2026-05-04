from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def hr_dashboard(request):
    if request.user.role != 'hr':
        return redirect('login')

    candidates = Candidate.objects.all()
    return render(request, 'hr_panel/dashboard.html', {'candidates': candidates})


@login_required
def user_logout(request):
    logout(request)          
    request.session.flush()  
    return redirect('login')


@login_required
def add_candidate(request):
    if request.method == "POST":
        name = request.POST['name']
        Candidate.objects.create(name=name)
        return redirect('hr_dashboard')


@login_required
def update_stage(request, id):
    candidate = get_object_or_404(Candidate, id=id)

    if request.method == "POST":
        action = request.POST.get('action')

        
        if action == "reject":
            candidate.selected = False
            candidate.remarks = request.POST.get('remarks')
            candidate.save()
            return redirect('hr_dashboard')

        if action == "select":
            if candidate.stage < 5:
                candidate.stage += 1
            else:
                candidate.selected = True
                candidate.remarks = request.POST.get('remarks')
                candidate.joining_date = request.POST.get('joining_date')

            candidate.save()
            return redirect('hr_dashboard')

    return render(request, 'hr_panel/update.html', {'candidate': candidate})