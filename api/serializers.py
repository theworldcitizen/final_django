from rest_framework import serializers
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, HotelPhoto, Comment


class HotelPhotoSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = HotelPhoto
        fields = '__all__'


class BaseHotelSerializer(serializers.ModelSerializer):
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'
        abstract = True


class HotelSerializerShort(BaseHotelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name']
        # fields = ['__all__']


class HotelSerializer(BaseHotelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomPhotoSerializer(serializers.Serializer):
    room_id = serializers.IntegerField(write_only=True)
    photo = serializers.ImageField()

    def create(self, validated_data):
        room_photo = RoomPhoto()
        room_photo.room_id = validated_data.get('room_id')
        room_photo.photo = validated_data.get('photo')
        room_photo.save()
        return room_photo

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


class BaseRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'cost', 'area', 'king_bed', 'queen_bed', 'tv', 'wifi', 'kitchen', 'extra_bed',
                  'room_photos']
        abstract = True


class RoomSerializer(BaseRoomSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializerShort(BaseRoomSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type', 'cost', 'area', 'room_photos']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ReservationSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'hotel', 'check_in', 'check_out']


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MainUser
#         fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction
        # fields = ['reservation_id', 'reference_number']
        fields = '__all__'


class BaseCommentSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(write_only=True)
    hotel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        abstract = True


class CommentSerializer(BaseCommentSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
