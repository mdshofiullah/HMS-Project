from django.shortcuts import render
from users.models import User
from core.models import HospitalInfo

def home(request):
    doctors = User.objects.filter(role='DOCTOR')[:4]
    hospital_info = HospitalInfo.objects.first()
    return render(request, 'website/home.html', {
        'doctors': doctors,
        'hospital_info': hospital_info
    })

def doctor_list(request):
    doctors = User.objects.filter(role='DOCTOR')
    specializations = User.objects.filter(
        role='DOCTOR'
    ).values_list('specialization', flat=True).distinct()
    
    return render(request, 'website/doctor_list.html', {
        'doctors': doctors,
        'specializations': specializations
    })

def doctor_detail(request, pk):
    doctor = User.objects.get(pk=pk, role='DOCTOR')
    return render(request, 'website/doctor_detail.html', {'doctor': doctor})

def book_appointment(request):
    return render(request, 'website/book_appointment.html')

def services(request):
    return render(request, 'website/services.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    hospital_info = HospitalInfo.objects.first()
    return render(request, 'website/about.html', {'hospital_info': hospital_info})

def reports(request):
    return render(request, 'website/reports.html')

def home_collection_request(request):
    return render(request, 'website/home_collection_request.html')