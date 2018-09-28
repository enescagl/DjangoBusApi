from django.db import models
from django.utils.timezone import now


class Customer(models.Model):
    createdAt = models.DateTimeField(default=now, blank=False)
    isDeleted = models.BooleanField(default=False)
    deletedAt = models.DateTimeField(blank=True)

    firstName = models.CharField()
    lastName = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
