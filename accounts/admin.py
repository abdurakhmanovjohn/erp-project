from django.contrib import admin
from .models import User, StudentProfile, TeacherProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_role', 'is_staff')
    list_filter = ('user_role',)
    search_fields = ('username',)


admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
