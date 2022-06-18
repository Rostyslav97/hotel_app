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


app_name = "core"


urlpatterns = [
    path("guests/", GuestListCreateAPI.as_view(), name="list_guests"),
    path("guests/<int:id>/", GuestRetrieveUpdateDestroyAPIView.as_view(), name="retrieve_update_destroy_guests"),
    path("hotels/", HotelListAPI.as_view(), name="list_hotels"),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view(), name="retrieve_hotels"),
    path("hotels/create/", HotelCreateAPI.as_view(), name="create_hotels"),
    path("hotels/update/<int:id>/", HotelUpdateAPI.as_view(), name="update_hotels"),
    path("hotels/destroy/<int:id>/", HotelDestroyAPI.as_view(), name="destroy_hotels"),
    path("rooms/", RoomListAPI.as_view(), name="list_rooms"),
    path("rooms/<int:id>/", RoomRetrieveAPI.as_view(), name="retrieve_rooms"),
    path("rooms/create/", RoomCreateAPI.as_view(), name="create_rooms"),
    path("rooms/update/<int:id>/", RoomUpdateAPI.as_view(), name="update_rooms"),
    path("rooms/destroy/<int:id>/", RoomDestroyAPI.as_view(), name="destroy_rooms"),
    path("bookings/", BookingListCreateAPI.as_view(), name="list_bookings"),
    path("bookings/<int:id>/", BookingRetrieveUpdateDestroyAPIView.as_view(), name="retrieve_update_destroy_bookings"),
]
