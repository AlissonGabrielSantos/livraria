from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core import serializers
from core.models import Categoria


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [IsAuthenticated]
