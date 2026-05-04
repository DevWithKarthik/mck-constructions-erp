from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        # ✅ Redirect to login instead of auto login
        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'hr':
                return redirect('hr_dashboard')
            elif user.role == 'accounts':
                return redirect('accounts_dashboard')
            elif user.role == 'project':
                return redirect('project_dashboard')
            else:
                return redirect('dashboard')

    return render(request, 'accounts/login.html')


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')