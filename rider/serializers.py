from .models import Rider
from rest_framework import serializers


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = "__all__"