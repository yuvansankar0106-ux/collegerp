from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Auto create student user for Render
try:
    if not User.objects.filter(username='student').exists():
        User.objects.create_user('student', password='1234')
except:
    pass

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['logged_in'] = True
            return redirect('student_home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_home(request):
    return render(request, 'students/home.html')

# ... unakku irukka matha functions apdiye irukkatum da keela