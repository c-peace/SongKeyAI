from django.urls import path
from SongKeyApp import views

urlpatterns = [
    path('', views.analyze, name='url'),
]
 