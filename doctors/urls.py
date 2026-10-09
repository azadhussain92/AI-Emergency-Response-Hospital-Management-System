from django.urls import path
from . import views

urlpatterns = [
    path('profile/create/',views.doctor_profile_create,name='doctor_profile_create'),
    path( 'dashboard/',views.doctor_dashboard,name='doctor_dashboard'),
    path('profile/edit/', views.doctor_profile_edit, name='doctor_profile_edit'),
    path('list/',views.doctor_list,name='doctor_list'),
    path('my-patients/',views.my_patients,name='my_patients'),
    path('treatment/<int:id>/',views.add_treatment,name='add_treatment')

]