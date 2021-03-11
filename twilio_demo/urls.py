from django.urls import path

from twilio_demo import views

urlpatterns = [
    path('crear/', views.create_room, name='create_room'),
    path('', views.index, name='index'),
]
