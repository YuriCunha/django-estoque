from django.db import models

class Cores(models.Model):
    cor = models.CharField('Cor', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.cor

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        ordering =['id']