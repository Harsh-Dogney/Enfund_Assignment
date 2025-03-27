from collections import UserDict
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from .models import Message
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required()
def chat_home(request):
    form = RoomForm(request.POST or None)
    users = User.objects.exclude(username=request.user.username)  

    if request.method == 'POST' and form.is_valid():
        room_name = form.cleaned_data['room_name']
        db_messages = Message.objects.filter(room=room_name)[:]
        messages.success(request, f"Joined: {room_name}")
        return render(request, 'chat/chatroom.html', {
            'room_name': room_name,
            'title': room_name,
            'db_messages': db_messages
        })

    return render(request, 'chat/chat.html', {
        'form': form,
        'users': users
    })


@login_required
def chat_room(request, room_name):
    db_messages = Message.objects.filter(room=room_name)
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'title': room_name,
        'db_messages': db_messages,
        'users': users,
    })



def chat_page(request, room_name="global"):
    return render(request, "chat/chatroom.html", {
        "room_name": room_name,
        "username": request.user.username if request.user.is_authenticated else "Anonymous"
    })
