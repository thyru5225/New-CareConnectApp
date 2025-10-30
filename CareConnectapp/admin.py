from django.contrib import admin
from CareConnectapp.models import Patient
from CareConnectapp.models import Doctor
from CareConnectapp.models import Appointment
from CareConnectapp.models import Contact

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Contact)
