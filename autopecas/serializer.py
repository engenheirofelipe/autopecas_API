from rest_framework import serializers
from autopecas.models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Categoria
        fields = ['id', 'nome']
       

class ProdutoSerializer(serializers.ModelSerializer):

    categoria = CategoriaSerializer()

    class Meta:
        
        model = Produto
        fields = ['id', 'nome', 'preco', 'quantidade', 'descricao', 'nivel', 'categoria']


