from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assigneddoctorid=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctorid=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientid=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorid=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    
    class Meta:
        model = models.Appointment
        fields = ['description', 'appointmentdate', 'appointmenttime', 'status']
        widgets = {
            'appointmentdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointmenttime': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            # 'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
           
            # 'status': forms.HiddenInput()  # status can be hidden if it's not meant to be changed by the user
        }


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ['room_number', 'room_type', 'capacity','status','patient']



from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'dept_id', 'dept_contact', 'head']
        widgets = {
            'dept_name': forms.Select(choices=Department.departments, attrs={'class': 'form-control'}),
            'dept_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department ID'}),
            'dept_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Contact'}),
            'head': forms.Select(attrs={'class': 'form-control'}),
        }
