from django.contrib import admin
from .models import Order, OrderItem, UserTicket

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'event', 'ticket_type', 'quantity', 'unit_price', 'subtotal', 'created_at')
    list_filter = ('event', 'ticket_type', 'created_at')
    search_fields = ('order__id', 'event__name', 'ticket_type__name')

@admin.register(UserTicket)
class UserTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_item', 'qr_code', 'redeemed_at', 'created_at')
    list_filter = ('redeemed_at', 'created_at')
    search_fields = ('qr_code',)