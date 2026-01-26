from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, StudentProfile, TeacherProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'STUDENT':
            StudentProfile.objects.create(user=instance)
        elif instance.user_role == 'TEACHER':
            TeacherProfile.objects.create(user=instance)
