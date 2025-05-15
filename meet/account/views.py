from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from videochat.models import Conference
from invite.models import Invite

# Create your views here.
def main_page(request):
    if request.user.is_authenticated:
        conference_count = Conference.objects.filter(created_by=request.user).count()
        invitation_count = Invite.objects.filter(invited_user=request.user).count()
    else:
        conference_count = 0
        invitation_count = 0
    
    return render(request, 'account/main_page.html', {
        'conference_count': conference_count,
        'invitation_count': invitation_count
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Вітаємо, {user.first_name}! Ви увійшли в систему.")
            return redirect('/')
        else:
            messages.error(request, "Невірне ім’я користувача або пароль.")
            return render(request, 'account/login.html')
        
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if password != confirm_pass:
            messages.error(request, "Паролі не співпадають.")
            return

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname
        )
        user.save()

        messages.success(request, "Реєстрація успішна!")
        return redirect('/account/login/')
    
    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Ви успішно вийшли з акаунту!")
    return redirect('/')

@login_required
def profile_user(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        messages.success(request, "Інформацію оновлено успішно!")
        return redirect('/account/profile/')

    return render(request, 'account/profile.html', {'user': request.user})

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "Старий пароль введено невірно.")
        elif new_password != confirm_password:
            messages.error(request, "Нові паролі не співпадають.")
        else:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль успішно змінено.")
            return redirect('/account/profile/')

    return render(request, 'account/change_password.html')