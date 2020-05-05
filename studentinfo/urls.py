"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentinfo import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('studentenrollment/', views.studentenrollment, name='studentenrollment'),
    path('coursedetails/', views.coursedetails, name='coursedetails'),
    path('coursedetailsinfo/', views.coursedetailsinfo, name='coursedetailsinfo'),
    path('studentdetailsinfo/', views.studentdetailsinfo, name='studentdetailsinfo'),
    path('savedata/', views.savedata, name='savedata'),


]
