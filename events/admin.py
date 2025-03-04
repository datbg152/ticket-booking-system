from django.contrib import admin
from .models import Event, TicketType, EventTicket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'event_date', 'status', 'created_at')
    list_filter = ('status', 'event_date')
    search_fields = ('name', 'venue')

@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    #list_display = ('name', 'created_at')
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(EventTicket)
class EventTicketAdmin(admin.ModelAdmin):
    #list_display = ('event', 'ticket_type', 'price', 'capacity', 'created_at')
    list_display = ('event', 'ticket_type', 'price', 'capacity')
    list_filter = ('event', 'ticket_type')