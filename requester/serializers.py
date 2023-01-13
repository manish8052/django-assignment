from .models import Requester
from rest_framework import serializers


class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = "__all__"