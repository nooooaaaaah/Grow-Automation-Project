from rest_framework import serializers

from growDataAPI.models import Plant

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'seed', 'clone', 'tent')