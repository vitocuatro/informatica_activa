



from django.urls import path

from contacto_app.views import contacto


urlpatterns = [
 path('',contacto,name='contacto'),  

]