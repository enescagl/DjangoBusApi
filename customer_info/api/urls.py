from django.urls import path, include
from views import CustomerViewSet, TicketViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customer-list', CustomerViewSet)
router.register(r'ticket-list', TicketViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
