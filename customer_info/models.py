from django.db import models
from django.utils.timezone import now

from route_info.models import Trip


class Customer(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Ticket(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
