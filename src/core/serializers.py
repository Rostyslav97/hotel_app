from rest_framework import serializers
from core.models import Guest, Hotel, Room, Booking


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ("id", "name", "age", "phone", "email")


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
        )


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("id", "name", "location", "phone", "email")


class HotelCreateUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelDetailSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ("id", "room_no", "price", "hotel", "is_booked")


class BookingCreateSerializer(serializers.ModelSerializer):
    guest = serializers.SlugRelatedField(slug_field="name", read_only=True)
    hotel = serializers.SlugRelatedField(slug_field="name", read_only=True)
    room = serializers.SlugRelatedField(slug_field="room_no", read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
