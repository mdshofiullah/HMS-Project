from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.decorators import role_required
from .models import LabTest, TestResult
from .forms import LabTestForm  # We'll create this form next
from users.models import User

@login_required
@role_required('LAB')
def lab_dashboard(request):
    pending_tests = LabTest.objects.filter(status='pending').count()
    in_progress_tests = LabTest.objects.filter(status='in_progress').count()
    recent_tests = LabTest.objects.order_by('-test_date')[:5]
    
    return render(request, 'lab/dashboard.html', {
        'pending_tests': pending_tests,
        'in_progress_tests': in_progress_tests,
        'recent_tests': recent_tests
    })

@login_required
@role_required('LAB')
def test_list(request):
    tests = LabTest.objects.all().order_by('-test_date')
    return render(request, 'lab/test_list.html', {'tests': tests})


@login_required
@role_required('LAB')
def create_test(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.ordered_by = request.user
            test.save()
            return redirect('lab:test_detail', pk=test.pk)
    else:
        form = LabTestForm()
    
    return render(request, 'lab/test_form.html', {'form': form})

@login_required
@role_required('LAB')
def test_detail(request, pk):
    test = get_object_or_404(LabTest, pk=pk)
    return render(request, 'lab/test_detail.html', {'test': test})

@login_required
@role_required('LAB')
def result_detail(request, pk):
    result = get_object_or_404(TestResult, pk=pk)
    return render(request, 'lab/result_detail.html', {'result': result})

@login_required
@role_required('LAB')
def verify_result(request, pk):
    result = get_object_or_404(TestResult, pk=pk)
    if not result.verified:
        result.verified = True
        result.verified_by = request.user
        result.save()
    return render(request, 'lab/verification_success.html', {'result': result})