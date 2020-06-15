from django.shortcuts import render
from .models import Mylessons
from django.views.generic import ListView
class MyLessonsView(ListView):
    model = Mylessons
    template_name = 'landing/index.html'

# Create your views here.
