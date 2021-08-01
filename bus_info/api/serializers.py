from rest_framework import serializers
from bus_info.models import Bus, BusType


class BusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusType
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):
    bus_type = BusTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Bus
        fields = '__all__'
