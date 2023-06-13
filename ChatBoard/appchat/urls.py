from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('roomsupdate/', rooms_return, name="rooms_return"),
    path('<str:room_name>/', room, name="room"),
    path('api/users/', userlist, name="userlist"),

]
