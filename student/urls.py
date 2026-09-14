from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('/login/')),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.student_home, name='student_home'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('attendance/', views.attendance, name='attendance'),
]