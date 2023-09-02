from django.contrib import admin
from .models import Servicio

# Register your models here.
class Servico_Admin(admin.ModelAdmin):
    readonly_fields = ('created','update')
admin.site.register(Servicio,Servico_Admin)