from django.db import models
from django.db.models.base import Model

# Create your models here.

class Donation(models.Model):
    amount = models.IntegerField()
    paymenttype = models.CharField(max_length=255)
    upvotes = models.IntegerField()
