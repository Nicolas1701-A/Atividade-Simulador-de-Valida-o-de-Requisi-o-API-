# No arquivo views.py do seu app
from django.http import HttpResponse

def home(request):
# O back-end prepara uma resposta em texto ou HTML
    return HttpResponse("<h1>Bem-vindo à API de Desenvolvimento de Sistemas!</h1>")

# No arquivo urls.py do projeto
from django.urls import path
from . import views

urlpatterns = [
# Quando o usuário acessar 'dominio.com/inicio/', o Django chama a
função 'home'
path('inicio/', views.home, name='pagina_inicial'),
]
