from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from doctors.forms import DoctorProfileForm,TreatmentRecordForm
from doctors.models import DoctorProfile
from emergency.models import EmergencyRequest

@login_required
def doctor_profile_create(request):

    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')
    # return render(
    #     request,
    #     'doctors/doctor_dashboard.html')

    if hasattr(request.user, 'doctor_profile'):
        return redirect('doctor_dashboard')
    if request.method == 'POST':
        # form = DoctorProfileForm(request.POST)

        form = DoctorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('dashboard')
        
    else:
        form = DoctorProfileForm()
    return render(request,'doctors/doctor_profile.html',{'form': form})


# Doctor Dashboard
@login_required
def doctor_dashboard(request):
    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')
    doctor = request.user.doctor_profile
    return render(request,'doctors/doctor_dashboard.html',{'doctor': doctor})

#doctor profile edit
@login_required
def doctor_profile_edit(request):
    if request.user.profile.Role !='DOCTOR':
        return redirect('dashboard')
    
    doctor = request.user.doctor_profile
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST,request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            request.user.username = request.POST.get('username')
            request.user.save()
            return redirect(doctor_dashboard)
    else:
        form = DoctorProfileForm(instance=doctor)

    return render(request,'doctors/doctor_profile_edit.html',{'form': form, 'doctor': doctor})

#doctor list
@login_required
def doctor_list(request):
    doctors = DoctorProfile.objects.all()
    return render(request,'doctors/doctor_list.html',{'doctors':doctors})

#doctor check the patient in how mnay assigned
@login_required
def my_patients(request):
    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(DoctorProfile,user=request.user)
    emergencies = EmergencyRequest.objects.filter(doctor=doctor).select_related('patient').order_by('-created_at')
    return render(request,'doctors/my_patient.html',{'emergencies':emergencies})

#treatment view the 
def add_treatment(request,id):
    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(DoctorProfile,user=request.user)
    emergency = get_object_or_404(EmergencyRequest,id=id,doctor=doctor)

    if request.method == 'POST':
        form = TreatmentRecordForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.doctor = doctor
            treatment.patient =emergency.patient
            treatment.emergency = emergency
            treatment.save()
            emergency.status = 'PROCESSING'
            emergency.save()
            return redirect('my_patients')
    else:
        form = TreatmentRecordForm()
    return render(request,'doctors/add_treatment.html',{'from':form,'emergency':emergency})
    