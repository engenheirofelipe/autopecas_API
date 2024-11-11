#   Configurar o ambiente

1.   Verificar a versão do python instalada ->  python --version
2.  Aplicar a pasta venv python -m venv venv
3.  Entrar em -> /venv/Scripts/activate.bat
4.  Instalar o Django -> pip install Django==5.0.3
5.  Criando o projeto -> Django-admin startproject setup .
6.  Começar o projeto -> python manage.py startapp mecanica
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

                            

