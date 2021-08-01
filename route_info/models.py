from django.db import models
from base import models as base_models

from bus_info.models import Bus


class Location(base_models.TimestampedModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)


class Route(base_models.TimestampedModel):
    name = models.CharField(max_length=100)
    from_location = models.ForeignKey(Location,
                                      related_name='from_loc',
                                      on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location,
                                    related_name='to_loc',
                                    on_delete=models.CASCADE)


class Driver(base_models.TimestampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    drivers_licence_type = models.CharField(max_length=10)


class Trip(base_models.TimestampedModel):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="bus")
    route = models.ForeignKey(Route,
                              on_delete=models.CASCADE,
                              related_name="route")
    driver = models.ForeignKey(Driver,
                               on_delete=models.CASCADE,
                               related_name="driver")
    price = models.FloatField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    peron_number = models.CharField(max_length=10)
