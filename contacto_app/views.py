from django.shortcuts import redirect, render

from contacto_app.forms import Formulario_Contacto

# Create your views here.

def contacto(request):
    formulario_contacto = Formulario_Contacto()
    
    #if(request.method=="GET"):
   
    if(request.method=="POST"):
      formulario_contacto = Formulario_Contacto(data=request.POST)
      if formulario_contacto.is_valid():
       return redirect('/contacto/?es_valido')
    return render(request,'contacto.html',{'formulario_contacto':formulario_contacto})


    