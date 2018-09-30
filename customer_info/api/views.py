from customer_info.models import Customer, Ticket
from serializers import CustomerSerializer, TicketSerializer

from rest_framework import generics


class CustomerViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TicketViewSet(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
