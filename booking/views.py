from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import Order, OrderItem
from events.models import EventTicket
from django.db import transaction
from accounts.permissions import IsCustomer
from rest_framework.permissions import IsAuthenticated


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def post(self, request):
        user = request.user  # Giả sử user đã đăng nhập
        event_id = request.data.get("event_id")
        ticket_type_id = request.data.get("ticket_type_id")
        quantity = int(request.data.get("quantity", 1))

        if quantity <= 0:
            return Response({"error": "Quantity must be at least 1"}, status=400)

        try:
            with transaction.atomic():  # avoid from race condition
                event_ticket = EventTicket.objects.select_for_update().get(
                    event_id=event_id, ticket_type_id=ticket_type_id
                )

                total_sold = OrderItem.objects.filter(
                    event_id=event_id, ticket_type_id=ticket_type_id
                ).aggregate(total=Sum("quantity"))["total"] or 0

                remaining_capacity = event_ticket.capacity - total_sold
                if quantity > remaining_capacity:
                    return Response({"error": "Not enough tickets available"}, status=400)

                # Nếu còn vé, tạo Order & OrderItem
                order = Order.objects.create(user=user, total_amount=event_ticket.price * quantity, status="pending")
                OrderItem.objects.create(order=order, event_id=event_id, ticket_type_id=ticket_type_id,
                                          quantity=quantity, unit_price=event_ticket.price, subtotal=event_ticket.price * quantity)

                return Response({"message": "Order created successfully", "order_id": order.id}, status=201)

        except EventTicket.DoesNotExist:
            return Response({"error": "Invalid event or ticket type"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
