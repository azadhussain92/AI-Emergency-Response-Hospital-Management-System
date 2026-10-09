from django.db import models
from django.contrib.auth.models import User
from hospital.models import Hospital,Department

# Create your models here.

class DoctorProfile(models.Model):
    user = models.OneToOneField(User,related_name='doctor_profile',on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,related_name='doctors',on_delete=models.CASCADE)
    department = models.ForeignKey(Department,related_name='doctors',on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to='doctors/',blank=True,null=True)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience_year = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

#treatment record
class TreatmentRecord(models.Model):
    doctor = models.ForeignKey(DoctorProfile,related_name='treatments',on_delete=models.CASCADE)
    patient = models.ForeignKey('patients.PatientProfile',related_name='treatments',on_delete=models.CASCADE)
    emergency = models.ForeignKey('emergency.EmergencyRequest',related_name='treatment',on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=200)
    treatment = models.TextField()
    medicines = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.patient_name} - {self.doctor.user.username}"