from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

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

@login_required
def profile(request):
    return HttpResponse(f"""
    <div style="padding:40px; font-family:Arial">
    <h1>👤 Profile</h1>
    <p><b>Username:</b> {request.user.username}</p>
    <p><b>Name:</b> Yuvan Student</p>
    <p><b>Roll No:</b> CS2023001</p>
    <br><a href="/home/" style="background:blue;color:white;padding:10px 20px;text-decoration:none;border-radius:5px">Back to Home</a>
    </div>
    """)

@login_required
def courses(request):
    return HttpResponse("""
    <div style="padding:40px; font-family:Arial">
    <h1>📚 Courses</h1>
    <p>1. Python Programming</p>
    <p>2. DBMS</p>
    <p>3. Data Structures</p>
    <br><a href="/home/" style="background:blue;color:white;padding:10px 20px;text-decoration:none;border-radius:5px">Back to Home</a>
    </div>
    """)

@login_required
def attendance(request):
    return HttpResponse("""
    <div style="padding:40px; font-family:Arial">
    <h1>📊 Attendance - 85%</h1>
    <p>Present: 85 days</p>
    <p>Absent: 15 days</p>
    <br><a href="/home/" style="background:blue;color:white;padding:10px 20px;text-decoration:none;border-radius:5px">Back to Home</a>
    </div>
    """)

@login_required
def fees(request):
    return HttpResponse('<h1>Fees Page</h1><a href="/home/">Back</a>')

@login_required
def results(request):
    return HttpResponse('<h1>Results Page</h1><a href="/home/">Back</a>')

@login_required
def library(request):
    return HttpResponse('<h1>Library Page</h1><a href="/home/">Back</a>')