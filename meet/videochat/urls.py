from django.urls import path
from .views import video_call_view

urlpatterns = [
    path('call/', video_call_view, name='video_call'),
]
