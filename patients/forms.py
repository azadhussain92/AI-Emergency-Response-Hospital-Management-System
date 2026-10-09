from django import forms
from patients.models import PatientProfile


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
            'image',
            'patient_name',
            'date_of_birth',
            'gender',
            'phone_num',
            'blood_group',
            'address',
            'medical_conditions',
            'emergency_contact',
        ]

        widgets = {
            'phone_num': forms.TextInput(attrs={'type': 'tel','placeholder': 'Enter phone number'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),'address': forms.Textarea(attrs={'rows': 3}),
            'medical_conditions': forms.TextInput(attrs={'placeholder': 'Enter medical conditions'}),
            }