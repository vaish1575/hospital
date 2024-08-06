from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now


departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=True)  # Add a full_name field

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def save(self, *args, **kwargs):
        self.full_name = self.get_name
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)




from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=100)
    assigneddoctorid = models.PositiveIntegerField(null=True)
    admitdate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=True)
    
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"

    def save(self, *args, **kwargs):
        self.full_name = self.get_name
        super().save(*args, **kwargs)

# Signal to update full_name when User is updated
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def update_patient_full_name(sender, instance, **kwargs):
    try:
        patient = instance.patient
        patient.full_name = patient.get_name
        patient.save()
    except Patient.DoesNotExist:
        pass



class Appointment(models.Model):
    patientid=models.PositiveIntegerField(null=True)
    doctorid=models.PositiveIntegerField(null=True)
    patientname=models.CharField(max_length=40,null=True)
    doctorname=models.CharField(max_length=40,null=True)
    appointmentdate=models.DateField(default=date.today,null=True )
    appointmenttime=models.TimeField(default=now, null=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientid=models.PositiveIntegerField(null=True)
    patientname=models.CharField(max_length=40)
    assigneddoctorname=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitdate=models.DateField(null=False)
    releasedate=models.DateField(null=False)
    dayspent=models.PositiveIntegerField(null=False)

    roomcharge=models.PositiveIntegerField(null=False)
    medicinecost=models.PositiveIntegerField(null=False)
    doctorfee=models.PositiveIntegerField(null=False)
    othercharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)

class PatientReport(models.Model):
    patientid = models.PositiveIntegerField(null=True)
    patientname = models.CharField(max_length=40)
    assigneddoctorname = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    def copy_from_discharge_details(self, discharge_details):
        self.patientid = discharge_details.patientid
        self.patientname = discharge_details.patientname
        self.assigneddoctorname = discharge_details.assigneddoctorname
        self.address = discharge_details.address
        self.mobile = discharge_details.mobile
        self.symptoms = discharge_details.symptoms
        

from django.db import models

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
        ('ICU', 'ICU'),
        ('opd','opd'),
    ]
    
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    ]

    room_number = models.CharField(max_length=10, unique=True,primary_key=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True, blank=True)
   

    def __str__(self):
        return f"{self.room_number} - {self.room_type} ({self.status})"
    



from django.db import models
from .models import Doctor

class Department(models.Model):
    departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
    dept_id = models.CharField(max_length=20, primary_key=True)
    dept_name = models.CharField(max_length=100,choices=departments)
    dept_contact = models.CharField(max_length=20)
    head = models.ForeignKey('Doctor', on_delete=models.CASCADE,related_name='department_head',null=True)

    def __str__(self):
        return self.dept_name
