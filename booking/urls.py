from django.urls import path
from . import views

urlpatterns = [
    path('creorder/',views.CreateOrderView.as_view(),name = 'creorder'),

]