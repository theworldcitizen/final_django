import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.base import Model
from rest_framework.exceptions import ValidationError

from auth_.models import MainUser
from utils.constants import star_numbers, room_type, status_choices


def is_valid_date(value):
    if datetime.date.today() > value:
        raise ValidationError("You can make reservation for future date only")


def is_valid_number(value):
    if value < 0:
        raise ValidationError("The cost can not be negative number")


def is_valid_account_number(value):
    value = len(value)
    if 8 > value > 12:
        raise ValidationError("Please enter valid account number")


def is_valid_comment(value):
    value = len(value)
    if value <= 1:
        raise ValidationError("Please add some words!")


class RoomManager(models.Manager):
    use_in_migrations = True

    def room_details_by_hotel(self, rk, pk):
        return self.filter(id=pk, hotel=rk)


class HotelManager(models.Manager):
    use_in_migrations = True

    def room_details_by_hotel(self, pk, rk):
        return self.filter(id=pk).filter(hotel=rk)


class ReservationManager(models.Manager):
    use_in_migrations = True

    def reservations_by_hotel(self, pk):
        return self.filter(hotel=pk)


class CommentManager(models.Manager):
    use_in_migrations = True

    def comment_detail_by_hotel(self, hk, pk):
        return self.filter(id=pk).filter(hotel=hk)


class Hotel(models.Model):
    name = models.CharField("Name", max_length=20)
    hotelier = models.ForeignKey(MainUser, verbose_name="Hotelier", on_delete=models.CASCADE, null=True)
    number_of_stars = models.IntegerField("Number of stars", choices=star_numbers)
    number_of_ratings = models.IntegerField("Number of ratings", default=0)
    rating = models.FloatField("rating", default=0)
    account_number = models.IntegerField("Account Number", blank=False)
    address = models.CharField("Address", max_length=200, blank=False)
    city = models.CharField("City", max_length=20)
    phone_number = models.CharField("Phone Number", max_length=11)
    yard = models.BooleanField("Yard")
    pool = models.BooleanField("Pool")
    gym = models.BooleanField("Gym")
    wifi = models.BooleanField("Wifi")
    parking = models.BooleanField("Parking")
    restaurant = models.BooleanField("Restaurant")

    objects = HotelManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"


# class RoomsManager(models.Manager):
#     use_in_migrations = True
#
#     def room_details_by_hotel(self, pk, rk):
#         return self.get(id=rk).hotel.filter(id=pk)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True)
    type = models.CharField("Type", choices=room_type, max_length=20)
    cost = models.IntegerField("Cost", validators=[is_valid_number])
    area = models.IntegerField("Area", validators=[is_valid_number])
    king_bed = models.IntegerField("King Bed")
    queen_bed = models.IntegerField("Queen Bed")
    tv = models.BooleanField("TV")
    wifi = models.BooleanField("Wifi")
    kitchen = models.BooleanField("Kitchen")
    extra_bed = models.BooleanField("Extra Bed")

    objects = RoomManager()

    # def __str__(self):
    #     return str(self.hotel + " " + self.type)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Photos(models.Model):
    photo = models.ImageField()

    class Meta:
        abstract = True


class HotelPhoto(Photos):
    photo = models.ImageField(upload_to='hotel_photos', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True,
                              related_name="hotel_photos")


class RoomPhoto(Photos):
    photo = models.ImageField(upload_to='room_photos', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE, null=True, related_name="room_photos")


class Reservation(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE, null=True,
                             related_name="room_reservations")
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True,
                              related_name="hotel_reservations")
    check_in = models.DateField("Check In", validators=[is_valid_date])
    check_out = models.DateField("Check Out", validators=[is_valid_date])
    # request_time = models.DateTimeField("Request Time", auto_now=True)
    total_cost = models.IntegerField("Total Cost", validators=[is_valid_number])
    payment_status = models.IntegerField("Payment status", choices=status_choices)

    objects = ReservationManager()

    def __str__(self):
        return self.room.type + ": " + str(self.customer)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Transaction(models.Model):
    reservation = models.OneToOneField(Reservation, verbose_name="Reservation", on_delete=models.CASCADE, null=True,
                                       related_name="reservation_transaction")
    reference_number = models.IntegerField("Reference number")

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Comment(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True,
                                 related_name="customer_comments")
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True,
                              related_name="hotel_comments")
    text = models.TextField("Comment Text", validators=[is_valid_comment])
    rating = models.IntegerField("Number of stars", choices=star_numbers)

    objects = CommentManager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '%s: %s' % (self.customer.first_name, self.text)


def star_numbers():
    return None
