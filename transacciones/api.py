from .models import Transaccion, Categoria
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, TransaccionSerializer

# un viewSet nos permite quien puede acceder a un serializer(recurso) y que peticiones puede hacer
# proporciona métodos predefinidos para manejar un CRUD estandar, y se pueden agregar metodos personalizados

class CategoriaViewSet(viewsets.ModelViewSet):
    # que objetos se van a poder gestionar
    queryset = Categoria.objects.all()
    # quien tiene permitido acceder al recurso
    permission_classes = [permissions.AllowAny] # cualquiera puede acceder
    # serializer
    serializer_class = CategoriaSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    permission_classes = [permissions.AllowAny] # cualquiera puede acceder
    serializer_class = TransaccionSerializer

