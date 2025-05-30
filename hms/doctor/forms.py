from django import forms
from .models import MedicalReport, DoctorSchedule
from reception.models import Appointment
from users.models import User

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['patient', 'appointment', 'diagnosis', 'findings', 'prescription']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter diagnosis...'}),
            'findings': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter clinical findings...'}),
            'prescription': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Enter prescription details...'}),
        }
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit patient choices to the doctor's patients
        self.fields['patient'].queryset = User.objects.filter(
            role='PATIENT',
            patient_appointments__doctor=user
        ).distinct()
        # Limit appointment choices to the doctor's appointments
        self.fields['appointment'].queryset = Appointment.objects.filter(
            doctor=user
        )

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = ['day_of_week', 'start_time', 'end_time', 'is_available']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }