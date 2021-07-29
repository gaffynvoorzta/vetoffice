from django.shortcuts import render, redirect
from .models import Owner, Patient, Appointment
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from .forms import OwnerCreateForm, OwnerDeleteForm, OwnerUpdateForm, PatientCreateForm, PatientDeleteForm, PatientUpdateForm, AppointmentCreateForm, AppointmentUpdateForm, AppointmentDeleteForm
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

class SignUp(CreateView):
  form_class = UserCreationForm
  #success_url = reverse_lazy("login")
  success_url = reverse_lazy("office")
  template_name = "registration/signup.html"

def home(request):
  try:
    found_pet = random.choice(Patient.objects.all())
  except Patient.DoesNotExist:
    raise Http404()
  context = {"name": request.user, "pet": found_pet}
  return render(request, "vetoffice/home.html", context)

@login_required
def office(request):
  context = {"name": request.user}
  return render(request, "vetoffice/office.html", context)

def logout_request(request):
  logout(request)
  return redirect("home")

def login_request(request):
  return redirect("office")

class OwnerList(LoginRequiredMixin, ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"

class PatientList(LoginRequiredMixin, ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

class AppointmentList(LoginRequiredMixin, ListView):
  model = Appointment
  template_name = "vetoffice/appointment_list.html"

class OwnerCreate(LoginRequiredMixin, CreateView):
  model = Owner
  form_class = OwnerCreateForm
  success_url = "/owner/list"
  template_name = "vetoffice/owner_create_form.html"
  
class PatientCreate(LoginRequiredMixin, CreateView):
  model = Patient
  form_class = PatientCreateForm
  success_url = "/patient/list"
  template_name = "vetoffice/patient_create_form.html"
  
class AppointmentCreate(LoginRequiredMixin, CreateView):
  model = Appointment
  form_class = AppointmentCreateForm
  success_url = "/appointment/list"
  template_name = "vetoffice/appointment_create_form.html"

class OwnerUpdate(LoginRequiredMixin, UpdateView):
  model = Owner
  form_class = OwnerUpdateForm
  success_url = "/owner/list"
  template_name = "vetoffice/owner_update_form.html"
  
class PatientUpdate(LoginRequiredMixin, UpdateView):
  model = Patient
  form_class = PatientUpdateForm
  success_url = "/patient/list"
  template_name = "vetoffice/patient_update_form.html"
  
class AppointmentUpdate(LoginRequiredMixin, UpdateView):
  model = Appointment
  form_class = AppointmentUpdateForm
  success_url = "/appointment/list"
  template_name = "vetoffice/appointment_update_form.html"

class OwnerDelete(LoginRequiredMixin, DeleteView):
  model = Owner
  form_class = OwnerDeleteForm
  success_url = "/owner/list"
  template_name = "vetoffice/owner_delete_form.html"

class PatientDelete(LoginRequiredMixin, DeleteView):
  model = Patient
  form_class = PatientDeleteForm
  success_url = "/patient/list"
  template_name = "vetoffice/patient_delete_form.html"

class AppointmentDelete(LoginRequiredMixin, DeleteView):
  model = Appointment
  form_class = AppointmentDeleteForm
  success_url = "/appointment/list"
  template_name = "vetoffice/appointment_delete_form.html"