from django.urls import path
from . import views

urlpatterns = [
    # path('', views.course_list, name='course_list'),
    path('', views.offline_courses, name='offline_courses'),
    path('online/', views.online_courses, name='online_courses'),
    path('mentors/', views.mentors, name='mentors'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
