from django.db import models
from .sensor_model import Sensor

class Sensor_Data(models.Model):
    id = models.AutoField(primary_key=True)
    temp = models.IntegerField()
    humidity = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name