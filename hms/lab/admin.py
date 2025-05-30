from django.contrib import admin
from .models import LabTest, TestResult

class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_type', 'test_date', 'status', 'doctor')
    list_filter = ('test_type', 'status', 'test_date')
    search_fields = ('patient__username', 'notes')
    date_hierarchy = 'test_date'
    ordering = ('-test_date',)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ('test', 'technician', 'created_at', 'verified', 'verified_by')
    list_filter = ('verified', 'created_at')
    search_fields = ('test__patient__username', 'conclusion')
    readonly_fields = ('created_at', 'verified_at')
    date_hierarchy = 'created_at'

admin.site.register(LabTest, LabTestAdmin)
admin.site.register(TestResult, TestResultAdmin)