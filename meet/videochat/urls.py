from django.urls import path
from .views import video_call_view, create_conference, my_conferences, join_conference

urlpatterns = [
    path('my_conferences/', my_conferences, name='my_conferences'),
    path('create/', create_conference, name='create_conference'),
    path('<str:room_name>/', join_conference, name='join_conference'),
]
