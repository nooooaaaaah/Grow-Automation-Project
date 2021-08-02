from rest_framework import viewsets

from growDataAPI.serializers import SensorSerializer
from growDataAPI.models import Sensor

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer