from autopecas.models import Categoria, Produto
from autopecas.serializer import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    # Modificar a lógica de criação do Produto para aceitar o ID da categoria
    def perform_create(self, serializer):
        categoria_id = self.request.data.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)
        serializer.save(categoria=categoria)

