from bus_info.api.views import BusTypeViewSet, BusViewSet

from rest_framework import routers

from django.urls import path, include

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'bustype', BusTypeViewSet)
router.register(r'bus', BusViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
