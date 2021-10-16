from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Donation
from .serializers import GetAllDonationSerializer, PostDonationSerializer

# Create your views here.

class GetAllDonationAPIView(APIView):

    def get(self, request):
        list_donation = Donation.objects.all()
        data = GetAllDonationSerializer(list_donation, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

class PostDonationAPIView(APIView):

    def post(self, request):
        data = PostDonationSerializer(data=request.data)

        if not data.is_valid():
            return Response('Invalid data', status=status.HTTP_400_BAD_REQUEST)

        amount = data.data['amount']
        paymenttype = data.data['paymenttype']
        upvotes = data.data['upvotes']
        
        dnt = Donation.objects.create(amount=amount, paymenttype=paymenttype, upvotes=upvotes)

        return Response(data=dnt.id, status=status.HTTP_200_OK)