from django.db import models

from base import models as base_models


class BusType(base_models.TimestampedModel):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    seat_count = models.IntegerField(blank=False)
    internet = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    power_outlet = models.BooleanField(default=False)
    tablet = models.BooleanField(default=False)


class Bus(base_models.TimestampedModel):
    licence_plate = models.CharField(max_length=8)
    bus_type = models.ForeignKey(BusType,
                                 on_delete=models.CASCADE,
                                 related_name="bus_type")
