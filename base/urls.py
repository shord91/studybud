from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('login/',views.LoginPage, name = 'login'),
    path('register/', views.RegisterPage, name='register'),
    path('logout/', views.LogoutUser, name = 'logout'),
    path('room/<int:pk>/', views.room, name = 'room'),
    path('profile/<int:pk>/', views.userProfile, name='user-profile'),
    path('create-room/', views.CreateRoom, name='create-room'),
    path('update-room/<int:pk>/', views.UpdateRoom, name='update-room'),
    path('delete-room/<int:pk>/', views.DeleteRoom, name='delete-room'),
    path('delete-message/<int:pk>/', views.DeleteMessage, name='delete-message'),
]