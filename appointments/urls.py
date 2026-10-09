from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment_list,name='appointment_list'),
    path('create/',views.create_appointment,name='create_appointment'),
    path('<int:id>/status/',views.update_appointment_status,name='update_appointment_status')
]