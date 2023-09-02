from django.contrib import admin

from blog.models import Categorias, Post

# Register your models here.

class Panel_Categorias(admin.ModelAdmin):
    readonly_fields=('created','updated')

class Panel_Post(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categorias,Panel_Categorias)
admin.site.register(Post,Panel_Post)
