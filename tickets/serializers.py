from rest_framework import serializers

from .models import (
    Seats,
    TicketType,
    Tickets,
    Orders,
    Feedback,
    Booking,
    ClubCard
)


class TicketSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tickets
        fields = [
            'id',
            'ticket_type',
            'seats',
            'user',
            'orders',
            'show_time',
            'price',
            'payment_methods',
            'club_card',
        ]
        read_only_fields = ["price"]

    def validate(self, data):
        seats = data.get('seats')
        show_time = data.get('show_time')
        if Booking.objects.filter(seats=seats, show_time=show_time).exists():

            raise serializers.ValidationError('This seat is already reserved.')

        return data


class OrdersSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.SerializerMethodField('get_total_price')

    class Meta:
        model = Orders
        fields = [
            'id',
            'user',
            'total_price',
        ]

    @staticmethod
    def get_total_price(obj):
        tickets = Tickets.objects.filter(orders=obj.id)
        total_price = 0
        for ticket in tickets:

                total_price += ticket.price

        return total_price


class FeedbackSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = (
            'id',
            'title',
            'content',
            'rate',
            'user'
        )


class BookingSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = (
            'id',
            'show_time',
            'seats',
            'user'
        )

    def validate(self, data):
        seats = data.get('seats')
        show_time = data.get('show_time')
        if Booking.objects.filter(seats=seats, show_time=show_time).exists():
            raise serializers.ValidationError('This seat is already reserved!')
        return data


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = (
            'id',
            'number_of_seat',
            'number_of_row',
            'rooms'
        )


class ClubCardSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    balance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ClubCard
        fields = (
            'id',
            'user',
            'balance',
            'discount'
        )

    def get_balance(self, obj):
        orders = Tickets.objects.filter(user=obj.user)
        balance = 0
        for i in orders:
            balance += i.price
        if balance > 5000:
            obj.discount = 5
        if balance > 10000:
            obj.discount = 10
        if balance > 15000:
            obj.discount = 15
        obj.save()
        return balance


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = (
            'id',
            'name',
            'price'
        )