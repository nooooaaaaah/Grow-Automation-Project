from rest_framework import serializers


from growDataAPI.models import Cycle
from growDataAPI.serializers.tent_serializer import TentSerializer

class CycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        tent_set = TentSerializer(many=True)
        model = Cycle
        fields = ('id', 'name', 'tent_set')


        