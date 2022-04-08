from rest_framework import serializers
from core.models import Guest, Hotel, Room, Booking


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ("name", "age", "phone", "email")
        

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", )


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", "location", "phone", "email")


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = ("id", )


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Room
        fields = ("room_no", "price", "hotel", "is_booked")


class BookingCreateSerializer(serializers.ModelSerializer):
    guest = serializers.SlugRelatedField(slug_field="name", read_only=True)
    hotel = serializers.SlugRelatedField(slug_field="name", read_only=True)
    room = serializers.SlugRelatedField(slug_field="room_no", read_only=True)
    class Meta:
        model = Booking
        exclude = ("id", )
