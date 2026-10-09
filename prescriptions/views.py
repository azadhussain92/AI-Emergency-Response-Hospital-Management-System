from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm, MedicineFormSet
from prescriptions.models import Prescription,PrescriptionMedicine
from prescriptions.forms import PrescriptionForm,PrescriptionMedicinForm
from doctors.models import DoctorProfile 
from patients.models import PatientProfile
from emergency.models import EmergencyRequest

# Create your views here.
@login_required
def create_prescription(request, id):

    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')
    doctor = get_object_or_404( DoctorProfile, user=request.user)
    emergency = get_object_or_404(EmergencyRequest,id=id,doctor=doctor)

    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        if prescription_form.is_valid():
            prescription = prescription_form.save(commit=False)
            prescription.doctor = doctor
            prescription.patient = emergency.patient
            prescription.emergency = emergency
            prescription.save()

            medicine_formset = MedicineFormSet( request.POST, instance=prescription)

            if medicine_formset.is_valid():
                medicine_formset.save()
                return redirect('prescription_details',id=prescription.id)
    else:
        prescription_form = PrescriptionForm()
        medicine_formset = MedicineFormSet()
    return render(request,'prescription/create_prescription.html',{'prescription_form': prescription_form,'medicine_formset': medicine_formset,'emergency': emergency})

@login_required
def prescription_list(request):
    role = request.user.profile.Role
    if role == 'DOCTOR':
        prescriptions = Prescription.objects.filter(doctor__user=request.user)
    elif role == 'PATIENT':
        prescriptions = Prescription.objects.filter(patient__user=request.user)
    elif role == 'HOSPITAL_ADMIN':
        prescriptions = Prescription.objects.all()
    else:
        return redirect('dashboard')
    prescriptions = prescriptions.order_by('-created_at')
    return render(request,'prescription/prescription_list.html',{'prescriptions':prescriptions})


@login_required
def prescription_details(request,id):
    prescription = get_object_or_404(Prescription,id=id)
    return render(request,'prescription/prescription_detail.html',{'prescription':prescription})