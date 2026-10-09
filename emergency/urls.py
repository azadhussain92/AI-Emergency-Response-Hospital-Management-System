from django.urls import path
from emergency import views

urlpatterns = [
    path('', views.emergency_list, name='emergency_list'),
    path('create/', views.emergency_create, name='emergency_create'),
    path('risk-prediction/', views.risk_prediction_list, name='risk_prediction_list'),
    path('<int:id>/', views.emergency_detail, name='emergency_detail'),
    path('<int:id>/discharge/',views.discharge_patient,name='discharge_patient'),
    #rest_framework api
    path('api/',views.EmergencyRequestListCreateAPI.as_view(),name='emergency_api'),
    path('api/<int:pk>/',views.EmergencyRequestDetailsAPI.as_view(), name='emergency_api_details')
]