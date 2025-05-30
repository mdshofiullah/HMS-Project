from django.urls import path
from . import views

app_name = 'reception'

urlpatterns = [
    path('dashboard/', views.reception_dashboard, name='reception_dashboard'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/new/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('records/<int:pk>/', views.patient_record, name='patient_record'),
]