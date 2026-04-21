"""
URL configuration for JungleBros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.views.generic.base import RedirectView as Redirecione
from home import views as pg_inicial
from login import views as pg_login
from pg_final import views as pg_final

urlpatterns = [
    path('home/', pg_inicial.home, name = 'home'),
    path('', Redirecione.as_view(url = '/home/')),
    path('login/', pg_login.login, name = 'login'),
    path('pagina_final/', pg_final.pg_final, name = 'pagina_final'),
]
