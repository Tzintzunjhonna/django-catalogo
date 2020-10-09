from django.db import models

# Create your models here.

class Moño(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'moño'
        verbose_name_plural = 'moños'
        ordering = ['-created']

    def __str__(self):
        return self.title
    