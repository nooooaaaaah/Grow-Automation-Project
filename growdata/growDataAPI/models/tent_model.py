from django.db import models
from .cycle_model import Cycle

# Create your models here.
class Tent(models.Model):
    name = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    lightModel = models.IntegerField(default=None, blank=True, null=True)
    numOfLights  = models.IntegerField(default=1)
    lightOn = models.TimeField((u"Light on"), default=0, blank=True)
    lightOff = models.TimeField((u"Light off"), default=0, blank=True)

    def __str__(self):
        return self.name