from django.contrib import admin
from django.urls import path, include
from .views import HotelsViewSet, RoomsViewSet, ReservationsViewSet, RoomPhotoListApiView, RoomPhotoDetailsApiView, \
    HotelPhotoDetailsApiView, HotelPhotoListApiView, transaction_list_post_view, transaction_view, CommentsViewSet, \
    comments_by_hotel_detail

urlpatterns = [
    path('hotels/', HotelsViewSet.as_view({'get': 'list',
                                           'post': 'create'})),
    path('hotels/<int:pk>/', HotelsViewSet.as_view({'get': 'retrieve',
                                                    'delete': 'destroy',
                                                    'put': 'update'})),
    path('hotels/<int:rk>/rooms/', RoomsViewSet.as_view({'get': 'rooms_by_hotel',
                                                         'post': 'create'})),
    path('hotels/<int:rk>/rooms/<int:pk>/', RoomsViewSet.as_view({'get': 'room_details_by_hotel',
                                                                  'delete': 'destroy',
                                                                  'put': 'update'})),
    path('roomphotos/', RoomPhotoListApiView.as_view()),
    path('roomphotos/<int:pk>/', RoomPhotoDetailsApiView.as_view()),
    path('hotelphotos/', HotelPhotoListApiView.as_view()),
    path('hotelphotos/<int:pk>/', HotelPhotoDetailsApiView.as_view()),

    path('hotels/<int:pk>/reservations/', ReservationsViewSet.as_view({'get': 'reservations_by_hotel'})),
    path('reservations/', ReservationsViewSet.as_view({'get': 'list',
                                                       'post': 'create'})),
    path('reservations/<int:pk>/', ReservationsViewSet.as_view({'get': 'retrieve',
                                                                'delete': 'destroy',
                                                                'put': 'update'})),
    path('transactions/', transaction_list_post_view),
    path('transactions/<int:pk>/', transaction_view),
    path('comments/', CommentsViewSet.as_view({'get': 'list',
                                               'post': 'create'})),
    path('comments/<int:pk>/', CommentsViewSet.as_view({'get': 'retrieve',
                                                        'delete': 'destroy',
                                                        'put': 'update'})),
    path('hotels/<int:hk>/comments/', CommentsViewSet.as_view({'get': 'comments_by_hotel'})),
    path('hotels/<int:hk>/comments/<int:pk>/', comments_by_hotel_detail),
]
