from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny

from .models import (
    Seats,
    TicketType,
    Tickets,
    Orders,
    Feedback,
    Booking,
    ClubCard
)

from .serializers import (
    SeatsSerializer,
    TicketTypeSerializer,
    TicketSerializer,
    OrdersSerializer,
    FeedbackSerializer,
    BookingSerializer,
    ClubCardSerializer
)


class TicketsViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Tickets.objects.all()
    permission_classes = [AllowAny, ]


class OrderViewSet(ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = [AllowAny, ]


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [AllowAny, ]


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]


class SeatsViewSet(ModelViewSet):
    serializer_class = SeatsSerializer
    queryset = Seats.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]


class TicketTypeViewSet(ModelViewSet):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()
    permission_classes = [AllowAny, ]


class ClubCardViewSet(ModelViewSet):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()
    permission_classes = [AllowAny, ]