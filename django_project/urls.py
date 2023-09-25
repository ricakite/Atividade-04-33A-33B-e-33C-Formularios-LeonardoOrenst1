"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appdoleo import views


urlpatterns = [
  path('', views.home, name="home"),
  path('tenistas', views.create_tenistas),
  path('tenistas/update/<id>', views.update_tenistas),
  path('tenistas/delete/<id>', views.delete_tenistas),

  
  path('torneios', views.create_torneios),
  path('torneios/update/<id>', views.update_torneios),
  path('torneios/delete/<id>', views.delete_torneios),


  path('tabela', views.create_tabela),
  path('tabela/update/<id>', views.update_tabela),
  path('tabela/delete/<id>', views.delete_tabela),
  
  path('admin/', admin.site.urls)
]
