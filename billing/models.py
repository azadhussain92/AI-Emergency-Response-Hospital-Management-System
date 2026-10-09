from django.db import models

# Create your models here.

STATUS_CHOICES =[
    ('PENDING', 'Pending'),
    ('PAID', 'Paid'),
    ('CANCELLED', 'Cancelled'),
]

class Bill(models.Model):
    patient = models.ForeignKey('patients.PatientProfile',related_name='bills',on_delete=models.CASCADE)
    emergency = models.ForeignKey('emergency.EmergencyRequest',related_name='bills',on_delete=models.SET_NULL,null=True,blank=True)
    consultation_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    medicine_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    bed_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    lab_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    other_charge = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey('appointments.Appointment',related_name='bills',on_delete=models.CASCADE,null=True,blank=True)


    def calculate_total(self):
        self.total_amount = (
            self.consultation_charge +
            self.medicine_charge +
            self.bed_charge +
            self.lab_charge +
            self.other_charge
        )

    def save(self, *args, **kwargs):
        self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.id} - {self.patient.patient_name}"
