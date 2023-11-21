from django.shortcuts import render
from .models import *


def app(request):
    return render(request, 'app/index.html')
