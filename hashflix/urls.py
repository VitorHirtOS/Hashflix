from django.urls import path
from .views import Home, HomeFilmes, DetalhesFilmes


urlpatterns = [
    path('', Home.as_view()),
    path('filmes/', HomeFilmes.as_view()),
    path('filmes/<int:pk>', DetalhesFilmes.as_view()),
]