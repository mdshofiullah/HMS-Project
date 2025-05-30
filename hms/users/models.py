from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'System Admin'),
        ('RECEPTION', 'Receptionist'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('LAB', 'Lab Technician'),
        ('FINANCE', 'Finance Staff'),
        ('HOME_COLLECT', 'Home Collection Staff'),
        ('PATIENT', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ADMIN')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    qualifications = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"