from django import forms
from .models import Bill


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = [
            'consultation_charge',
            'medicine_charge',
            'bed_charge',
            'lab_charge',
            'other_charge',
        ]
        widgets = {

            'consultation_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Consultation charge'
                }
            ),
            'medicine_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Medicine charge'
                }
            ),
            'bed_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Bed charge'
                }
            ),
            'lab_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Lab charge'
                }
            ),
            'other_charge': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Other charges'
                }
            ),
        }