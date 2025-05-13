from django.urls import path
from .views import login, register, logout, profile_user, change_password

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_user, name='profile_user'),
    path('profile/change-password/', change_password, name='change_password'),
]