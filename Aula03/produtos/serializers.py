from rest_framework import serializers

from .models import (
    Produto,
    Categoria,
    Cliente,
    Pedido,
    ItemPedido
)

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cliente



# Classe usuarioserializer

class CadastroUsuarioSerializers(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    
    nome = serializers.CharField()
    email = serializers.EmailField()
    telefone = serializers.CharField(
        required = False,
        allow_blank = True
    )
    
    def validated_username(self, value):
        
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Este nome de usuario já está cadastrado"
            )
            
            return value
            
    def validate_email(self, value):
        
        if Cliente.objects.filter(email=value).exists():
            
            raise serializers.ValidationError("Este email já está cadastrado")
        return value
       
    def create(self, validated_data):
        
        #Cria o usuario de autenticação do Django
        
        usuario = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        
        
        # cria o cliente
        
        cliente = Cliente.objects.create(
            usuario =usuario,
            nome = validated_data['nome'],
            email = validated_data['email'],
            telefone = validated_data.get('telefone','')
        )
        
        return cliente
    
    def to_representation(self, instance):
        
        return{
            "id": instance.id,
            "username":instance.usuario.username,
            "nome":instance.nome,
            "email":instance.email,
            "telefone":instance.telefone
        }


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
    cliente = serializers.PrimaryKeyRelatedField(
        read_only = True
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
