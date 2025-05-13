from django.urls import path
from .views import video_call_view, create_conference, my_conferences, join_conference, edit_conference, delete_conference, direct_join_conference

urlpatterns = [
    path('direct_join_conference/', direct_join_conference, name='direct_join_conference'),
    path('my_conferences/', my_conferences, name='my_conferences'),
    path('edit/<str:room_name>/', edit_conference, name='edit_conference'),
    path('delete/<str:room_name>/', delete_conference, name='delete_conference'),
    path('create/', create_conference, name='create_conference'),
    path('<str:room_name>/', join_conference, name='join_conference'),
]
