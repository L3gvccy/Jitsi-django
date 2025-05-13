from django.urls import path
from .views import create_invite

urlpatterns = [
    path('create/<str:room_name>/', create_invite, name='create_invite'),
]
