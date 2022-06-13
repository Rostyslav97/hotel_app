from django.urls import path
from core.views import (
    GuestListCreateAPI,
    GuestRetrieveUpdateDestroyAPIView,
    HotelListAPI,
    HotelRetrieveAPI,
    HotelCreateAPI,
    HotelUpdateAPI,
    HotelDestroyAPI,
    RoomListAPI,
    RoomRetrieveAPI,
    RoomCreateAPI,
    RoomUpdateAPI,
    RoomDestroyAPI,
    BookingListCreateAPI,
    BookingRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("guests/", GuestListCreateAPI.as_view()),
    path("guests/<int:id>/", GuestRetrieveUpdateDestroyAPIView.as_view()),
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view()),
    path("hotels/create/", HotelCreateAPI.as_view()),
    path("hotels/update/<int:id>/", HotelUpdateAPI.as_view()),
    path("hotels/delete/<int:id>/", HotelDestroyAPI.as_view()),
    path("rooms/", RoomListAPI.as_view()),
    path("rooms/<int:id>/", RoomRetrieveAPI.as_view()),
    path("rooms/create/", RoomCreateAPI.as_view()),
    path("rooms/update/<int:id>/", RoomUpdateAPI.as_view()),
    path("rooms/delete/<int:id>/", RoomDestroyAPI.as_view()),
    path("bookings/", BookingListCreateAPI.as_view()),
    path("bookings/<int:id>/", BookingRetrieveUpdateDestroyAPIView.as_view()),
]
