from django.contrib import admin
from .models import CollectionRequest, CollectionPayment

class CollectionPaymentInline(admin.TabularInline):
    model = CollectionPayment
    extra = 1
    fields = ('amount', 'payment_method', 'transaction_id', 'payment_date')
    readonly_fields = ('payment_date',)

@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'preferred_date', 'status', 'payment_status', 'collector')
    list_filter = ('status', 'payment_status', 'preferred_date')
    search_fields = ('patient__username', 'collection_address')
    date_hierarchy = 'preferred_date'
    inlines = [CollectionPaymentInline]
    ordering = ('-preferred_date',)

@admin.register(CollectionPayment)
class CollectionPaymentAdmin(admin.ModelAdmin):
    list_display = ('collection', 'amount', 'payment_method', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('collection__patient__username',)
    date_hierarchy = 'payment_date'
    ordering = ('-payment_date',)