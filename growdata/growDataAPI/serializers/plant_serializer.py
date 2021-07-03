from rest_framework import serializers

from growDataAPI.models import Plant

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('name', 'id', 'seed', 'clone', 'tent')