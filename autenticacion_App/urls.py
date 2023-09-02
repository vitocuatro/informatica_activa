

from django.urls import path

from autenticacion_App.views import Registro, cerrar_sesion, login_Usuario


urlpatterns = [
path('',Registro.as_view(),name='autenticacion'),   
path('cerrar_sesion',cerrar_sesion,name='cerrar_sesion'),
path('login_Usuario',login_Usuario,name='login_Usuario')
]