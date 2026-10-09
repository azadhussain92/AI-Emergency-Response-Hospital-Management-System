from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from accounts.forms import AdminProfileForm
from hospital.models import Hospital
from doctors.models import DoctorProfile
from patients.models import PatientProfile
from emergency.models import EmergencyRequest
from accounts.forms import RegesterForm
from accounts.models import UserProfile
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegesterForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            # email = data['email']
            password = data['password']
            Phone = data['phone']
            # emergency_contact = data['emergency_contact']
            Role = data['role']

            # Username check
            if User.objects.filter(username=username).exists():
                form.add_error('username','This username is already registered.')
            # Phone check
            elif UserProfile.objects.filter(Phone=Phone).exists():
                form.add_error('phone','This phone number is already registered.')

            else:
                # Create User
                user = User.objects.create_user(username=username,password=password)

                # Create UserProfile
                UserProfile.objects.create(user=user,UserName=username,Role=Role,Phone=Phone,Gender='OTHER' )
                messages.success(request,'Registration successful! Please login.')
                return redirect('login')
    else:
        form = RegesterForm()
    return render(request,'account/register.html',{'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            #doctor
            if user.profile.Role == 'DOCTOR':
                if not hasattr(user, 'doctor_profile'):
                    return redirect('doctor_profile_create')
                
             # PATIENT
            if user.profile.Role == 'PATIENT':
                if not hasattr(user, 'patient_profile'):
                    return redirect('patient_profile_create')  
                 
            return redirect('dashboard')
        messages.error(request,"invalid user and password")
    return render(request,'account/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"you have been logout out")
    return redirect('login')


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = request.user.profile
    doctor_profile_exists = False
    doctor = None
    patient = None

    #doctor profile
    if profile.Role == 'DOCTOR':
        doctor_profile_exists = hasattr(request.user, 'doctor_profile')
        if doctor_profile_exists:
            doctor = request.user.doctor_profile

    #patient profile
    if profile.Role == 'PATIENT':
        patient = getattr(request.user, 'patient_profile', None)
    hospital_count = 0
    doctor_count = 0
    patient_count = 0
    hospital_count = 0
    online_doctor_count = 0
    #admin profile 
    if profile.Role == 'HOSPITAL_ADMIN':
         hospital_count = Hospital.objects.count()
         doctor_count = DoctorProfile.objects.count()
         patient_count = PatientProfile.objects.count()
         five_minutes_ago = timezone.now() - timedelta(minutes=5)
         online_doctor_count = DoctorProfile.objects.filter(user__profile__Last_seen__gte=five_minutes_ago).count()

    return render(request,'account/dashboard.html',
                  {'profile': profile,
                   'doctor_profile_exists': doctor_profile_exists,
                   'hospital_count': hospital_count,
                   'doctor': doctor,'patient': patient,
                   'doctor_count':doctor_count,
                   'patient_count':patient_count,
                   'online_doctor_count':online_doctor_count,
                   'doctor':doctor,
                   'patient':patient
                   })

# @login_required
# def admin_profile(request):
#     profile = request.user.profile

#     if profile.Role != 'HOSPITAL_ADMIN':
#         return redirect('dashboard')

#     if request.method == 'POST':
#         form = AdminProfileForm(request.POST,request.FILES,instance=profile)
#         if form.is_valid():form.save()
#         return redirect('admin_profile')
#     else:
#         form = AdminProfileForm(instance=profile)

#     hospital_count = Hospital.objects.count()
#     doctor_count = DoctorProfile.objects.count()
#     patient_count = PatientProfile.objects.count()
#     emergency_count = EmergencyRequest.objects.count()

#     return render(request,'account/admin_profile.html',
#                   {
#                     'profile':profile,
#                     'hospital_count': hospital_count,
#                     'doctor_count': doctor_count,
#                     'patient_count': patient_count,
#                     'emergency_count': emergency_count,
#                     })

@login_required
def admin_profile(request):

    profile = request.user.profile

    if profile.Role != 'HOSPITAL_ADMIN':
        return redirect('dashboard')

    if request.method == 'POST':

        form = AdminProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('admin_profile')

        print(form.errors)

    else:
        form = AdminProfileForm(instance=profile)

    hospital_count = Hospital.objects.count()
    doctor_count = DoctorProfile.objects.count()
    patient_count = PatientProfile.objects.count()
    emergency_count = EmergencyRequest.objects.count()

    return render(
        request,
        'account/admin_profile.html',
        {
            'profile': profile,
            'form': form,
            'hospital_count': hospital_count,
            'doctor_count': doctor_count,
            'patient_count': patient_count,
            'emergency_count': emergency_count,
        }
    )