from django import forms
from .models import Owner, Patient, Appointment

class OwnerCreateForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = "__all__"

class OwnerUpdateForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = "__all__"

class OwnerDeleteForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = "__all__"

class PatientCreateForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = "__all__"

class PatientUpdateForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = "__all__"

class PatientDeleteForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = "__all__"

class AppointmentCreateForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = "__all__"

class AppointmentUpdateForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = "__all__"

class AppointmentDeleteForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = "__all__"