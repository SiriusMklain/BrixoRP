from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app2.models import UserProfile


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }