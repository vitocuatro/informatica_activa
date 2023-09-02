

from django.urls import path

from blog.views import blog, categoria

urlpatterns = [
path('categoria/<int:id>/',categoria,name='categoria'),    
path('',blog), 
]