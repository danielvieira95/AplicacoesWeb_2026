from django.db import models

# Create your models here.

# Cria a classe Categoria

class Categoria (models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome
    
    
# Cria a classe chamada produto
class Produto (models.Model):
    nome = models.CharField(max_length=120) # definindo o tamanho do nome do produto com tamanho maximo de 120 caracteres
    quantidade = models.PositiveIntegerField(default=0) # quantidade do produto
    preco = models.DecimalField(max_digits=10,decimal_places=2) # definindo a qtde de digitos e casas decimais
    
    # Aqui atraves da chave relacionamos a categoria e o produto
    categoria = models.ForeignKey(
        Categoria,
        # serve para caso exclua a categoria não exclua o produto
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "produtos"
    )
    created_at = models.DateTimeField(auto_now_add = True) # registro de tempo automatico quando o produto é carregado



    # cria a função
    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"
    


# Cria a classe cliente

class Cliente(models.Model):
    
    nome = models.CharField(max_length = 150)
    email = models.EmailField(
        unique = True # Registra como unico o email
    )
    
    telefone = models.CharField(
        max_length = 20,
        blank = True # pode deixar em branco
    )
    
    
    def __str__(self):
        return self.nome
    
    
    
    # Cria a classe Pedido
    
class Pedido (models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("PAGO", "Pago"),
        ("ENVIADO","Enviado"),
        ("ENTREGUE", "Entregue"),
        ("CANCELADO","Cancelado")
    ]
    
    # relacionando cliente com pedidos
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete = models.CASCADE,
        related_name = "pedidos"
    )
    
    descricao = models.CharField(
        max_length = 200,
        blank = True
    ),
    
    data_pedido = models.DateTimeField(
        auto_now_add = True
    ),
    
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = "PENDENTE"
    )
    
    
    def total(self):
        return sum(
            item.subtotal()
            for item in self.itens.all()
        )
    
    def __str__(self):
        
        return f"Pedido {self.id} - {self.cliente.nome} - {self.descricao}"
    


# Cria  a classe item pedido

class ItemPedido(models.Model):
    
    pedido = models.ForeignKey(
        Pedido,
        on_delete = models.CASCADE,
        related_name = 'itens'
    )
    
    produto = models.ForeignKey(
        Produto,
        on_delete = models.PROTECT)
    
    
    quantidade = models.PositiveIntegerField() 
    
    preco_unitario =models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        editable = False
    )
    
    
    def save(self, *args, **kwargs):
        # Ao criar um novo item do pedido pega automaticamente
        if self.pk is None:
            self.preco_unitario = self.produto.preco
        
            
        super().save(*args, **kwargs)
        
    def subtotal (self):
        
        return self.quantidade * self.preco_unitario
    
    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"