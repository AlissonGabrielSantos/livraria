from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core import serializers

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = serializers.EditoraSerializer
