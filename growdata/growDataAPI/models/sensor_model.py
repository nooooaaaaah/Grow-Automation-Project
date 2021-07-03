from django.db import models
from .plant_model import Plant
from .tent_model import Tent

class Sensor(models.Model):
   name = models.CharField(max_length=60)
   id = models.AutoField(primary_key=True)
   plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
   tent = models.ForeignKey(Tent, on_delete=models.CASCADE)

   def __str__(self):
        return self.name