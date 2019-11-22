from django.db import models
from core.models import Cores

class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    cor = models.ForeignKey(Cores, on_delete='protect')
    descricao = models.TextField('Descrição', blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade', default=0)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)

    def __str__(self):
        return self.nome

