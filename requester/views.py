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
        # requests = model_to_dict(requests).update({"status":"pending"})
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)


class MatchedAssetAPI(APIView):
    def get(self, request, *args, **kwargs):
        requests = Requester.objects.raw('SELECT requester_requester.recipient, requester_requester.from_location, requester_requester.to_location, requester_requester.date, requester_requester.assets FROM requester_requester INNER JOIN rider_rider ON requester_requester.from_location = rider_rider.from_location AND requester_requester.to_location = rider_rider.to_location AND requester_requester.date = rider_rider.date')
        # requests = model_to_dict(requests).update({"status":"pending"})
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)

# def create_AssetTransport(request):
#     if request.method == 'POST':
#         # Get the posted data
#         from_location = request.POST.get('from_location')
#         to_location = request.POST.get('to_location')
#         date_time = request.POST.get('date_time')
#         asset_type = request.POST.get('asset_type')
#         sensitivities = request.POST.get('sensitivities')
#         recipient = request.POST.get('recipient')
#         # Create a new Employee object
#         asset_transport = Requester(first_name=first_name, last_name=last_name, email=email)
#         asset_transport.save()

#         # Return a JSON response with the new employee's ID
#         return JsonResponse({'employee_id': employee.id}, status=201)
#     else:
#         # Return a JSON response with an error message
#         return JsonResponse({'error': 'Invalid request method'}, status=405)