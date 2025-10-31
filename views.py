from django.shortcuts import render, redirect, get_object_or_404
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
       return redirect('/appointments')
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

def delete(request,id):
    myappoint = get_object_or_404(Appointment, id = id)
    myappoint.delete()
    messages.success(request, 'Your appointment has been deleted')
    return redirect('/showappointment')

def edit(request,id):
    editappointment = get_object_or_404(Appointment, id = id)
    if request.method == "POST":
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.datetime = request.POST.get('date')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.message = request.POST.get('message')

        editappointment.save()
        messages.success(request, 'Your appointment has been updated')
        return redirect('/showappointment')

    return render(request, 'edit.html', {'editappointment': editappointment})
