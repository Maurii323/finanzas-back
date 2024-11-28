from rest_framework import serializers
from .models import Transaccion, Categoria

# serializer transforma datos en formatos fáciles de usar para la API cuando sea necesario(de JSON a Objeto Python y viceversa)
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria     #nombre del modelo
        # campos del modelo
        fields = ('id','nombre','descripcion')

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ('id','nombre','tipo','categoria','monto','descripcion')
        read_only_fields = ('fecha',)    # campos solo para leer, no se pueden actualizar ni eliminar
    
    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser un valor positivo.")
        return value