from django.db import models
from users.models import User
from reception.models import Appointment

TEST_TYPE_CHOICES = (
    ('BLOOD', 'Blood Test'),
    ('URINE', 'Urine Analysis'),
    ('XRAY', 'X-Ray'),
    ('MRI', 'MRI Scan'),
    ('CT', 'CT Scan'),
    ('ULTRASOUND', 'Ultrasound'),
)

TEST_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)

class LabTest(models.Model):
    test_type = models.CharField(max_length=50, choices=TEST_TYPE_CHOICES)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ordered_tests')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    ordered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ordered_by')
    test_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=TEST_STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    result = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_test_type_display()} for {self.patient}"

class TestResult(models.Model):
    test = models.OneToOneField(LabTest, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    findings = models.TextField()
    conclusion = models.TextField()
    attachment = models.FileField(upload_to='lab_results/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='verified_results')
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Result for {self.test}"