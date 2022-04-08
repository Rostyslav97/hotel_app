from rest_framework.generics import ListAPIView
from core.models import Hotel
from core.serializers import HotelSerializer


class HotelListAPI(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer