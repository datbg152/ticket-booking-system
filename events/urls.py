from django.urls import path
from . import views

urlpatterns = [
        path('ticketSet/',views.event.as_view(),name = 'event'),
        path('tickettype/<int:pk>/',views.tickettype.as_view(), name = 'tickettype'),
        path('eventticket/',views.eventticket.as_view(),name = 'eventticket'),
        path('infoticket/<int:event_id>/<int:ticket_type_id>/',views.GetTicketInfo.as_view(),name = 'GetTicketInfo')

]