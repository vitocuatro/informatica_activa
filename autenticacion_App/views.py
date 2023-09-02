from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import View


# Create your views here.
class Registro(View):
    

    def get(self,request):
        form = UserCreationForm()
        return render(request,'autenticacion.html',{'form': form})
    def post(self,request):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            usuario = form.save()
            login(request,usuario)
            return redirect('inicio')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                return render(request,'autenticacion.html',{'form': form})
            
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')
def login_Usuario(request):
    if(request.method =='POST'):
       form = AuthenticationForm(request,data=request.POST)
       if(form.is_valid()):
           nombre_Usuario = form.cleaned_data.get('username')
           password       = form.cleaned_data.get('password')
           usuario        = authenticate(username=nombre_Usuario, password = password)
           if(usuario is not None):
               login(request,usuario)
               return redirect('inicio')
           else:
               messages.error(request,'Usuario no válido')
       else:
            messages.error(request,'Información incorecta')   
    form = AuthenticationForm()
    return render(request,'login_Usuario.html',{'form':form})
