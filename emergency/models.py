from django.db import models
from patients.models import PatientProfile
from hospital.models import Hospital
from doctors.models import DoctorProfile


# Create your models here.
STATUS_CHOICES = [
    ('PROCESSING', 'Processing'),
    ('PENDING', 'Pending'),
    ('ASSIGNED', 'Assigned'),
    ('DISCHARGED', 'Discharged'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
]

EMERGENCY_TYPE = [
    ('ACCIDENT', 'Accident'),
    ('CHEST_PAIN', 'Chest Pain'),
    ('BREATHING', 'Breathing Problem'),
    ('FEVER', 'Fever'),
    ('INJURY', 'Injury'),
    ('OTHER', 'Other'),
]

class EmergencyRequest(models.Model):
    patient = models.ForeignKey(PatientProfile,related_name='emergency_request',on_delete=models.CASCADE)
    emergency_type = models.CharField(max_length=30,choices=EMERGENCY_TYPE)
    symptoms = models.TextField()
    heart_rate = models.PositiveIntegerField(null=True,blank=True)
    oxygen_level = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    temperature = models.DecimalField(max_digits=4,decimal_places=1,null=True,blank=True)
    blood_pressure = models.CharField(max_length=20,blank=True)
    location = models.CharField(max_length=100,blank=True)
    hospital = models.ForeignKey(Hospital,related_name='emergency_requests',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    discharge_date = models.DateTimeField(null=True,blank=True)
    discharge_notes = models.TextField(blank=True)
    is_discharged = models.BooleanField(default=False)
    doctor = models.ForeignKey(DoctorProfile,related_name='emergency_requests',on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.patient)

# RiskPrediction

RISK_LEVELS = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High'),
]

class RiskPrediction(models.Model):
    emergency_request = models.OneToOneField(EmergencyRequest,related_name='risk_prediction',on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=20,choices=RISK_LEVELS)
    probability = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    model_name = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emergency_request.id} - {self.risk_level}"


