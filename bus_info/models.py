from django.db import models
from django.utils.timezone import now


class BusType(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    seatCount = models.IntegerField(blank=False)
    internet = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    powerOutlet = models.BooleanField(default=False)
    tablet = models.BooleanField(default=False)


class Bus(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    licencePlate = models.CharField(max_length=8)
    busType = models.ForeignKey(BusType, on_delete=models.CASCADE)
