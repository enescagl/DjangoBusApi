from rest_framework import serializers
from customer_info.models import Customer, Ticket


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    model = Customer
    fields = '__all__'


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    model = Ticket
    fields = '__all__'
