from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'editoras', views.EditoraViewSet)
router.register(r'livroget', views.LivroGetViewSet)
router.register(r'livroput', views.LivroPutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
