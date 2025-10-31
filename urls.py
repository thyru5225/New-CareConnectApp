
from django.contrib import admin
from django.urls import path
from CareConnectapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('appointments/', views.appointment, name='appointments'),
    path('departments/', views.departments, name= 'departments'),
    path('contact/', views.contacts, name= 'contact'),
    path('showappointment/', views.showappointment, name= 'showappointment'),
    path('department/', views.department, name= 'departments'),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id>', views.edit),

]

