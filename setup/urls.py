from django.contrib import admin
from django.urls import path, include
from autopecas.views import CategoriaViewSet, ProdutoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet, basename = 'categorias')
router.register('produtos', ProdutoViewSet, basename='produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
