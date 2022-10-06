from rest_framework.viewsets import ModelViewSet

from core import serializers
from core.models import Autor


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = serializers.AutorSerializer