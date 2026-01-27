from django.urls import path

from . import views

urlpatterns = [
    path("student/subjects/", views.student_subjects, name="student_subjects"),
    path("teacher/subjects/", views.teacher_subjects, name="teacher_subjects"),
]
