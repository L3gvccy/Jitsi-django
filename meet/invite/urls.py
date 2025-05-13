from django.urls import path
from .views import create_invite, my_invites

urlpatterns = [
    path('create/<str:room_name>/', create_invite, name='create_invite'),
    path('my_invites/', my_invites, name='my_invites'),
]
