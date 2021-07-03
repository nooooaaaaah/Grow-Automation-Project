from django.db import models

# Create your models here.
class Cycle(models.Model):
    name = models.CharField(max_length=60)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name