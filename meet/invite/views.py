from django.shortcuts import render
from .models import Invite
from videochat.models import Conference
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def create_invite(request, room_name):
    conference = Conference.objects.get(room_name=room_name)
    context = {
        'conference': conference,
    }
    if request.method == 'POST':
        inv_username = request.POST.get('username')
        if request.user.username == inv_username:
            context['err'] = "Ви не можете запросити себе."
            return render(request, 'invite/create_invite.html', context)
        if User.objects.filter(username=inv_username).exists():
            invited_user = User.objects.get(username=inv_username)
            if Invite.objects.filter(conference=conference, invited_user=invited_user).exists():
                context['err'] = "Цей користувач вже запрошений."
                return render(request, 'invite/create_invite.html', context)
            
            invite = Invite.objects.create(
                conference=conference,
                invited_user=invited_user,
                invited_by=request.user
            )
            invite.save()
            messages.success(request, "Запрошення надіслано успішно!")
            return render(request, 'invite/create_invite.html', context)
        else:
            context['err'] = "Користувача не знайдено."
            return render(request, 'invite/create_invite.html', context)
    return render(request, 'invite/create_invite.html', context)