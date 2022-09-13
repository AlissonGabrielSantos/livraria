from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core import serializers

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = serializers.AutorSerializer
