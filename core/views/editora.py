from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Editora
from core import serializers

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = serializers.EditoraSerializer
    permission_classes = [IsAuthenticated]
