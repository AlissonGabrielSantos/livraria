from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core import serializers

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
