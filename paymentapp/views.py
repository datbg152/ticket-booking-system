from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from paymentapp.models import Payment
from booking.models import Order
from paymentapp.tasks import process_payment


class CreatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get("order_id")
        order = get_object_or_404(Order, id=order_id, user=request.user, status="pending")
        
        payment, created = Payment.objects.get_or_create(
            order_id=order,
            defaults={
                "variant": "default",
                "amount_paid": order.total_amount,
                "status": "pending",
            }
        )
        
        process_payment.apply_async(queue="payment_queue")

        
        return Response({"message": "Payment processing", "payment_id": payment.id}, status=202)