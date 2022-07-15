from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro
from core import serializers

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = serializers.AutorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = serializers.EditoraSerializer

class LivroGetViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = serializers.LivroGetSerializer

class LivroPutViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = serializers.LivroPutSerializer