from django.db import models

# Create your models here.
class HospitalInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    established_date = models.DateField()

    def __str__(self):
        return self.name