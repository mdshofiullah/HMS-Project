from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('dashboard/', views.finance_dashboard, name='finance_dashboard'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/new/', views.create_invoice, name='create_invoice'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('reports/', views.financial_reports, name='financial_reports'),
]