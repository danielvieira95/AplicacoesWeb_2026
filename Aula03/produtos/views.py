from django.shortcuts import render
from rest_framework import viewsets # importa o viewset a partir da biblioteca restframework
from .models import Pedido
from .serializers import StatusPedidoSerializer
from rest_framework import mixins

from .serializers import (ProdutoSerializer, CategoriaSerializer, ClienteSerializer, PedidoSerializer, ItemPedidoSerializer,StatusPedidoSerializer) 
from .models import (Produto, Categoria, Cliente, Pedido, ItemPedido)  
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import(
    AllowAny, IsAuthenticated
)

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CadastroUsuarioSerializers

# importando metodo para exibir uma pagina home

from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Django ! Aplicações Web 2026 -2 - Aula 05 Loja de Produtos")




class CadastroUsuarioView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = CadastroUsuarioSerializers
    permission_classes = [AllowAny]


    # Cria a classe Produtoviewset responsável por permitir fazer o crude

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("-id")
    serializer_class = ProdutoSerializer
    
    # função de permissao
    
    def get_permissions(self):
        
        # Permite que qualquer pessoa consulte produtos
        if self.action in ['list', 'retrieve']:
            
            return [AllowAny()]
        
        # Para poder cadastrar, editar ou excluir o usuario precisa estar autenticado
        
        return [IsAuthenticated()]


# Categoria

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("-id")
    serializer_class = CategoriaSerializer
    


# Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("-id")
    serializer_class = ClienteSerializer
    
    
   
    
# ItemPedido


class ItemPedidoViewSet(viewsets.ModelViewSet):
    
    queryset = ItemPedido.objects.all().order_by("-id")
    serializer_class = ItemPedidoSerializer
# Create your views here.


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    
    # Mostra somente os pedidos do usuario autenticado
    
    def get_queryset(self):
        
        return Pedido.objects.filter(
            cliente_usuario = self.request.user).order_by("-id")
        
        
    # Ao criar um pedido, associa automaticamente ao cliente autenticado
    
    def perform_create(self, serializer):
        
        try: 
        
             cliente = Cliente.objects.get(
             usuario = self.request.user
        )
             
        except Cliente.DoesNotExist:
            raise ValidationError ("O usuario autenticado não possui um cliente associado")
        
        serializer.save(cliente =cliente)
        







class StatusPedidoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = Pedido.objects.all()
    serializer_class = StatusPedidoSerializer