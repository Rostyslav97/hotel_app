from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    room_no = models.IntegerField()
    price = models.FloatField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.room_no)


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    num_of_guests = models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    def __str__(self) -> str:
        return self.guest.name

    def hotel_name(self) -> str:
        return self.hotel.hotel
