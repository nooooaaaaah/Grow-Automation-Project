from django.contrib import admin
from .models import Cycle #
from .models import Tent #
from .models import Plant
from .models import Sensor
from .models import Sensor_Data

# Register your models here.
admin.site.register(Cycle)
admin.site.register(Tent)
admin.site.register(Plant)
admin.site.register(Sensor)
admin.site.register(Sensor_Data)

