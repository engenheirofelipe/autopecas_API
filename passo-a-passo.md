#   Configurar o ambiente

1.   Verificar a versão do python instalada ->  python --version
2.  Aplicar a pasta venv python -m venv venv
3.  Entrar em -> /venv/Scripts/activate.bat
4.  Instalar o Django -> pip install Django==5.0.3
5.  Criando o projeto -> django-admin startproject setup .
6.  Começar o projeto -> python manage.py startapp autopecas
7.  Na pasta setup, no arquivo setting.py ir em aplicativos instalados colocar o nome do projeto 'autopecas'
8.  language = pt-br,  UTC = America/Sao_Paulo

#   Começando com o json

1.  No arquivo view.py importar o jsonResponse para no momento que um usuário fazer o GET, 
no momento que o usuário entra na rota, passa a informação para pessoa -> from Django.httpm import jsonResponse.
2.  Função categorias -> def categorias(request)
                            if request.method == 'GET'
                            categoria = {
                                'id'= '1',
                                'nome'= 'Sistema de Suspensão'
                            }

                            return jsonResponse(categoria) -> Tranforma o dicionário escrito em python para formato json.

#   Criando a rota

1.  Dentro da pasta setup, abrir o arquivo urls.py
2.  Importar a view com o método criado -> from autopecas.views import categorias
3.  Dentro do URL patterns, colocar o path -> path('categorias/', categorias)

rodar python manage.py runserver

#   Instalar pacotes

1.  pip install djangorestframework
2.  pip install markdown       # Markdown support for the browsable API.
3.  pip freeze > requirements.txt
4.  colocar rest_framework em settings.py, INSTALLED_APPS 
5.  pip install django-filter  # Filtering support

*   API mais navegável


#   Criando models

*   Model é a representação da tabela do banco de dados.

1.  class Categoria(models.Model):
        nome = models.CharField(max_length = 100)
        

        def __str__(self):
            return self.nome 

2.  class Produto(models.Model):

        NIVEL = (
            'C':'Caro',
            'I':'Intermediario',
            'B':'Barato',
        )

        nome = models.CharField(max_length = 100)
        preco = models.CharField(blank = False, max_length = 10)
        quantidade = models.CharField(blank = False, max_length = 1000)
        descricao = models.CharField(blank = False)    
        nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False , null = False, default = 'I')       

        def __str__(self):
            return self.nome               

3.  Fazer as migrations -> python manage.py makemigrations
4.  Migrar -> python manage.py migrate 


#   Criar admin

1.  Fazer import das models -> from autopecas.models import Categoria, Produto
2.  Criar classe Categorias -> class Categorias(admin.ModelAdmin):
                                    list_display = ('id', 'nome')
                                    list_display_links = ('id')
                                    list_per_page = 20 # quantidade de categorias por pagina
                                    search_fields = ('nome',)

                                admin.site.register(Categoria, Categorias)

classe de Produtos
                                class Produtos(admin.ModelAdmin):
                                    list_display = ('id', 'nome', 'preco', 'quantidade', 'descricao', 'nivel')
                                    list_display_links = ('id', 'nome')
                                    search_fields = ('nome',)

                                admin.site.register(Produto,Produtos)


*   criar superusuario 

-> python manage.py createsuperuser

#   Iniciando Serializer

1.  Criar um arquivo serializer.py dentro do app autopecas

2.  No arquivo importar -> from rest_framework import serializer
3.  Importar ->from autopecas.models import Categoria, Produto

4.  Criar classes serializers :

    class CategoriaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Categoria
            fields = ['id', 'nome']
        

    class ProdutoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Produto
            fields = ['id', 'nome', 'preco', 'quantidade', 'descricao', 'nivel']

#   Construindo as viewsets

1.  No arquivo views.py importar ->  from autopecas.models import Categoria, Produto
                                ->  from autopecas.serializer import CategoriaSerializer,ProdutoSerializer
                                ->  from rest_framework import viewsets

2.  Fazer as classes 

CategoriaViewSet e ProdutoViewSet

from autopecas.models import Categoria, Produto
from autopecas.serializer import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

#   DefaultRouter

1.  Importar -> from rest_framework import routers
2.  Importar as viewsets, categoria e produto.
3.  criar o objeto router :
    router = routers.DefaultRouter()
    router.register('categorias', CategoriaViewSet, basename = 'Categorias')
    router.register('produtos', ProdutoViewSet, basename = 'Produtos')
    