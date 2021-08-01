from route_info.api.views import (
    LocationViewSet,
    RouteViewSet,
    DriverViewSet,
    TripViewSet,
)
from rest_framework import routers

from django.urls import path, include

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'location', LocationViewSet)
router.register(r'route', RouteViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'trip', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
