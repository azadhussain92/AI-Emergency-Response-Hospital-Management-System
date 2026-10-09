from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('COMPLETED','Completed'),
        ('CANCELLED', 'Cancelled')
    ]

#appointment section
class Appointment(models.Model):
    patient = models.ForeignKey('patients.PatientProfile',related_name='appointments',on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.DoctorProfile',related_name='appointment',on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor}"