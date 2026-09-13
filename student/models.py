from django.db import models
from django.contrib.auth.models import User
class ExamMark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    cia_marks = models.IntegerField()
    semester = models.IntegerField()
def profile(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    # Dummy student data - nee maathalam
    student_data = {
        'name': 'Yuvan',
        'age': 20,
        'roll_no': 'CS101',
        'email': 'yuvan@college.com',
        'dept': 'CSE'
    }
    return render(request, 'students/profile.html', {'student': student_data})