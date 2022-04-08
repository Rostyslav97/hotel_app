from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from core.models import Guest, Hotel, Room, Booking
from core.serializers import GuestSerializer, HotelSerializer, HotelDetailSerializer, HotelCreateSerializer, RoomSerializer, BookingCreateSerializer
from rest_framework.permissions import IsAdminUser


class GuestListCreateAPI(ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAdminUser, )


class HotelListAPI(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRetrieveAPI(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    lookup_field = "id"


class HotelCreateAPI(CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer
    permission_classes = (IsAdminUser, )


class RoomListAPI(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class RoomCreateAPI(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUser, )


class BookingListCreateAPI(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_classes = (IsAdminUser, )


class BookingUpdateAPI(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )

