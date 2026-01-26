from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel



class User(AbstractUser, BaseModel):
    USER_ROLE = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher'),
    )

    user_role = models.CharField(max_length=29, choices=USER_ROLE, default='STUDENT')
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to='users_photo/', default='user_photo/default_user.png', blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return f"{self.username} ({self.user_role})"


class StudentProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50, blank=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


