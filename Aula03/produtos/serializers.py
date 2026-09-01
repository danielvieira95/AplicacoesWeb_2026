from rest_framework import serializers

from .models import (
    Produto,
    Categoria,
    Cliente,
    Pedido,
    ItemPedido
)


# Categoria
class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = "__all__"


# Produto
class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = "__all__"


# Cliente
class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"


# ItemPedido
class ItemPedidoSerializer(serializers.ModelSerializer):

    subtotal = serializers.SerializerMethodField(
        read_only=True
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

        read_only_fields = [
            "preco_unitario"
        ]

    def get_subtotal(self, obj):
        return obj.subtotal()


# Pedido
class PedidoSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Pedido

        fields = [
            "id",
            "cliente",
            "descricao",
            "data_pedido",
            "status",
            "total"
        ]

        read_only_fields = [
            "data_pedido",
            "status"
        ]

    def get_total(self, obj):
        return obj.total()




class ItemPedidoDetalheSerializer(serializers.ModelSerializer):
    
    produto_nome = serializers.CharField(
        source="produto.nome",
        read_only=True
    )

    subtotal = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = ItemPedido

        fields = [
            "id",
            "produto",
            "produto_nome",
            "quantidade",
            "preco_unitario",
            "subtotal"
        ]

    def get_subtotal(self, obj):
        return obj.subtotal()

# Alteração do status do pedido
class StatusPedidoSerializer(serializers.ModelSerializer):
    
    itens = ItemPedidoDetalheSerializer(
        many=True,
        read_only=True
    )

    total = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Pedido

        fields = [
            "id",
            "cliente",
            "descricao",
            "data_pedido",
            "status",
            "itens",
            "total"
        ]

        read_only_fields = [
            "id",
            "cliente",
            "descricao",
            "data_pedido",
            "itens",
            "total"
        ]

    def get_total(self, obj):
        return obj.total()
