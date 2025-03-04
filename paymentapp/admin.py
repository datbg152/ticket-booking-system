from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    def order_id(self, obj):
        return obj.order.id  # Lấy ID của Order

    list_display = ("id", "order_id", "amount_paid", "created_at", "status")
    search_fields = ("order__id", "status", "transaction_id")
    list_filter = ("status", "created_at")
