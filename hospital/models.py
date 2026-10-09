from django.db import models

# Create your models here.
class Hospital(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    City = models.CharField(max_length=100)
    Phone_no = models.CharField(max_length=15,unique=True)
    Email = models.EmailField()
    Emerg_Available = models.BooleanField(default=True)
    Total_Beds = models.PositiveIntegerField(default=0)
    Available_beds = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='hospitals/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

#it will be show department
class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='department/',blank=True,null=True)
    description = models.TextField(blank=True)
    hospital = models.ForeignKey(Hospital,related_name='department',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hospital.Name} - {self.name}"


#beds status 
BED_STATUS = [
        ('AVAILABLE', 'Available'),
        ('OCCUPIED', 'Occupied'),
        ('MAINTENANCE', 'Maintenance'),
    ]
class Bed(models.Model):
    Bed_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='beds/',blank=True,null=True)
    Status = models.CharField(max_length=20,choices=BED_STATUS,default='AVAILABLE')
    deparment = models.ForeignKey(Department,related_name='beds',on_delete=models.SET_NULL,null=True,blank=True)
    hospital = models.ForeignKey(Hospital,related_name='bed',on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.Bed_number
