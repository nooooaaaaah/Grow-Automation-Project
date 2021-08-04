from django.db import models
from .sensor_model import Sensor

class Sensor_Data(models.Model):
    id = models.AutoField(primary_key=True)
    temp = models.DecimalField((""), max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField((""), max_digits=5, decimal_places=2, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name