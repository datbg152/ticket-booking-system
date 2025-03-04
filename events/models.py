from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='upcoming')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name


class TicketType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ticket Type'
        verbose_name_plural = 'Ticket Types'

    def __str__(self):
        return self.name


class EventTicket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Event Ticket'
        verbose_name_plural = 'Event Tickets'

    def __str__(self):
        return f"{self.event.name} - {self.ticket_type.name}"