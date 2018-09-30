from bus_info.models import BusType, Bus
from serializers import BusTypeSerializer, BusSerializer

from rest_framework import generics


class BusTypeViewSet(generics.ListCreateAPIView):
    queryset = BusType.objects.all()
    serializer_class = BusTypeSerializer


class BusViewSet(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
