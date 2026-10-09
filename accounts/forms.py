from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile,ROLE_CHOISE, GENDER

#creat a form here 

class RegesterForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    # middle_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=100,required=False)
    # email = forms.EmailField()
    phone = forms.CharField(max_length=17)
    # emergency_contact = forms.CharField(max_length=17)
    role = forms.ChoiceField(choices=ROLE_CHOISE)
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

#admin form
class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['UserName', 'Phone', 'image']

        widgets = {
            'UserName': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username=username).exists():
        raise forms.ValidationError("user name already exist..")
    return username


def clean_email(self):
    email =self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("email is already exist")
    return email

def clean(self):
    clean_data = super().clean()
    password = clean_data.get('password')
    conform_password = clean_data.get('conform_password')
    if password and conform_password:
        if password != conform_password:
            raise forms.ValidationError("passwodr do not match")
    return clean_data

