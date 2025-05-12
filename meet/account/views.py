from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def main_page(request):
    return render(request, 'account/main_page.html')

def login(request):
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        context = {
            'username': username,
            'lastname': lastname,
            'firstname': firstname
        }

        if password != confirm_pass:
            context['pass_err'] = 'Введені паролі не співпадають'
            return render(request, 'account/register.html', context)
        
        if len(password) < 3:
            context['pass_err'] = 'Пароль має складатись мінімум з 3 символів'
            return render(request, 'account/register.html', context)
        
        if User.objects.filter(username = login).exists():
            context['login_err'] = 'Користувач з таким логіном вже існує'
            return render(request, 'account/register.html', context)

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

