from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.models import Hotel, Room
from core.serializers import HotelSerializer, HotelDetailSerializer, RoomSerializer


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
    