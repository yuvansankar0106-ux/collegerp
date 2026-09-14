from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

try:
    if not User.objects.filter(username='student').exists():
        User.objects.create_user('student', password='1234')
except:
    pass

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_home')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('student_home')
        else:
            messages.error(request, 'Invalid')
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_home(request):
    return render(request, 'students/home.html')

@csrf_exempt
@login_required
def profile(request):
    if request.method == 'POST':
        request.session['p_name'] = request.POST.get('name','')
        request.session['p_roll'] = request.POST.get('roll','')
        request.session['p_dept'] = request.POST.get('dept','')
        request.session['p_email'] = request.POST.get('email','')
        request.session.modified = True
        return redirect('profile')
    name = request.session.get('p_name','')
    roll = request.session.get('p_roll','')
    dept = request.session.get('p_dept','')
    email = request.session.get('p_email','')
    return HttpResponse(f"""
    <div style="padding:20px;font-family:Arial;max-width:500px;margin:auto">
    <h2>Profile Saved: {name} ✅</h2>
    <form method="POST">
    Name:<br><input name="name" value="{name}" placeholder="Type name" style="width:100%;padding:10px"><br><br>
    Roll No:<br><input name="roll" value="{roll}" placeholder="Type roll" style="width:100%;padding:10px"><br><br>
    Dept:<br><input name="dept" value="{dept}" placeholder="CSE" style="width:100%;padding:10px"><br><br>
    Email:<br><input name="email" value="{email}" placeholder="email" style="width:100%;padding:10px"><br><br>
    <button type="submit" style="background:green;color:white;padding:12px 25px;border:none;border-radius:5px">💾 SAVE</button>
    </form><br><a href="/home/">Back to Home</a>
    </div>
    """)

@csrf_exempt
@login_required
def courses(request):
    clist = request.session.get('courses', [])
    if request.method == 'POST':
        clist.append({'name':request.POST.get('cname',''), 'code':request.POST.get('ccode','')})
        request.session['courses'] = clist
        request.session.modified = True
        return redirect('courses')
    html = "".join([f"<p>📚 {c['name']} - {c['code']}</p>" for c in clist])
    return HttpResponse(f"""
    <div style="padding:20px;font-family:Arial;max-width:500px;margin:auto">
    <h2>Courses</h2>
    <form method="POST">
    Course Name:<br><input name="cname" style="width:100%;padding:10px"><br><br>
    Course Code:<br><input name="ccode" style="width:100%;padding:10px"><br><br>
    <button type="submit" style="background:green;color:white;padding:10px 20px;border:none">ADD</button>
    </form><hr><h3>Saved:</h3>{html if html else 'Empty - type pannu da'}<br><br><a href="/home/">Back</a></div>
    """)

@csrf_exempt
@login_required
def attendance(request):
    alist = request.session.get('atts', [])
    if request.method == 'POST':
        alist.append({'sub':request.POST.get('sub',''), 'per':request.POST.get('per','')})
        request.session['atts'] = alist
        request.session.modified = True
        return redirect('attendance')
    html = "".join([f"<p>{a['sub']} - {a['per']}%</p>" for a in alist])
    return HttpResponse(f"""
    <div style="padding:20px;font-family:Arial;max-width:500px;margin:auto">
    <h2>Attendance</h2>
    <form method="POST">
    Subject:<br><input name="sub" style="width:100%;padding:10px"><br><br>
    Percentage:<br><input name="per" style="width:100%;padding:10px"><br><br>
    <button type="submit" style="background:green;color:white;padding:10px 20px;border:none">SAVE</button>
    </form><hr><h3>Saved:</h3>{html if html else 'Empty'}<br><br><a href="/home/">Back</a></div>
    """)

@login_required
def fees(request): return HttpResponse('<h1>Fees</h1><a href="/home/">Back</a>')
@login_required
def results(request): return HttpResponse('<h1>Results</h1><a href="/home/">Back</a>')
@login_required
def library(request): return HttpResponse('<h1>Library</h1><a href="/home/">Back</a>')