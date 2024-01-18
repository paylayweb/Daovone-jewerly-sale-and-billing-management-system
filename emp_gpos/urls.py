from django.urls import path, include
from django.contrib import admin
from django.conf.urls import *
from . import views

urlpatterns = [
    path('',views.emp_gpos, name='index'),
    path('home/', views.home, name='home')
]