from django import forms
from accounts.models import User
from .models import StudentProfile, TeacherProfile

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'user_role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['grade', 'bio']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['subject', 'bio']