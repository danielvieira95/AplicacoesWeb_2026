"""
URL configuration for loja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet

def home(request):
    return HttpResponse("Olá Django ! Aplicações Web 2026 - 2 Aula 03 - Loja de produtos")

router = DefaultRouter()
router.register(r'produtos',ProdutoViewSet, basename= 'produto')

urlpatterns = [
    path('', home),
    path('admin/',admin.site.urls),
    path('api/', include(router.urls))
   
]
