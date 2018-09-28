from django.db import models
from django.utils.timezone import now
from ..bus_info.models import Bus


class Location(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    name = models.CharField()
    abbreviation = models.CharField()


class Route(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    name = models.CharField()
    fromLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    toLocation = models.ForeignKey(Location, on_delete=models.CASCADE)


class Driver(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    firstName = models.CharField()
    lastName = models.CharField()
    driversLicenceType = models.CharField()


class Trip(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    price = models.FloatField()
    departureTime = models.DateTimeField()
    arrivalTime = models.DateTimeField()
    peronNumber = models.CharField()
