from django.contrib import admin
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, HotelPhoto, Comment

# Register your models here.

admin.site.register(Hotel)
admin.site.register(HotelPhoto)
admin.site.register(Room)
admin.site.register(RoomPhoto)
admin.site.register(Reservation)
admin.site.register(Transaction)
admin.site.register(Comment)
