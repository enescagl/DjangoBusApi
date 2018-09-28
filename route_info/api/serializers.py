from rest_framework import serializers
from route_info.models import Location, Driver, Route, Trip


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DriverSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = Driver
        fields = '__all__'


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
