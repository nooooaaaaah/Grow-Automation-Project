from rest_framework import serializers

from growDataAPI.models import Sensor

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'plant', 'tent')