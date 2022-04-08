from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from core.models import Guest, Hotel, Room, Booking
from core.serializers import GuestSerializer, HotelSerializer, HotelDetailSerializer, RoomSerializer, BookingCreateSerializer


class GuestCreateAPI(CreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class HotelListAPI(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRetrieveAPI(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    lookup_field = "id"


class RoomListAPI(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class BookingCreateAPI(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
