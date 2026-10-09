from django import forms
from appointments.models import Appointment


#appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctor',
            'appointment_date',
            'appointment_time',
            'reason'
        ]

        widgets = {
            'appointment_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'appointment_time':forms.TimeInput(attrs={'type':'time','class': 'form-control'}),
            'reason':forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Enter reson for appointment'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }