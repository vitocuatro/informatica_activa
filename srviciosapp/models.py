from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo    = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen_externa = models.CharField(null=True,blank=True,max_length=300)
    #imagen    = models.ImageField()
    created   = models.DateTimeField(auto_now_add=True)
    update    = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    def __str__(self):
        return self.titulo