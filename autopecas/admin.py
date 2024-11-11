from django.contrib import admin
from autopecas.models import Categoria, Produto

class Categorias(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    list_per_page = 20 # quantidade de categorias por pagina
    search_fields = ('nome',)

admin.site.register(Categoria, Categorias)

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade', 'descricao', 'nivel')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Produto,Produtos)

