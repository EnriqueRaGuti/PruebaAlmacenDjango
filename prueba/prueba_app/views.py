from django.shortcuts import render

from rest_framework import generics

from prueba_app.models import Producto
from prueba_app.serializers import ProductoSerializer 
# Create your views here.

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
# Create your views here.
