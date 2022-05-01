# Movie API 
API que provê um serviço de filmes e series, onde apresenta os seguintes dados: nome, overview, nota do imdb, data de lançameto, gênero, uma imagem de capa, e no caso das series, a quantidade de teporadas. 

## Endpoints
```
/api/genres/ - Lista todos os gêneros dos filmes, permite cadastrar novos gêneros
```

```
/api/movies/ - Lista todos os filmes cadastrados com suas respictivas informações, e permite o cadastro de novos filmes.

/api/movies/{id} - Lista um filme pelo id.

/api/movies/?name=nome do filme - Retorna uma lista com todos os filmes que contenham em seu nome o nome passado na query name.
```

```
/api/series/ - Lista todas as séries, e permite o cadastro de novas séries.

/api/series/{id} - Lista uma série pelo id.

/api/series/?name=nome da serie - Retorna uma lista com todos as séries que contenham em seu nome o nome passado na query name.
```

## Executando a aplicação
- Crie um ambiente virtual e ative
```
python -m venv venv
source /venv/bin/activate (linux)
/venv/script/activate (windows)
```
- Instale as dependências
```
pip install -r requirements
```
- Execute as migrations para o banco de dados
```
python manage.py migrate
```
- Caso queira, execute os testes.
```
python manage.py test
```
- Caso também queira ver a cobertura dos testes, instale a seguinte biblioteca e execute o comando.
```
pip install coverage
coverage run manage.py test
coverage report
```
- Executar aplicação.
```
python manage.py runserver
```
Para testar api no browser, acesse os endpoints listados acima.

Acesse `/docs/` ou `/redoc/` para ver a documentação da API com seus schemas de dados, podendo também, testar os endpoints com o primeiro.

## Frameworks e Bibliotecas
- [Django](https://www.djangoproject.com/)
- [Django REST](https://www.django-rest-framework.org/)
