from rest_framework import serializers
from .models import Event, TicketType, EventTicket

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'venue', 'event_date', 'status']


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ['name','description']
class EventTicketSerializer(serializers.ModelSerializer):
    ticket_type = serializers.CharField(source="ticket_type.name")  # Lấy tên loại vé
    description = serializers.CharField(source="ticket_type.description")  # Lấy description từ TicketType

    class Meta:
        model = EventTicket
        fields = ["event", "ticket_type", "description", "price", "capacity"]