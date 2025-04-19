from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Category, Enrollment, Mentor
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'courses/index.html')

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})


def online_courses(request):
    courses = Course.objects.filter(is_online=True)
    return render(request, 'courses/online_courses.html', {'courses': courses})

def offline_courses(request):
    courses = Course.objects.filter(is_online=False)
    return render(request, 'courses/offline_courses.html', {'courses': courses})


def mentors(request):
    mentors = Mentor.objects.all()
    return render(request, 'courses/mentors.html', {'mentors': mentors})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('my_courses')

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'courses/enroll.html', {'enrollments': enrollments})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})
