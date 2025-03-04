from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import isAuthenticated
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsManager
from .serializers import EventSerializer, TicketTypeSerializer,EventTicketSerializer
from .models import TicketType, Event ,EventTicket
from rest_framework import status

#ceate event by manages
class event(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def post(self,request):
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status = 400)

# Create your views here.

#Create ticket_type and modify existing ticket (everyone can modify so consider to classify in the future )
class tickettype(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    def post(self,request):
        serializer = TicketTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = 201)
        return Response(serializer.errors,status = 400)
    
    def patch(self, request, pk):  # Cập nhật một phần thông tin
        try:
            ticket_type = TicketType.objects.get(id=pk)
        except TicketType.DoesNotExist:
            return Response({"error": "TicketType not found or no permission"}, status=404)

        serializer = TicketTypeSerializer(ticket_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

#user creates ticket following existing event and ticket   
class eventticket(APIView):

    permission_classes = [IsAuthenticated,IsManager]
    def post(self, request):
        event_id = request.data.get("event_id")
        ticket_type_id = request.data.get("ticket_type_id")

        # check event if existing 
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        # check ticket type if existing 
        try:
            ticket_type = TicketType.objects.get(id=ticket_type_id)
        except TicketType.DoesNotExist:
            return Response({"error": "Ticket Type not found"}, status=status.HTTP_404_NOT_FOUND)

        # both of them existing 
        event_ticket = EventTicket.objects.create(
            event=event,
            ticket_type=ticket_type,
            price=request.data.get("price"),
            capacity=request.data.get("capacity"),
        )

        return Response(
            {"message": "Event Ticket created successfully", "id": event_ticket.id},
            status=status.HTTP_201_CREATED,
        )
    
#manage check ticket info depending on foreign key 
class GetTicketInfo(APIView):
    def get(self, request, event_id, ticket_type_id):
        try:
            # Lấy event_ticket dựa trên event_id và ticket_type_id
            event_ticket = EventTicket.objects.get(event_id=event_id, ticket_type_id=ticket_type_id)
            
            # Truy xuất description từ ticket_type
            description = event_ticket.ticket_type.description  

            return Response({
                "event_id": event_ticket.event.id,
                "ticket_type": event_ticket.ticket_type.name,
                "description": description,
                "price": event_ticket.price,
                "capacity": event_ticket.capacity
            })

        except EventTicket.DoesNotExist:
            return Response({"error": "Event Ticket not found"}, status=404)