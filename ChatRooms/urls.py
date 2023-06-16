from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('rooms/', views.room_list, name='room_list'),
    path('create_room/', views.create_room, name='create_room'),
    path('edit_room/', views.edit_room, name='edit_room'),
    path('rooms/<int:room_id>', views.room, name='room'),
    path('rooms/my_rooms', views.my_rooms, name='my_rooms')
]
