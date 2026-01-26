from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required

@login_required
@role_required('ADMIN')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
@role_required('TEACHER')
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


@login_required
@role_required('STUDENT')
def student_dashboard(request):
    return render(request, 'student_dashboard.html')
