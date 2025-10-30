from django.shortcuts import render, redirect
from CareConnectapp.models import *
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'About.html')

def service(request):
    return render(request, 'services.html')
def department(request):
    return render(request, 'departments.html')


def appointment(request):
    if request.method == "POST":
       myappointment = Appointment(
           name = request.POST['name'],
           email = request.POST['email'],
           phone = request.POST['phone'],
           datetime = request.POST['date'],
           department = request.POST['department'],
           doctor = request.POST['doctor'],
           message = request.POST['message'],
       )
       myappointment.save()
       messages.success(request, 'Your appointment has been created')
       return redirect('/showappointment')
    else:
        return render(request, 'appointments.html')

def departments(request):
    return render(request, 'departments.html')

def contacts(request):
    if request.method == "POST":
        mycontacts = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],


        )
        mycontacts.save()
        messages.success(request, 'Your contact has been created')
        return redirect('/contact')
    else:
        messages.error(request, 'Unable to save your contact')
        return render(request, 'contact.html')

def showappointment(request):
    allappointments = Appointment.objects.all()
    return render(request, 'showappointment.html', {"allappointments": allappointments})