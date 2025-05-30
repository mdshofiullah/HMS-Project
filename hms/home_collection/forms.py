from django import forms
from .models import CollectionRequest
from users.models import User
from lab.models import LabTest

class CollectionRequestForm(forms.ModelForm):
    class Meta:
        model = CollectionRequest
        fields = ['patient', 'requested_tests', 'collection_address', 
                  'preferred_date', 'preferred_time', 'special_instructions']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
            'special_instructions': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit patient choices to patients only
        self.fields['patient'].queryset = User.objects.filter(role='PATIENT')
        # Limit test choices to available lab tests
        self.fields['requested_tests'].queryset = LabTest.objects.all()