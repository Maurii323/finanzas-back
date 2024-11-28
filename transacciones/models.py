from django.db import models
from django.contrib.auth.models import User    # User de django
from django.core.exceptions import ValidationError


# Categoria de la transaccion(ej: alimentos,varios,etc)
class Categoria(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)
    nombre = models.CharField(max_length=200, null=False, default="")
    descripcion = models.CharField(max_length = 500, blank=True, null=True)

# Transaccion(ingresos y costos)
class Transaccion(models.Model):
    user = models.ForeignKey(User,null = False, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=200, null=False)
    tipo = models.CharField(max_length=20, null=False)     # si es ingreso o costo
    categoria = models.ForeignKey(Categoria,null=True, on_delete=models.SET_NULL)
    monto = models.FloatField(null=False)
    descripcion = models.CharField(max_length = 500, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    # clean() se utiliza para realizar validaciones personalizadas
    def clean(self):
        super().clean()
        if self.monto <= 0:
            raise ValidationError({'monto': 'El monto debe ser un valor positivo.'})


    