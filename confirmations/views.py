from rest_framework import viewsets
from .models import Confirmations
from .serializers import ConfirmationsSerializer

class ConfirmationsViewSet(viewsets.ModelViewSet):
    queryset = Confirmations.objects.all()
    serializer_class = ConfirmationsSerializer
