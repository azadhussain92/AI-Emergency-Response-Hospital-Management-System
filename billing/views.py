from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from billing.models import Bill
from billing.forms import BillForm
from patients.models import PatientProfile
from appointments.models import Appointment
from emergency.models import EmergencyRequest

# Create your views here.
#here create the bill 
@login_required
def create_bill(request,id):
    if request.user.profile.Role != 'HOSPITAL_ADMIN':
        return redirect('dashboard')
    emergency = get_object_or_404(EmergencyRequest,id= id)
    patient = emergency.patient
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.patient = patient
            bill.emergency = emergency
            bill.status = 'PENDING'
            # Bill.save()
            bill.save()
            return redirect('bill_detail',id=bill.id)
    else:
        form = BillForm()
    return render(request,'billing/create_bill.html',{'form':form,'patient':patient,'emergency':emergency})

# here will show the bill list of admin and patient
@login_required
def bill_list(request):
    role = request.user.profile.Role

    if role == 'PATIENT':
        patient = get_object_or_404(PatientProfile, user=request.user)
        bills = Bill.objects.filter(patient=patient).order_by('-created_at')
        return render(request, 'billing/bill_list.html', {'bills': bills,'appointments': [],'emergencies': []})

    elif role == 'HOSPITAL_ADMIN':
        appointments = Appointment.objects.filter(status='COMPLETED').order_by('-appointment_date', '-appointment_time')
        emergencies = EmergencyRequest.objects.all().order_by('-id')
        bills = Bill.objects.all().order_by('-created_at')

        return render(request, 'billing/bill_list.html', {'bills': bills,'appointments': appointments,'emergencies': emergencies})

    return redirect('dashboard')

# here will show the details of bills
@login_required
def bill_detail(request, id):
    role = request.user.profile.Role

    if role == 'PATIENT':
        patient = get_object_or_404(PatientProfile,user=request.user)
        bill = get_object_or_404( Bill,id=id, patient=patient)
    elif role == 'HOSPITAL_ADMIN':
        bill = get_object_or_404(Bill, id=id)
    else:
        return redirect('dashboard')

    return render(request,'billing/bill_detail.html',{'bill': bill})

#show the bill paid on dashboard
@login_required
def mark_bill_paid(request,id):
    if request.user.profile.Role != 'HOSPITAL_ADMIN':
        return redirect('dashboard')

    bill = get_object_or_404(Bill,id=id)
    if request.method == 'POST':
        bill.status = 'PAID'
        bill.save()
        return redirect('bill_detail',id=bill.id)
    
#here should be create the appointment 
@login_required
def create_appointment_bill(request, id):
    if request.user.profile.Role != 'HOSPITAL_ADMIN':
        return redirect('dashboard')
    appointment = get_object_or_404(Appointment,id=id,status='COMPLETED')
    patient = appointment.patient
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.patient = patient
            bill.appointment = appointment
            bill.status = 'PENDING'
            bill.save()
            return redirect('bill_detail',id=bill.id)
    else:
        form = BillForm()
    return render( request,'billing/create_bill.html',{'form': form,'patient': patient,'appointment': appointment})