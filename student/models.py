from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    roll_no = models.CharField(max_length=20, blank=True)
    dept = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    staff = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.course_name

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    total_classes = models.IntegerField(default=0)
    attended = models.IntegerField(default=0)
    
    def __str__(self):
        return self.subject