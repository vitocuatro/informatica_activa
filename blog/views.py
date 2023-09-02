from django.shortcuts import render

from blog.models import Categorias, Post

# Create your views here.

def blog(request):
    posts      = Post.objects.all()
    categorias = Categorias.objects.all()
    return render(request,'blog.html',{'posts':posts,'categorias':categorias})

def categoria(request,id):
    categorias = Categorias.objects.get(id=id)
    posts      = Post.objects.filter(categoria=categorias)
    enlaces    = Categorias.objects.all()
    
    return render(request,'categoria.html',{'posts':posts,'categorias':categorias,'enlaces':enlaces})