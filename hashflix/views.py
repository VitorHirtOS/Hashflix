from django.shortcuts import render
from .models import Filme

# Functions Class Base Views -> Sites complexos, tendo templates prontos OU Functions Class View -> Sites simples, não vem com templates prontos

# Create your views here.
def Home(request):
    return render(request, 'hashflix/pages/home.html')


def HomeFilme(request):
    context = {}
    lista_filmes = Filme.objects.all()
    context['lista_filmes'] = lista_filmes
    return render(request, 'hashflix/pages/homefilmes2.html', context)