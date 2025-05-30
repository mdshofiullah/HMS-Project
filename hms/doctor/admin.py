from django.contrib import admin
from .models import MedicalReport, DoctorSchedule

class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at', 'updated_at')
    list_filter = ('doctor', 'created_at')
    search_fields = ('patient__username', 'diagnosis')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time', 'is_available')
    list_filter = ('doctor', 'day_of_week', 'is_available')
    search_fields = ('doctor__username',)
    ordering = ('doctor', 'day_of_week')

admin.site.register(MedicalReport, MedicalReportAdmin)
admin.site.register(DoctorSchedule, DoctorScheduleAdmin)