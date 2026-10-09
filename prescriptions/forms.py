from django.forms import inlineformset_factory
from django import forms
from prescriptions.models import Prescription,PrescriptionMedicine


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = [
            'diagnosis',
            'notes'
        ]
        widgets = {
            'diagnosis': forms.TextInput(attrs={'class':"form-control",'placeholder':'enter diagnosis'}),
            'notes': forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Additional Instruction'}),
        }

class PrescriptionMedicinForm(forms.ModelForm):
    class Meta:
        model = PrescriptionMedicine
        fields =[
            'medicin_name',
            'dosage',
            'duration',
            'instructions'
        ]
        widgets = {
            'medicin_name':forms.TextInput(attrs={'class':'form-control','placeholder':'medical name'}),
            'dosage':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 500mg'}),
            'duration': forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 5 days'}),
            'instructions': forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. After Food'})
        }

MedicineFormSet = inlineformset_factory(
    Prescription,
    PrescriptionMedicine,
    form=PrescriptionMedicinForm,
    extra=1,
    can_delete=True
)