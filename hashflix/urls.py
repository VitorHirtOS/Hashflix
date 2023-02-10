from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name="home-netflix"),
    path('filmes/', views.HomeFilme, name="homefilmes")
]