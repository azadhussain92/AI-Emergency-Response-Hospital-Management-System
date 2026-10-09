from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from emergency.serializers import EmergencyRequestSerializer
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from emergency.models import EmergencyRequest
from emergency.forms import EmergencyRequestForm,DischargeForm
from patients.models import PatientProfile
from doctors.models import DoctorProfile
from django.db.models import Count
from emergency.models import RiskPrediction
from emergency.ml_prediction import predict_risk

# Create your views here.
#craete here to emergency request
@login_required
def emergency_create(request):

    if request.user.profile.Role != 'PATIENT':
        return redirect('dashboard')
    patient = get_object_or_404(PatientProfile,user=request.user)

    if request.method == 'POST':
        form = EmergencyRequestForm(request.POST)
        if form.is_valid():

            emergency = form.save(commit=False)
            emergency.patient = patient
            # Available doctor find karo
            doctor = DoctorProfile.objects.filter(is_available=True).annotate(emergency_count=Count('emergency_requests')).order_by('emergency_count').first()

            if doctor:
                emergency.doctor = doctor
                emergency.hospital = doctor.hospital
                emergency.status = 'ASSIGNED'
            else:
                emergency.status = 'PENDING'

            # emergency saved
            emergency.save()
            # Blood Pressure
            try:
                bp = emergency.blood_pressure
                systolic,diastolic = bp.split('/')
                systolic = float(systolic)
                diastolic = float(diastolic)
            except:
                systolic = 120
                diastolic = 80

            #Ml prediction
            risk_level, probability = predict_risk(
                oxygen_level=float(emergency.oxygen_level),
                heart_rate=float(emergency.heart_rate),
                temperature=float(emergency.temperature),
                systolic_bp=systolic,
                diastolic_bp=diastolic,
                emergency_type=emergency.emergency_type
            )

            # Save Risk Prediction
            RiskPrediction.objects.create(
                emergency_request=emergency,
                risk_level=risk_level,
                probability=round(probability * 100, 2),
                model_name='Random Forest'
            )

            return redirect( 'emergency_detail',id=emergency.id)
    else:
        form = EmergencyRequestForm()
    return render(request,'emergency/emergency_form.html',{'form': form})

@login_required
def emergency_list(request):
    role = request.user.profile.Role
    if role == 'PATIENT':
        patient = get_object_or_404(PatientProfile,user=request.user)

        emergencies = EmergencyRequest.objects.filter(patient=patient).order_by('-created_at')
    elif role == 'DOCTOR':
        doctor = get_object_or_404(DoctorProfile,user=request.user)
        emergencies = EmergencyRequest.objects.filter(doctor=doctor).order_by('-created_at')
    elif role == 'HOSPITAL_ADMIN':
        emergencies = EmergencyRequest.objects.all().order_by('-created_at')
    else:
        return redirect('dashboard')

    return render(request,'emergency/emergency_list.html',{'emergencies':emergencies})

#enmergency details
@login_required
def emergency_detail(request,id):
    emergency = get_object_or_404(EmergencyRequest,id=id)
    return render(request,'emergency/emergency_detail.html',{'emergency':emergency})

#risk prediction
@login_required
def risk_prediction_list(request):

    role = request.user.profile.Role
    if role == 'PATIENT':
        prediction = RiskPrediction.objects.filter(emergency_request__patient__user=request.user)

    elif role == 'DOCTOR':
        prediction = RiskPrediction.objects.filter(emergency_request__doctor__user=request.user)

    elif role == 'HOSPITAL_ADMIN':
        prediction = RiskPrediction.objects.all()

    else:
        return redirect('dashboard')
    
    prediction = prediction.order_by('-created_at')
    return render(request,'emergency/risk_prediction.html',{'prediction': prediction})

# rest_framework
class EmergencyRequestListCreateAPI(generics.ListCreateAPIView):
    serializer_class = EmergencyRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if self.request.user.profile.Role == 'PATIENT':
            patient = PatientProfile.objects.get(user=user)
            return EmergencyRequest.objects.filter(patient=patient).order_by('-created_at')
        return EmergencyRequest.objects.all().order_by('-created_at')

    def perform_create(self,serializer):
        patient = PatientProfile.objects.get(user=self.request.user)
        serializer.save(patient=patient)


class EmergencyRequestDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmergencyRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.profile.Role == 'PATIENT':
            patient = PatientProfile.objects.get(user=self.request.user)
            return EmergencyRequest.objects.filter(patient=patient)
        return EmergencyRequest.objects.all()


#patient discharge 
@login_required
def discharge_patient(request,id):
    if request.user.profile.Role != 'DOCTOR':
        return redirect('dashboard')
    emergency = get_object_or_404(EmergencyRequest,id=id,doctor__user=request.user)
    if request.method == 'POST':
        form = DischargeForm(request.POST,instance=emergency)

        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.is_discharged = True
            emergency.discharge_date = timezone.now()
            emergency.status = 'DISCHARGED'
            emergency.save()
            return redirect('emergency_detail',id=emergency.id)
    else:
        form = DischargeForm(instance=emergency)
    return render(request,'emergency/discharge.html',{'form':form,'emergency':emergency})