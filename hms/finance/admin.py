from django.contrib import admin
from .models import Invoice, InvoiceItem, Payment

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1
    fields = ('description', 'quantity', 'unit_price', 'total_price')
    readonly_fields = ('total_price',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date', 'due_date', 'total_amount', 'paid_amount', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__username',)
    date_hierarchy = 'date'
    inlines = [InvoiceItemInline]
    readonly_fields = ('total_amount', 'paid_amount')
    ordering = ('-date',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'payment_method', 'payment_date', 'received_by')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('invoice__patient__username', 'transaction_id')
    date_hierarchy = 'payment_date'
    ordering = ('-payment_date',)