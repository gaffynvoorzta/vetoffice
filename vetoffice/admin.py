from django.contrib import admin
from .models import Owner, Patient, Appointment

# Register your models here.
admin.site.register(Owner)
admin.site.register(Patient)
admin.site.register(Appointment)
