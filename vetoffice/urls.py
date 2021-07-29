from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("office/", views.office, name="office"),
  path("accounts/", include("django.contrib.auth.urls")),
  path("signup/", views.SignUp.as_view(), name="signup"),
  path("logout/", views.logout_request, name="logout"),
  path("login/", views.login_request, name="login"),
  path("owner/list", views.OwnerList.as_view(), name="ownerlist"),
  path("patient/list", views.PatientList.as_view(), name="patientlist"),
  path("appointment/list", views.AppointmentList.as_view(), name="appointmentlist"),
  path("owner/create", views.OwnerCreate.as_view(), name="ownercreate"),
  path("patient/create", views.PatientCreate.as_view(), name="patientcreate"),
  path("appointment/create", views.AppointmentCreate.as_view(), name="appointmentcreate"),
  path("owner/update/<pk>", views.OwnerUpdate.as_view(), name="ownerupdate"),
  path("patient/update/<pk>", views.PatientUpdate.as_view(), name="patientupdate"),
  path("appointment/update/<pk>", views.AppointmentUpdate.as_view(), name="appointmentupdate"),
  path("owner/delete/<pk>", views.OwnerDelete.as_view(), name="ownerdelete"),
  path("patient/delete/<pk>", views.PatientDelete.as_view(), name="patientdelete"),
  path("appointment/delete/<pk>", views.AppointmentDelete.as_view(), name="appointmentdelete"),
]