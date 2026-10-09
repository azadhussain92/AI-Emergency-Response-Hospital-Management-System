from django.urls import path
from accounts import views



urlpatterns = [
    path('', views.register, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admin-profile/', views.admin_profile, name='admin_profile'),
 
]