from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'account/main_page.html')

def login(request):
    return render(request, 'account/login.html')