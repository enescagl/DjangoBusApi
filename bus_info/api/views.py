from bus_info.models import BusType, Bus
from bus_info.api.serializers import (
    BusTypeSerializer,
    BusSerializer,
)

from rest_framework import viewsets


class BusTypeViewSet(viewsets.ModelViewSet):
    queryset = BusType.objects.all()
    serializer_class = BusTypeSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
