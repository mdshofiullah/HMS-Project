from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.decorators import role_required
from django.utils import timezone
from .models import Appointment, PatientRecord
from .forms import AppointmentForm, PatientRecordForm
from users.models import User

@login_required
@role_required('RECEPTION')
def reception_dashboard(request):
    today_appointments = Appointment.objects.filter(
        date_time__date=timezone.now().date()
    ).order_by('date_time')
    
    new_patients = User.objects.filter(
        role='PATIENT', 
        date_joined__date=timezone.now().date()
    )
    
    return render(request, 'reception/dashboard.html', {
        'today_appointments': today_appointments,
        'new_patients': new_patients
    })

@login_required
@role_required('RECEPTION')
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('reception:appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'reception/appointment_form.html', {'form': form})

@login_required
@role_required('RECEPTION')
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-date_time')
    return render(request, 'reception/appointment_list.html', {'appointments': appointments})

@login_required
@role_required('RECEPTION')
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'reception/appointment_detail.html', {'appointment': appointment})

@login_required
@role_required('RECEPTION')
def patient_list(request):
    patients = User.objects.filter(role='PATIENT')
    return render(request, 'reception/patient_list.html', {'patients': patients})

@login_required
@role_required('RECEPTION')
def patient_detail(request, pk):
    patient = get_object_or_404(User, pk=pk)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date_time')[:5]
    return render(request, 'reception/patient_detail.html', {
        'patient': patient,
        'appointments': appointments
    })

# Add this function to resolve the error
@login_required
@role_required('RECEPTION')
def patient_record(request, pk):
    patient = get_object_or_404(User, pk=pk)
    record, created = PatientRecord.objects.get_or_create(patient=patient)
    
    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('reception:patient_detail', pk=patient.pk)
    else:
        form = PatientRecordForm(instance=record)
    
    return render(request, 'reception/patient_record.html', {
        'patient': patient,
        'form': form
    })