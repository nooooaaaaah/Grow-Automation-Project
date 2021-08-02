from rest_framework import viewsets

from growDataAPI.serializers import PlantSerializer
from growDataAPI.models import Plant

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer