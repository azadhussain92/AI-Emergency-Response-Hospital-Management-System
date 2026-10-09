from django import forms
from hospital.models import Hospital,Department,Bed


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = [
            'image',
            'Name',
            'Address',
            'City',
            'Phone_no',
            'Email',
            'Emerg_Available',
            'Total_Beds',
            'Available_beds'
        ]

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'image',
            'name',
            'hospital',
            'description'
        ]

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = [
            'image',
            'hospital',
            'Bed_number',
            'Status',
            'deparment'
        ]