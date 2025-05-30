from django.contrib import admin
from .models import HospitalInfo

@admin.register(HospitalInfo)
class HospitalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'established_date')
    search_fields = ('name', 'email')
    ordering = ('-established_date',)