# routers es un modulo que crea todas las rutas estandar de crud automaticamente
from rest_framework import routers
from .api import TransaccionViewSet, CategoriaViewSet

# crea las rutas del crud y lo guarda en una variable
router = routers.DefaultRouter()

# registra las rutas
router.register(r'finanzas/transaccion', TransaccionViewSet, basename='transaccion')
router.register(r'finanzas/categorias', CategoriaViewSet, basename='categoria')

# genera las urls
urlpatterns = router.urls