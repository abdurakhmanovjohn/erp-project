from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from enrollments.models import Enrollment, TeacherSubject


@login_required
def student_subjects(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related(
        "subject", "subject__semester", "subject__department"
    )
    return render(
        request, "academics/student_subjects.html", {"enrollments": enrollments}
    )


@login_required
def teacher_subjects(request):
    teacher_subjects = TeacherSubject.objects.filter(
        teacher=request.user
    ).select_related("subject", "subject__semester", "subject__department")
    return render(
        request,
        "academics/teacher_subjects.html",
        {"teacher_subjects": teacher_subjects},
    )
