from rest_framework.viewsets import ModelViewSet

from core import serializers
from core.models import Editora


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = serializers.EditoraSerializer
