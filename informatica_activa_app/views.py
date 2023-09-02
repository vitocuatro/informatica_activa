from django.http import HttpResponse
from django.shortcuts import render

from srviciosapp.models import Servicio




# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def tienda(request):
    return render(request,'tienda.html')
def administracion(request):
    return render(request,'administracion.html')