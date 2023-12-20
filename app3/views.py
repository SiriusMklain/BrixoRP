from django.shortcuts import render

from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'app3/index.html'
    form_class = CustomAuthenticationForm
