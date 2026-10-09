from django import forms
from emergency.models import EmergencyRequest


class EmergencyRequestForm(forms.ModelForm):
    class Meta:
        model = EmergencyRequest
        fields = [
            'emergency_type',
            'symptoms',
            'heart_rate',
            'oxygen_level',
            'temperature',
            'blood_pressure',
            'location'
        ]
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 4}),
            'blood_pressure': forms.Textarea(attrs={'placeholder':'Example:120/80'}),
            'location': forms.TextInput(attrs={'placeholder':'Enter Your Current Location'}),
        }


#descharge form
class DischargeForm(forms.ModelForm):
    class Meta:
        model = EmergencyRequest
        fields = ['discharge_notes']

        widgets = {
            'discharge_notes': forms.Textarea(attrs={
                'class':'form-control',
                'row': 4,
                'placeholder': 'Enter Discharge Notes..'
            }),
        }