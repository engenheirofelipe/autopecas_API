from django.db import models

class Categoria(models.Model):

    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome 

class Produto(models.Model):

    NIVEL = (
        ('C','Caro'),
        ('I','Intermediario'),
        ('B','Barato'),
    )

    nome = models.CharField(max_length = 100)
    preco = models.CharField(blank = False, max_length = 10)
    quantidade = models.CharField(blank = False, max_length = 1000)
    descricao = models.CharField(blank = False, max_length=10000)    
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False , null = False, default = 'I')       

     # Adicionando a chave estrangeira para Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')


    def __str__(self):
        return self.nome         