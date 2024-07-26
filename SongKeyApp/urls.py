from django.urls import path
from SongKeyApp import views

urlpatterns = [
    path('', views.index, name='url'),
    path('analyze/', views.analyze, name='url')
]
 