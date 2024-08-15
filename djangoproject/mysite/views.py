from django.http import HttpResponse #Import Package Http
from django.shortcuts import render #Import Render Template Django



def index(request): #Mendefinisikan Index
    return HttpResponse("Hallo DUnia")

def index1(request): #Mendefinisikan Index
    return render(request, 'index.html')

def blog(request):
    return HttpResponse("<h1>Ini adalah halamam BLog</h1>")