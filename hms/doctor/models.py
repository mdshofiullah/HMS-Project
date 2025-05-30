from django.db import models
from users.models import User
from reception.models import Appointment

class MedicalReport(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_reports')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField()
    findings = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report for {self.patient} by {self.doctor}"

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=(
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), 
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')
    ))
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor}'s Schedule ({self.get_day_of_week_display()})"