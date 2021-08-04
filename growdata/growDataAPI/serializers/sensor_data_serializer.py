from rest_framework import serializers

from growDataAPI.models import Sensor_Data

class Sensor_DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor_Data
        fields = ('id', 'temp', 'humidity', 'sensor')