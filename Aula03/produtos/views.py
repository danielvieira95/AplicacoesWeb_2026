from django.shortcuts import render
from rest_framework import viewsets # importa o viewset a partir da biblioteca restframework

from .serializers import (ProdutoSerializer, CategoriaSerializer, ClienteSerializer, PedidoSerializer, ItemPedidoSerializer) 
from .models import (Produto, Categoria, Cliente, Pedido, ItemPedido)  
# importando metodo para exibir uma pagina home

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Django ! Aplicações Web 2026 -2 - Aula 05 Loja de Produtos")

    # Cria a classe Produtoviewset responsável por permitir fazer o crude

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("-id")
    serializer_class = ProdutoSerializer


# Categoria

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("-id")
    serializer_class = CategoriaSerializer
    


# Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("-id")
    serializer_class = ClienteSerializer
    
    
# Pedido

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by("-id")
    serializer_class = PedidoSerializer
    
    
# ItemPedido


class ItemPedidoViewSet(viewsets.ModelViewSet):
    
    queryset = ItemPedido.objects.all().order_by("-id")
    serializer_class = ItemPedidoSerializer
# Create your views here.
