from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    request.session.flush()
    return redirect('login')

@login_required(login_url='/login/')
def student_home(request):
    return render(request, 'students/home.html')

@login_required(login_url='/login/')
def profile(request):
    student_data = {
        'name': 'Yuvan',
        'age': 20,
        'roll_no': 'CS101',
        'email': 'yuvan@college.com',
        'dept': 'CSE'
    }
    return render(request, 'students/profile.html', {'student': student_data})

@login_required(login_url='/login/')
def courses(request):
    return render(request, 'students/courses.html')

@login_required(login_url='/login/')
def attendance(request):
    return render(request, 'students/attendance.html')