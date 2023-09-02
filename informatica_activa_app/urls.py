from django.urls import path
from informatica_activa_app.views import *

urlpatterns = [
    path('',inicio,name='inicio'),
    path('tienda/',tienda),
   
    path('administracion/',administracion),
]
