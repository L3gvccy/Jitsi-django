import uuid
from django.shortcuts import render

def video_call_view(request):
    room_name = str(uuid.uuid4())  # уникальное имя комнаты
    return render(request, "videochat/call.html", {"room_name": room_name})
