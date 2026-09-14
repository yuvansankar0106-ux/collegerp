from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.student_home, name='student_home'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('attendance/', views.attendance, name='attendance'),
]