from django.urls import path
from core.views import HotelListAPI


urlpatterns = [
    path("hotels", HotelListAPI.as_view()),
]