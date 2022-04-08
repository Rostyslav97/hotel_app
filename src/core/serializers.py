from rest_framework import serializers
from core.models import Hotel, Room


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", )


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ("name", "location", "phone", "email")


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Room
        fields = ("room_no", "price", "hotel", "is_booked")