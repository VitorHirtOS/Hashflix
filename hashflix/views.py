from django.shortcuts import render

# Functions Class Base Views -> Sites complexos, tendo templates prontos OU Functions View -> Sites simples, não vem com templates prontos

# Create your views here.
def Home(request):
    return render(request, 'hashflix/pages/home.html')