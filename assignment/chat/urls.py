from django.contrib import admin

from django.urls import path
from .views import chat_page

app_name = "chat"

urlpatterns = [
    path('', lambda request: chat_page(request, room_name="global"), name='chat_page'),
    path('<str:room_name>/', chat_page, name='chat_room'),
]
