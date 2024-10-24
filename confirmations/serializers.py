from rest_framework import serializers
from .models import Confirmations

class ConfirmationsSerializer(serializers.ModelSerializer):
    mensaje = serializers.CharField(read_only=True, default='')

    class Meta:
        model = Confirmations
        fields = ['familia', 'mensaje']  # Incluye el campo de mensaje

    def validate_familia(self, value):
        # Verificar si el valor de 'familia' ya existe en la base de datos
        if Confirmations.objects.filter(familia=value).exists():
            self.fields['mensaje'].default = "El valor de familia ya existe."  # Ajustar el mensaje
        return value

