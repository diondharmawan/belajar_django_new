"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse #Import Package Http
from django.contrib import admin
from django.urls import path

def index(request): #Mendefinisikan Index
    return HttpResponse("Hallo DUnia")

def blog(request):
    return HttpResponse("<h1>Ini adalah halamam BLog</h1>")


urlpatterns = [  
    path('', index),  #Merouting halaman index yang telah dibuat
    path('blog/',blog),
    path('admin/', admin.site.urls),
]
