import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Conference

def video_call_view(request):
    room_name = str(uuid.uuid4())
    return render(request, "videochat/call.html", {"room_name": room_name})

def create_conference(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_time = request.POST.get('start_time')
        room_name = str(uuid.uuid4())
        created_by = request.user
        
        conference = Conference.objects.create(
            title=title,
            description=description,
            start_time=start_time,
            room_name=room_name,
            created_by=created_by
        )
        conference.save()
        messages.success(request, "Конференцію створено успішно!")
        return redirect('/')

    return render(request, "videochat/create_conference.html")

def my_conferences(request):
    conferences = Conference.objects.filter(created_by=request.user)
    return render(request, "videochat/my_conferences.html", {"conferences": conferences})

def join_conference(request, room_name):
    try:
        conference = Conference.objects.get(room_name=room_name)
    except conference.DoesNotExist:
        messages.error(request, "Конференція не знайдена.")
        return redirect('/')

    return render(request, "videochat/call.html", {"conference": conference})