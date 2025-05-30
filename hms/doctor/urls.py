from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('reports/create/', views.create_report, name='create_report'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('schedule/', views.schedule_management, name='schedule_management'),
]