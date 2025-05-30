from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.decorators import role_required
from reception.models import Appointment
from .models import MedicalReport, DoctorSchedule
from .forms import MedicalReportForm, ScheduleForm

@login_required
@role_required('DOCTOR')
def doctor_dashboard(request):
    appointments = Appointment.objects.filter(
        doctor=request.user, 
        status='scheduled'
    ).order_by('date_time')[:5]
    
    recent_reports = MedicalReport.objects.filter(
        doctor=request.user
    ).order_by('-created_at')[:5]
    
    return render(request, 'doctor/dashboard.html', {
        'appointments': appointments,
        'recent_reports': recent_reports
    })

@login_required
@role_required('DOCTOR')
def create_report(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.user, request.POST)  # Pass current user
        if form.is_valid():
            report = form.save(commit=False)
            report.doctor = request.user
            report.save()
            return redirect('doctor:report_detail', pk=report.pk)
    else:
        form = MedicalReportForm(request.user)  # Pass current user
    return render(request, 'doctor/report_form.html', {'form': form})

@login_required
@role_required('DOCTOR')
def schedule_management(request):
    schedules = DoctorSchedule.objects.filter(doctor=request.user)
    
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.doctor = request.user
            schedule.save()
            return redirect('doctor:schedule_management')
    else:
        form = ScheduleForm()
    
    return render(request, 'doctor/schedule.html', {
        'schedules': schedules,
        'form': form
    })
    

@login_required
@role_required('DOCTOR')
def appointment_list(request):
    appointments = Appointment.objects.filter(doctor=request.user).order_by('-date_time')
    return render(request, 'doctor/appointment_list.html', {'appointments': appointments})

@login_required
@role_required('DOCTOR')
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, doctor=request.user)
    return render(request, 'doctor/appointment_detail.html', {'appointment': appointment})

@login_required
@role_required('DOCTOR')
def patient_list(request):
    patients = User.objects.filter(
        role='PATIENT',
        patient_appointments__doctor=request.user
    ).distinct()
    return render(request, 'doctor/patient_list.html', {'patients': patients})

@login_required
@role_required('DOCTOR')
def patient_detail(request, pk):
    patient = get_object_or_404(User, pk=pk, role='PATIENT')
    appointments = Appointment.objects.filter(patient=patient, doctor=request.user).order_by('-date_time')
    reports = MedicalReport.objects.filter(patient=patient, doctor=request.user).order_by('-created_at')[:5]
    
    return render(request, 'doctor/patient_detail.html', {
        'patient': patient,
        'appointments': appointments,
        'reports': reports
    })

@login_required
@role_required('DOCTOR')
def report_detail(request, pk):
    report = get_object_or_404(MedicalReport, pk=pk, doctor=request.user)
    return render(request, 'doctor/report_detail.html', {'report': report})