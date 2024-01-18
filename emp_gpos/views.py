from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from django.contrib.auth.models import super_user
from django.contrib.auth.views import LoginView


def emp_gpos(request):
    return render(request, 'index.html')
 
def home(LoginView):
    return render(LoginView, 'home.html')