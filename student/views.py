from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        if request.POST.get('username') == 'student' and request.POST.get('password') == '1234':
            request.session['logged_in'] = True
            return redirect('home')
        return render(request, 'students/login.html', {'error': 'Wrong Username or Password!'})
    return render(request, 'students/login.html')

def home(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request, 'students/home.html')

def profile(request):
    return render(request, 'students/profile.html')

def courses(request):
    courses_list = ["Python Programming - CS101", "DBMS - CS102", "Web Tech - CS103"]
    return render(request, 'students/courses.html', {'courses': courses_list})

def attendance(request):
    return render(request, 'students/attendance.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')
def cia_marks(request):
    marks = ExamMark.objects.filter(student=request.user)
    return render(request, 'students/examination.html', {'marks': marks})
def profile(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    
    # Session la iruntha data edukkum, illana default
    student_data = request.session.get('student_data', {
        'name': '',
        'age': '',
        'roll_no': '',
        'email': '',
        'dept': ''
    })
    
    if request.method == 'POST':
        student_data = {
            'name': request.POST.get('name'),
            'age': request.POST.get('age'),
            'roll_no': request.POST.get('roll_no'),
            'email': request.POST.get('email'),
            'dept': request.POST.get('dept')
        }
        request.session['student_data'] = student_data
    
    return render(request, 'students/profile.html', {'student': student_data})