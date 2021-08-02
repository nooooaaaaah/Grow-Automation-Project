from rest_framework import serializers

from growDataAPI.models import Tent
from growDataAPI.models import Cycle

class TentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tent
        cycle = Cycle
        fields = ('id', 'name', 'cycle', 'lightWatts', 'numOfLights')
