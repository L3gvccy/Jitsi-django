from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages, auth


# Create your views here.
def main_page(request):
    return render(request, 'account/main_page.html')

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