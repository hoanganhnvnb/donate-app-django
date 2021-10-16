from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Donation
from .serializers import GetAllDonationSerializer

# Create your views here.

class GetAllDonationAPIView(APIView):

    def get(self, request):
        list_donation = Donation.objects.all()
        data = GetAllDonationSerializer(list_donation, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)