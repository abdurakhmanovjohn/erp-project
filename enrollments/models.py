from django.conf import settings
from django.db import models

from academics.models import Subject

User = settings.AUTH_USER_MODEL


class Enrollment(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"role": "STUDENT"}
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "subject")

    def __str__(self):
        return f"{self.student} -> {self.subject}"


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"role": "TEACHER"}
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("teacher", "subject")

    def __str__(self):
        return f"{self.teacher} teaches {self.subject}"
