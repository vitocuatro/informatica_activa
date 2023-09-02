
from django import forms


class Formulario_Autenticacion(forms.Form):
    nombre   = forms.CharField(label='Nombre',required=True)
    password = forms.CharField(label='Pasword',widget=forms.PasswordInput,required=True)