from customer_info.api.views import CustomerViewSet, TicketViewSet

from rest_framework import routers

from django.urls import path, include

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customer', CustomerViewSet)
router.register(r'ticket', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
