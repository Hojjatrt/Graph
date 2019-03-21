from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('data/', views.data, name='data'),
]