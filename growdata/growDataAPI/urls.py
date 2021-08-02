from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cycle', views.CycleViewSet)
router.register(r'tent', views.TentViewSet) #added 7/14
router.register(r'plant', views.PlantViewSet)
router.register(r'sensor', views.SensorViewSet)
router.register(r'sensor_data', views.Sensor_DataViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]