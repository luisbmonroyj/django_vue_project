from http.client import HTTPResponse
from django.shortcuts import render

def index(request):
    return HTTPResponse('Esta es una prueba de impresion de index')

# Create your views here.
def detail(request, producto_id):
    return HTTPResponse("El id del producto: %s" % id_producto)

def results(request, producto_id):
    return HTTPResponse("Ordenes que tienen el producto: %s" % id_producto)

def vote(request, producto_id):
    return HTTPResponse("cantidad: %s" % id_producto)
