from django.urls import path 
from core.views import HotelListAPI, HotelRetrieveAPI


urlpatterns = [
    path("hotels/", HotelListAPI.as_view()),
    path("hotels/<int:id>/", HotelRetrieveAPI.as_view())
]