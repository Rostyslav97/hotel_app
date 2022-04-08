from django.urls import path 
from core.views import GuestCreateAPI, HotelListAPI, HotelRetrieveAPI, RoomListAPI


urlpatterns = [
    path("guest/", GuestCreateAPI.as_view()),
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view()),
    path("rooms/", RoomListAPI.as_view())
]