from rest_framework import serializers

from growDataAPI.models import Tent

class TentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tent
        fields = ('name', 'id', 'lightModel', 'numOfLights', 'lightOn', 'lightOff')