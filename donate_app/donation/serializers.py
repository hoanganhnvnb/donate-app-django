from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Donation

class GetAllDonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = ('id', 'amount', 'paymenttype', 'upvotes', )