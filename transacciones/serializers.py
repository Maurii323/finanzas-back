from rest_framework import serializers
from .models import Transaccion, Categoria

# serializer transforma datos en formatos fáciles de usar para la API cuando sea necesario(de JSON a Objeto Python y viceversa)
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria     #nombre del modelo
        # campos del modelo
        fields = ('id','user','nombre','descripcion')

class TransaccionSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)  # Usa el serializador de Categoria para mostrar detalles

    class Meta:
        model = Transaccion
        fields = '__all__'
        read_only_fields = ('fecha',)

    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser un valor positivo.")
        return value