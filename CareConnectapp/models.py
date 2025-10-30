from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    idno = models.IntegerField()
    phonenumber = models.IntegerField()
    dob = models.DateField()
    age = models.IntegerField()
    admitteddatetime = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    idno = models.IntegerField()

    def __str__(self):
        return self.fullname

class Appointment(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      phone = models.IntegerField()
      datetime = models.DateTimeField()
      department = models.CharField(max_length=100)
      doctor = models.CharField(max_length=100)
      message = models.TextField()

      def __str__(self):
          return self.name

class Contact(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      subject = models.TextField()
      message = models.TextField()

      def __str__(self):
          return self.name

