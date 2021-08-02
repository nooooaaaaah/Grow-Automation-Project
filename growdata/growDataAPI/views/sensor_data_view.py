from rest_framework import viewsets

from growDataAPI.serializers import Sensor_DataSerializer
from growDataAPI.models import Sensor_Data

class Sensor_DataViewSet(viewsets.ModelViewSet):
    queryset = Sensor_Data.objects.all()
    serializer_class = Sensor_DataSerializer