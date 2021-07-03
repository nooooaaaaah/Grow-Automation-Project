# Create your views here.
from rest_framework import viewsets

from growDataAPI.serializers import CycleSerializer
from growDataAPI.models import Cycle


class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer