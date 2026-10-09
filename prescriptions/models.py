from django.db import models

# Create your models here.

class Prescription(models.Model):
    doctor = models.ForeignKey('doctors.DoctorProfile',related_name='prescriptions',on_delete=models.CASCADE)
    patient = models.ForeignKey('patients.PatientProfile',related_name='prescriptions',on_delete=models.CASCADE)
    emergency = models.ForeignKey('emergency.EmergencyRequest',related_name='prescriptions',on_delete=models.SET_NULL,null=True,blank=True)
    diagnosis = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.patient.patient_name} - prescription"

class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription,related_name='medicines',on_delete=models.CASCADE)
    medicin_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.CharField(max_length=300,blank=True)


    def __str__(self):
        return self.medicin_name
