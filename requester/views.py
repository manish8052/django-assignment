from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Requester
from .serializers import RequesterSerializer
from rider.models import Rider
# Create your views here.


class RequesterAPI(APIView):
    serializer = RequesterSerializer

    def get(self, request, *args, **kwargs):
        requests = Requester.objects.all()
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        new_data = Requester.objects.create(from_location = request_data['from_location'],
                                            to_location = request_data['from_location'], 
                                            date = request_data['date'],
                                            assets = request_data['No of assets'], 
                                            asset_type = request_data['asset_type'],
                                            sensitivities = request_data['sensitivities'],
                                            recipient = request_data['recipient'])
        new_data.save()
        serializer = RequesterSerializer(new_data)
        return Response(serializer.data, status=201)
class MyAssetAPI(APIView):
    def get(self, request, *args, **kwargs):
        requests = Requester.objects.all()
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)


class MatchedAssetAPI(APIView):
    def get(self, request, *args, **kwargs):
        requests = Requester.objects.raw('SELECT requester_requester.recipient, requester_requester.from_location, requester_requester.to_location, requester_requester.date, requester_requester.assets FROM requester_requester INNER JOIN rider_rider ON requester_requester.from_location = rider_rider.from_location AND requester_requester.to_location = rider_rider.to_location AND requester_requester.date = rider_rider.date')
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)

