from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExamMark

@login_required(login_url='/login/')
def student_home(request):
    return render(request, 'students/home.html')

@login_required(login_url='/login/')
def profile(request):
    if not request.session.get('logged_in'):
        return redirect('login')
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
    def home(request):
        return render(request, 'students/home.html')