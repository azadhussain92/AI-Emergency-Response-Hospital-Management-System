from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ROLE_CHOISE = [
    ('PATIENT','Patient'),
    ('DOCTOR','Doctor'),
    ('HOSPITAL_ADMIN','Hospital_Admin'),
]
GENDER = [
    ('MALE','Male'),
    ('FEMALE','Female'),
    ('OTHER','Other'),
]

class UserProfile(models.Model):
    UserName = models.CharField(max_length=50,blank=True)
    Role = models.CharField(max_length=50,choices=ROLE_CHOISE)
    Phone = models.CharField(max_length=17,unique=True)
    Gender = models.CharField(max_length=50,choices=GENDER)
    DOB = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='admins/',blank=True,null=True)
    Last_seen = models.DateTimeField(null=True, blank=True)  
    Created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.UserName} ({self.Role})"

