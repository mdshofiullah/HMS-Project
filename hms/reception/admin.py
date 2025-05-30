from django.contrib import admin
from .models import Appointment, PatientRecord

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_time', 'status', 'created_at')
    list_filter = ('status', 'date_time', 'doctor')
    search_fields = ('patient__username', 'doctor__username', 'purpose')
    date_hierarchy = 'date_time'
    ordering = ('-date_time',)

class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'last_updated')
    search_fields = ('patient__username',)
    readonly_fields = ('last_updated',)

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PatientRecord, PatientRecordAdmin)