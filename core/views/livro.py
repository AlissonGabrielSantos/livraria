from rest_framework.viewsets import ModelViewSet

from core import serializers
from core.models import Livro


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.LivroDetailSerializer
        return serializers.LivroSerializer