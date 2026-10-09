from django import forms
from .models import DoctorProfile
from doctors.models import TreatmentRecord

# doctor profile 
class DoctorProfileForm(forms.ModelForm):

    class Meta:
        model = DoctorProfile

        fields = [
            'image',
            'hospital',
            'department',
            'specialization',
            'qualification',
            'experience_year',
            'phone',
            'is_available'
        ]


# treatment records
class TreatmentRecordForm(forms.ModelForm):
    class Meta:
        model = TreatmentRecord
        fields = [
            'diagnosis',
            'treatment',
            'medicines',
            'notes'
        ]

        widgets = {
            'diagnosis': forms.TextInput(attrs={'class': 'form-control'}),
            'treatment': forms.Textarea(attrs={'class':'form-control','rows':4}),
            'medicines': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'notes': forms.Textarea(attrs={'class':'form-control','rows':3})
        }