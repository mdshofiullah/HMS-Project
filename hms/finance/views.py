from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.decorators import role_required

@login_required
@role_required('FINANCE')
def finance_dashboard(request):
    return render(request, 'finance/dashboard.html')

@login_required
@role_required('FINANCE')
def invoice_list(request):
    return render(request, 'finance/invoice_list.html')

@login_required
@role_required('FINANCE')
def create_invoice(request):
    return render(request, 'finance/invoice_form.html')

@login_required
@role_required('FINANCE')
def invoice_detail(request, pk):
    return render(request, 'finance/invoice_detail.html', {'invoice_id': pk})

@login_required
@role_required('FINANCE')
def payment_list(request):
    return render(request, 'finance/payment_list.html')

@login_required
@role_required('FINANCE')
def payment_detail(request, pk):
    return render(request, 'finance/payment_detail.html', {'payment_id': pk})

@login_required
@role_required('FINANCE')
def financial_reports(request):
    return render(request, 'finance/financial_reports.html')