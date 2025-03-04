from django.urls import path
from . import views

urlpatterns = [
        path('paymentpage/',views.CreatePaymentView.as_view(),name = 'paymentpage'),


]