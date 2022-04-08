from django.urls import path 
from core.views import HotelListAPI, HotelRetrieveAPI, RoomListAPI


urlpatterns = [
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view()),
    path("rooms/", RoomListAPI.as_view())
]