from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
)
from core.models import Guest, Hotel, Room, Booking
from core.serializers import (
    GuestSerializer,
    HotelSerializer,
    HotelDetailSerializer,
    HotelCreateUpdateDestroySerializer,
    RoomSerializer,
    BookingCreateSerializer,
)
from rest_framework.permissions import IsAdminUser


class GuestListCreateAPI(ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (IsAdminUser,)


class GuestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)


class HotelListAPI(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelRetrieveAPI(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    lookup_field = "id"


class HotelCreateAPI(CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateUpdateDestroySerializer
    permission_classes = (IsAdminUser,)


class HotelUpdateAPI(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateUpdateDestroySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)


class HotelDestroyAPI(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateUpdateDestroySerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)


class RoomListAPI(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomRetrieveAPI(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "id"


class RoomCreateAPI(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUser,)


class RoomUpdateAPI(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)


class RoomDestroyAPI(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)


class BookingListCreateAPI(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_classes = (IsAdminUser,)


class BookingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)
