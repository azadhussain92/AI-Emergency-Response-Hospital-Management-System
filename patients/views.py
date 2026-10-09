from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from patients.forms import PatientProfileForm
from patients.models import PatientProfile
from doctors.models import DoctorProfile

# Create your views here.

@login_required
def patient_profile_create(request):

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, request.FILES)

        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('dashboard')
    else:
        form = PatientProfileForm()
    return render(request,'patients/patient_profile.html',{'form': form})

@login_required
def patient_profile_edit(request):
    patient = request.user.patient_profile

    if request.method == 'POST':
        form = PatientProfileForm(request.POST,request.FILES,instance=patient)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientProfileForm(instance=patient)

    return render(request,'patients/patient_profile_edit.html',{'form': form,'patient': patient})


@login_required
def patient_profile_view(request):
    patient = get_object_or_404(PatientProfile,user=request.user)
    return render(request,'patients/patient_profile_view.html',
        {'patient': patient})


@login_required
def patient_list(request):
    patients = PatientProfile.objects.all()
    return render(request,'patients/patient_list.html',{'patients':patients})
