from rest_framework import viewsets

from growDataAPI.serializers import TentSerializer
from growDataAPI.models import Tent

class TentViewSet(viewsets.ModelViewSet):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer