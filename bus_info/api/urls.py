from django.urls import path, include

from views import BusTypeViewSet, BusViewSet

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'bustype-list', BusTypeViewSet)
router.register(r'bus-list', BusViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
