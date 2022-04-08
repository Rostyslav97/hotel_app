from django.urls import path 
from core.views import GuestListCreateAPI, HotelListAPI, HotelRetrieveAPI, HotelCreateAPI, RoomListAPI, RoomCreateAPI, BookingListCreateAPI, BookingUpdateAPI


urlpatterns = [
    path("guest/", GuestListCreateAPI.as_view()),
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view()),
    path("hotel/create/", HotelCreateAPI.as_view()),
    path("rooms/", RoomListAPI.as_view()),
    path("room/create/", RoomCreateAPI.as_view()),
    path("booking/", BookingListCreateAPI.as_view()),
    path("booking/update/<int:id>/", BookingUpdateAPI.as_view())
]