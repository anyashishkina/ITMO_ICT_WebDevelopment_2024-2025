from django import forms
from django.contrib.auth.models import User
from .models import Hw, Profile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Создание профиля пользователя
            profile = Profile(user=user, role=self.cleaned_data['role'])
            profile.save()
        return user


class HwSubmissionForm(forms.ModelForm):
    subject = forms.CharField(max_length=100, label='Предмет')

    class Meta:
        model = Hw
        fields = ['subject', 'description']
