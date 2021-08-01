from django.db import models
from base import models as base_models

from route_info.models import Trip


class Customer(base_models.TimestampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Ticket(base_models.TimestampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
