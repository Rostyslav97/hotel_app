from django.urls import path
from core.views import GuestListCreateAPI, GuestRetrieveUpdateDestroyAPIView, HotelListAPI, HotelRetrieveAPI, HotelCreateAPI, HotelUpdateAPI, HotelDestroyAPI, RoomListAPI, RoomRetrieveAPI, RoomCreateAPI, RoomUpdateAPI, RoomDestroyAPI, BookingListCreateAPI, BookingRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("guest/", GuestListCreateAPI.as_view()),
    path("guest/<int:id>/", GuestRetrieveUpdateDestroyAPIView.as_view()),
    path("hotels/", HotelListAPI.as_view()),
    path("hotel/<int:id>/", HotelRetrieveAPI.as_view()),
    path("hotel/create/", HotelCreateAPI.as_view()),
    path("hotel/update/<int:id>/", HotelUpdateAPI.as_view()),
    path("hotel/delete/<int:id>/", HotelDestroyAPI.as_view()),
    path("rooms/", RoomListAPI.as_view()),
    path("room/<int:id>/", RoomRetrieveAPI.as_view()),
    path("room/create/", RoomCreateAPI.as_view()),
    path("room/update/<int:id>/", RoomUpdateAPI.as_view()),
    path("room/delete/<int:id>/", RoomDestroyAPI.as_view()),
    path("booking/", BookingListCreateAPI.as_view()),
    path("booking/<int:id>/", BookingRetrieveUpdateDestroyAPIView.as_view())
]