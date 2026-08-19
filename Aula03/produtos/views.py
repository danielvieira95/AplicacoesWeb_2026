from django.shortcuts import render
from rest_framework import viewsets # importa o viewset a partir da biblioteca restframework
from .models import  Produto
from .serializers import ProdutoSerializer

# importando metodo para exibir uma pagina home

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Django ! Aplicações Web 2026 -2 - Aula 03 Loja de Produtos")

    # Cria a classe Produtoviewset responsável por permitir fazer o crude

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("-id")
    serializer_class = ProdutoSerializer


# Create your views here.
