from django.urls import path
from hospital import views

urlpatterns = [
    path('',views.hospital_list,name='hospital_list'),
    path('add/',views.add_hospital,name='hospital_form'),
    path('department/',views.add_department,name='add_department'),
    path('bed/',views.add_bed,name='add_bed'),
    path('<int:id>/',views.hospital_details,name='hospital_detail'),
    # path('department/<int:id>/update/', views.update_department, name='update_department'),
    # path('bed/<int:id>/update/', views.update_bed, name='update_bed'),
    path('<int:id>update/',views.update_hospital,name='update'),
    path('<int:id>/delete/',views.delete_hospital,name='delete'),
    path(
    'department/<int:id>/delete/',
    views.delete_department,
    name='delete_department'
),

]