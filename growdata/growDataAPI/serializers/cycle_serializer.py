from rest_framework import serializers


from growDataAPI.models import Cycle
from growDataAPI.serializers.tent_serializer import TentSerializer

class CycleSerializer(serializers.HyperlinkedModelSerializer):
    tent_set = TentSerializer(many=True)
    class Meta:
        model = Cycle
        fields = ('name', 'id', 'tent_set')


        