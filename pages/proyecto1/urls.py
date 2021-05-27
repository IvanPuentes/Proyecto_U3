"""proyecto_vacaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from django.contrib import admin
from mipagina.views import HomePageView,TecView,RegistrarView,VueloPageView,HospedajePageView,DescripViajesPageView,DescripVuelosPageView,DescripHospPageView,ViajeDeleteView,AboutPageView
from django.views.generic.base import TemplateView
#rutas para los templates 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mipagina/', include('mipagina.urls')),
    path('mipagina/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('Home',HomePageView.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='vuelo.html'), name='vuelo'),
    path('vuelo',VueloPageView.as_view(), name='vuelo'),
    path('', TemplateView.as_view(template_name='hospedaje.html'), name='hospedaje'),
    path('hospedaje',HospedajePageView.as_view(), name='hospedaje'),
    path('Acerca_de', TemplateView.as_view(template_name='About.html'), name='About'),
    path('Acerca_de',AboutPageView.as_view(), name='About'),
    path('Tec',TecView.as_view(), name='tec'),
    path('registrar/', RegistrarView.as_view(),name='registrar'),
    path('Descripcion/Viajes/<int:pk>',DescripViajesPageView.as_view(),name='DescViajes'),
    path('Descripcion/Vuelos/<int:pk>',DescripVuelosPageView.as_view(),name='DescVuelos'),
    path('Descripcion/Hospedajes/<int:pk>',DescripHospPageView.as_view(),name='DescHosp'),
    path('Viaje/<int:pk>/delete',ViajeDeleteView.as_view(),name='deleteViaje'),
   
     
]