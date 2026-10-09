from django.urls import path
from patients import views


urlpatterns = [
    path('profile/create/',views.patient_profile_create,name='patient_profile_create'),
    path('profile/edit/',views.patient_profile_edit,name='patient_profile_edit'),
    path('profile/',views.patient_profile_view,name='patient_profile_view'),
    path('list/',views.patient_list,name='patient_list'),
]