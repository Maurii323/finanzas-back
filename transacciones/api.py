from .models import Transaccion, Categoria
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, TransaccionSerializer

# un viewSet nos permite quien puede acceder a un serializer(recurso) y que peticiones puede hacer
# proporciona métodos predefinidos para manejar un CRUD estandar, y se pueden agregar metodos personalizados

class CategoriaViewSet(viewsets.ModelViewSet):
    # quien tiene permitido acceder al recurso
    permission_classes = [permissions.IsAuthenticated] # Solo pueden acceder usuarios autenticados
    # serializer
    serializer_class = CategoriaSerializer

    # modifica el queryset(define qué registros de la base de datos deben ser accesibles) que se va a usar
    def get_queryset(self):
        # Devuelve las categorías del usuario autenticado o las generales(user=None).
        
        user = self.request.user
        # Trae las categorías del usuario autenticado y las categorías generales
        return Categoria.objects.filter(usuario=user) | Categoria.objects.filter(usuario__isnull=True)
    
    # modifica como va a crear el recurso
    def perform_create(self, serializer):
        # Asegura que la tarea creada se asocie al usuario autenticado
        serializer.save(user=self.request.user)

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.filter()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransaccionSerializer

    def get_queryset(self):
        #Devuelve las categorias relacionadas con el usuario autenticado.
        user = self.request.user 
        return Categoria.objects.filter(user=user)  # Filtra las tareas por el usuario
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

