from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from appointments.models import Appointment
from appointments.forms import AppointmentForm
from patients.models import PatientProfile
from doctors.models import DoctorProfile

# Create your views here.

@login_required
def create_appointment(request):

    if request.user.profile.Role != 'PATIENT':
        return redirect('dashboard')
    patient = get_object_or_404(PatientProfile,user=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.status = 'PENDING'
            appointment.save()
            messages.success(request,'Appointment booked successfully! 🎉')
            return redirect('appointment_list')

        print("FORM ERRORS:", form.errors)
    else:
        form = AppointmentForm()

    return render(request,'appointment/create_appointment.html',{'form': form})

# appointment list show
@login_required
def appointment_list(request):
    role = request.user.profile.Role

    if role == 'PATIENT':
        patient = get_object_or_404(PatientProfile,user=request.user)
        appointments = Appointment.objects.filter(patient=patient)

    elif role == 'DOCTOR':
        doctor = get_object_or_404(DoctorProfile,user=request.user)
        appointments = Appointment.objects.filter(doctor=doctor)
    elif role == 'HOSPITAL_ADMIN':
        appointments = Appointment.objects.all()
    else:
        return redirect('dashboard')

    appointments = appointments.order_by('-appointment_date','-appointment_time' )

    return render(request,'appointment/appointment_list.html',{ 'appointments': appointments})
@login_required
def update_appointment_status(request, id):

    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')
    doctor = get_object_or_404(DoctorProfile,user=request.user )
    appointment = get_object_or_404(Appointment,id=id,doctor=doctor)

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['CONFIRMED','CANCELLED','COMPLETED']:
            appointment.status = status
            appointment.save()
    return redirect('appointment_list')
