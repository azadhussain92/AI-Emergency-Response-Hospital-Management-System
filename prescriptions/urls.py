from django.urls import path
from . import views

urlpatterns = [
    path('',views.prescription_list,name='prescription_list'),
    path('create/<int:id>',views.create_prescription,name='create_prescription'),
    path('<int:id>/',views.prescription_details,name='prescription_details')
]