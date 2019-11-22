from django.db import models
from produto.models import Produtos

class NotasEntradas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete='protect')
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)

    def __str__(self):
        return self.produto.nome
