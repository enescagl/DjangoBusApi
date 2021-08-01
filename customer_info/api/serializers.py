from route_info.api.serializers import TripSerializer
from rest_framework import serializers
from customer_info.models import Customer, Ticket


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class TicketSerializer(serializers.HyperlinkedModelSerializer):

    customer = CustomerSerializer(many=True, read_only=True)
    trip = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
