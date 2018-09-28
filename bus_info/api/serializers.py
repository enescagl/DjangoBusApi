from rest_framework import serializers
from bus_info.models import Bus, BusType


class BusSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class BusTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusType
        fields = '__all__'
