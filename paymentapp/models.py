from django.db import models
from booking.models import Order

# Create your models here.
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  

    def get_failure_url(self) -> str:
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self) -> str:
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"
    
    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id}"

   
