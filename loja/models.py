from django.db import models


class Cliente(models.Model):

    ESTADOS = [
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('PR', 'Paraná'),
        ('BA', 'Bahia'),
        ('RS', 'Rio Grande do Sul'),
    ]

    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    ]

    CONTATOS = [
        ('C', 'Carta'),
        ('E', 'E-mail'),
        ('T', 'Telefone'),
        ('F', 'Fax'),
    ]

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    cidade = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENEROS)
    contato = models.CharField(max_length=1, choices=CONTATOS)
    email = models.EmailField()
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.nome


class Produto(models.Model):

    CORES = [
        ('Azul', 'Azul'),
        ('Vermelho', 'Vermelho'),
        ('Verde', 'Verde'),
        ('Amarelo', 'Amarelo'),
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Marrom', 'Marrom'),
    ]

    nome = models.CharField(max_length=70)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    cor = models.CharField(max_length=20, choices=CORES)
    data_fabricacao = models.DateField()
    
    imagem = models.ImageField(
    upload_to='produtos/',
    blank=True,
    null=True,
    verbose_name='Imagem do produto'
)
    def __str__(self):
        return self.nome