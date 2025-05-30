from django import forms
from .models import LabTest
from users.models import User

TEST_TYPE_CHOICES = (
    ('BLOOD', 'Blood Test'),
    ('URINE', 'Urine Analysis'),
    ('XRAY', 'X-Ray'),
    ('MRI', 'MRI Scan'),
    ('CT', 'CT Scan'),
    ('ULTRASOUND', 'Ultrasound'),
)

class LabTestForm(forms.ModelForm):
    test_type = forms.ChoiceField(choices=TEST_TYPE_CHOICES)
    
    class Meta:
        model = LabTest
        fields = ['test_type', 'patient', 'doctor', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit patient choices to patients only
        self.fields['patient'].queryset = User.objects.filter(role='PATIENT')
        # Limit doctor choices to doctors only
        self.fields['doctor'].queryset = User.objects.filter(role='DOCTOR')