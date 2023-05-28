from rest_framework.routers import DefaultRouter

from .views import (
    SeatsViewSet,
    OrderViewSet,
    FeedbackViewSet,
    ClubCardViewSet,
    TicketTypeViewSet,
    BookingViewSet,
    TicketsViewSet
)

tickets_router = DefaultRouter()
tickets_router.register(r'seats', SeatsViewSet, basename='seats')
tickets_router.register(r'orders', OrderViewSet, basename='orders')
tickets_router.register(r'feedback', FeedbackViewSet, basename='feedback')
tickets_router.register(r'club-card', ClubCardViewSet, basename='club-card')
tickets_router.register(r'ticket-type', TicketTypeViewSet, basename='ticket-type')
tickets_router.register(r'booking', BookingViewSet, basename='booking')
tickets_router.register(r'tickets', TicketsViewSet, basename='tickets')


urlpatterns = [

]