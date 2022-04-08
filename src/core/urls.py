from django.urls import path 
from core.views import GuestCreateAPI, HotelListAPI, HotelRetrieveAPI, RoomListAPI, BookingCreateAPI


urlpatterns = [
    path("guest/", GuestCreateAPI.as_view()),
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view()),
    path("rooms/", RoomListAPI.as_view()),
    path("booking/create/", BookingCreateAPI.as_view()),
]