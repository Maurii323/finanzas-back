from django.db import models
from django.contrib.auth.models import User    # User de django


# Categoria de la transaccion(ej: alimentos,varios,etc)
class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)
    nombre = models.CharField(max_length=200, null=False, default="")
    descripcion = models.CharField(max_length = 500)

# Transaccion(ingresos y costos)
class Transaccion(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,null = False, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=200, null=False)
    tipo = models.CharField(max_length=20, null=False)     # si es ingreso o costo
    categoria = models.ForeignKey(Categoria,null=False, on_delete= models.CASCADE)
    monto = models.FloatField(null=False)
    descripcion = models.CharField(max_length = 500)
    fecha = models.DateTimeField(auto_now_add=True)


    