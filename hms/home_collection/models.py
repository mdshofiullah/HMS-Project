from django.db import models
from users.models import User
from lab.models import LabTest

COLLECTION_STATUS_CHOICES = (
    ('requested', 'Requested'),
    ('scheduled', 'Scheduled'),
    ('in_transit', 'In Transit'),
    ('collected', 'Collected'),
    ('delivered', 'Delivered to Lab'),
    ('cancelled', 'Cancelled'),
)

PAYMENT_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('partial', 'Partially Paid'),
    ('paid', 'Fully Paid'),
)

class CollectionRequest(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_tests = models.ManyToManyField(LabTest)
    collection_address = models.TextField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    special_instructions = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=COLLECTION_STATUS_CHOICES, default='requested')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    collector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Collection for {self.patient} on {self.preferred_date}"

class CollectionPayment(models.Model):
    collection = models.ForeignKey(CollectionRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=(
        ('cash', 'Cash'), 
        ('online', 'Online Payment'),
        ('card', 'Credit/Debit Card')
    ))
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ₹{self.amount} for {self.collection}"