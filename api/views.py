import logging

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, HotelPhoto, Comment, star_numbers
from .serializers import HotelSerializer, HotelSerializerShort, HotelPhotoSerializer, \
    TransactionSerializer, CommentSerializer, RoomSerializerShort, RoomPhotoSerializer, ReservationSerializer, \
    RoomSerializer, ReservationSerializerShort

# Create your views here.

logger = logging.getLogger(__name__)


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelSerializerShort
        elif self.action == 'retrieve':
            return HotelSerializer
        elif self.action == 'create':
            return HotelSerializer
        elif self.action == 'update':
            return HotelSerializerShort
        elif self.action == 'destroy':
            return HotelSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RoomSerializerShort

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomSerializerShort
        # elif self.action == 'retrieve':
        #     return RoomSerializer
        if self.action == 'create':
            return RoomSerializer
        elif self.action == 'update':
            return RoomSerializer
        elif self.action == 'destroy':
            return RoomSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def rooms_by_hotel(self, request, rk):
        queryset = Room.objects.filter(hotel=rk)
        serializer = RoomSerializerShort(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def room_details_by_hotel(self, request, pk, rk):
        queryset = Room.objects.room_details_by_hotel(rk, pk)
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReservationSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ReservationSerializerShort
        elif self.action == 'retrieve':
            return ReservationSerializer
        elif self.action == 'create':
            return ReservationSerializer
        elif self.action == 'update':
            return ReservationSerializer
        elif self.action == 'destroy':
            return ReservationSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def reservations_by_hotel(self, request, pk):
        queryset = Reservation.objects.reservations_by_hotel(pk)
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)


class RoomPhotoListApiView(generics.ListCreateAPIView):
    serializer_class = RoomPhotoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser, JSONParser, MultiPartParser]

    def get_queryset(self):
        queryset = RoomPhoto.objects.all()
        return queryset


class RoomPhotoDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomPhotoSerializer
    permission_classes = (AllowAny,)
    queryset = RoomPhoto.objects.all()
    parser_classes = [FormParser, JSONParser, MultiPartParser]

    def get_queryset(self):
        queryset = HotelPhoto.objects.all()
        return queryset


class HotelPhotoListApiView(generics.ListCreateAPIView):
    serializer_class = HotelPhotoSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser, JSONParser, MultiPartParser]

    def get_queryset(self):
        queryset = HotelPhoto.objects.all()
        return queryset


class HotelPhotoDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelPhotoSerializer
    permission_classes = (AllowAny,)
    queryset = HotelPhoto.objects.all()
    parser_classes = [FormParser, JSONParser, MultiPartParser]


@api_view(['GET', 'POST'])
def transaction_list_post_view(request):
    if request.method == 'GET':
        transaction_list = Transaction.objects.all()
        serializer = TransactionSerializer(transaction_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Transaction created ID: {serializer.instance}')
            logger.info(f'Transaction created ID:  {serializer.instance}')
            logger.warning(f'Transaction created ID:  {serializer.instance}')
            logger.error(f'Transaction created ID:  {serializer.instance}')
            logger.critical(f'Transaction created ID:  {serializer.instance}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def transaction_view(request, pk):
    try:
        transaction = Transaction.objects.get(id=pk)
    except Transaction.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TransactionSerializer(instance=transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    if request.method == 'DELETE':
        transaction.delete()
        return Response({'deleted': True})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionSerializer
        elif self.action == 'retrieve':
            return TransactionSerializer
        elif self.action == 'create':
            return TransactionSerializer
        elif self.action == 'update':
            return TransactionSerializer
        elif self.action == 'destroy':
            return TransactionSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentSerializer
        elif self.action == 'retrieve':
            return CommentSerializer
        elif self.action == 'create':
            return CommentSerializer
        elif self.action == 'update':
            return CommentSerializer
        elif self.action == 'destroy':
            return CommentSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def comments_by_hotel(self, request, hk):
        queryset = Comment.objects.filter(hotel=hk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def comments_by_hotel_detail(request, pk, hk):
    queryset = Comment.objects.comment_detail_by_hotel(hk, pk)
    serializer = CommentSerializer(queryset, many=True)
    return Response(serializer.data)
