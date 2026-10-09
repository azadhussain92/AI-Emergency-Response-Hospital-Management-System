from django.urls import path
from . import views


urlpatterns = [
    path('',views.bill_list,name='bill_list'),
    path('create/<int:id>/',views.create_bill,name='create_bill'),
    path('appointment/<int:id>/create/',views.create_appointment_bill,name='create_appointment_bill'),
    path('<int:id>/',views.bill_detail,name='bill_detail'),
    path('<int:id>/paid/',views.mark_bill_paid,name='mark_bill_paid'),
]