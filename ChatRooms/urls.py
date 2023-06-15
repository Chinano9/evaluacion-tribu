from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('rooms/', views.room_list, name='room_list'),
    path('create_room', views.create_room, name='create_room')
]
