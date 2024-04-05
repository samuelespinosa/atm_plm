from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hola mundo cruel sopa")
# Create your views here.
