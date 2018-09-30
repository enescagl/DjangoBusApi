from customer_info.models import Customer, Ticket
from customer_info.api.serializers import (
    CustomerSerializer,
    TicketSerializer,
)

from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
