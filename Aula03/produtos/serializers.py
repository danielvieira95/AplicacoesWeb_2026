 # Arquivo serializers responsável por transformar a requisição de informação para salvar no banco de dados no formato de tabela
 # importand da biblioteca rest framework o serializers
from rest_framework import serializers
from .models import (Produto, Categoria, Cliente, Pedido, ItemPedido)



# Criando Serializar para a Categoria
class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
       model = Categoria
       fields = "__all__" 


 # Criando a classe Serializers produtos
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        # fields = ["id","nome","quantidade","preco","created_at"]
        fields = "__all__"
        


# Cliente 

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        
        
# ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
    
    subtotal = serializers.SerializerMethodField(
        read_only = True
    )
    
    
    class Meta:
        
        model = ItemPedido
        fields = [
            "id",
            "pedido",
            "produto",
            "quantidade",
            "preco_unitario",
            "subtotal"
        ]
        
        
    def get_subtotal(self,obj):
        return obj.subtotal()
    
    
    
# Pedido


class PedidoSerializer(serializers.ModelSerializer):
    
    total = serializers.SerializerMethodField(
        read_only = True
    )
    
    
    class Meta:
        
        model = Pedido
        fields = [
            "id",
            "cliente",
            "data_pedido",
            "status",
            "total"
        ]
        
    def get_total(self,obj):
        return obj.total()