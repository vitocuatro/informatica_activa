from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    nombre    = models.CharField(max_length=50)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now_add=True)

    def Metal():
        verbose_name        = 'categoria'
        verbose_name_plural = 'categrorias'
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo    = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen    = models.CharField(null=True,blank=True,max_length=600)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now_add=True)
    autotor   = models.ForeignKey(User,models.CASCADE)
    categoria = models.ManyToManyField(Categorias)


    def Metal():
        verbose_name        = 'post'
        verbose_name_plural = 'posts'
    def __str__(self):
        return self.titulo

