from rest_framework import generics

from route_info.models import Location, Route, Driver, Trip
from serializers import LocationSerializer, RouteSerializer, DriverSerializer, TripSerializer


class LocationViewSet(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RouteViewSet(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class DriverViewSet(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TripViewSet(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
