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

