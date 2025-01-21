from django.shortcuts import render

# Create your views here.

def chat_room(request, room_name):
    context = {"room_name": room_name}
    return render(request, 'livechat.html', context)