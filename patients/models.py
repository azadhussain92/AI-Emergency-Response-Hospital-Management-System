from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES= [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other'),
]

BLOOD_GROUP = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]
class PatientProfile(models.Model):
    user = models.OneToOneField(User,related_name='patient_profile',on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES,blank=True)
    phone_num = models.PositiveBigIntegerField(max_length=17,unique=True)
    image = models.ImageField(upload_to='patients/',blank=True,null=True)
    blood_group = models.CharField(max_length=15,choices=BLOOD_GROUP,blank=True)
    address = models.TextField(blank=True)
    medical_conditions = models.CharField(max_length=100, blank=True)
    emergency_contact = models.PositiveBigIntegerField(max_length=17,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username