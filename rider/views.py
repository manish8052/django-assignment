from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Rider
from .serializers import RiderSerializer
# Create your views here.


class RiderAPI(APIView):
    serializer = RiderSerializer

    def get(self, request, *args, **kwargs):
        requests = Rider.objects.all()
        serializer = RiderSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        new_data = Rider.objects.create(from_location = request_data['from_location'],
                                        to_location = request_data['from_location'], 
                                        date_time = request_data['date_time'], 
                                        travel_medium = request_data['travel_medium'],
                                        assets_quantity = request_data['assets_quantity'])
        new_data.save()
        serializer = RiderSerializer(new_data)
        return Response(serializer.data, status=201)

