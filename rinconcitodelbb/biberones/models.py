from django.db import models

# Create your models here.

class Biberon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    price = models.TextField(verbose_name='Precio', default=None)
    image = models.ImageField(verbose_name='Imagen', upload_to='biberones')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'biberon'
        verbose_name_plural = 'biberones'
        ordering = ['-price']
    
    def __str__(self):
        return self.title
    
