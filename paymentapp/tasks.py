from celery import shared_task
from django.utils.timezone import now
from django.db import transaction
from booking.models import Order
from paymentapp.models import Payment
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(payment_id, user_email):
    payment = Payment.objects.get(id=payment_id)
    subject = "Payment Confirmation"
    message = f"Your payment status is now: {payment.status}."
    send_mail(subject, message, "noreply@example.com", [user_email])


@shared_task
def process_payment(order_id):
    try:
        order = Order.objects.get(id=order_id)
        payment = Payment.objects.get(order_id=order_id)
        
        #make logic to access real provider like paypal,stripeß
        if payment.variant == 'default':  
            success = True  
        else:
            success = False

        with transaction.atomic():
            if success:
                payment.status = 'confirmed'
                payment.paid_at = now()
                order.status = 'paid'
            else:
                payment.status = 'failed'
                order.status = 'failed'
            
            payment.save()
            order.save()
        send_payment_confirmation_email.apply_async(queue="email_queue")
        return {"message": "Payment processed successfully"}
    except Exception as e:
        return {"message": f"Error processing payment: {str(e)}"}
