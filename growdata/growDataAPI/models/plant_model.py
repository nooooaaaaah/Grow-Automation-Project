from django.db import models
from .tent_model import Tent

class Plant(models.Model):
    name = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    seed = models.BooleanField(default=False)
    clone = models.BooleanField(default=False)
    tent = models.ForeignKey(Tent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name