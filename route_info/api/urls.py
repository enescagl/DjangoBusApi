from django.urls import path, include

from rest_framework import routers

from views import LocationViewSet, RouteViewSet, DriverViewSet, TripViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'location-list', LocationViewSet)
router.register(r'route-list', RouteViewSet)
router.register(r'driver-list', DriverViewSet)
router.register(r'trip-list', TripViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
