from django import forms
from .models import Appointment, PatientRecord
from users.models import User

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time', 'purpose', 'status']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit patient choices to patients only
        self.fields['patient'].queryset = User.objects.filter(role='PATIENT')
        # Limit doctor choices to doctors only
        self.fields['doctor'].queryset = User.objects.filter(role='DOCTOR')

class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ['medical_history', 'allergies', 'medications']
        widgets = {
            'medical_history': forms.Textarea(attrs={'rows': 4}),
            'allergies': forms.Textarea(attrs={'rows': 2}),
            'medications': forms.Textarea(attrs={'rows': 3}),
        }