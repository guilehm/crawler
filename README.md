# Crawler

---
# Exemplo em produção para testes
[https://gui-crawler.herokuapp.com/](https://gui-crawler.herokuapp.com/)

# Visão Geral

* API Rest
* Documentações da API [Swagger](https://gui-crawler.herokuapp.com/swagger/), [Redoc](https://gui-crawler.herokuapp.com/redoc/)
* Django
* Docker
* Testes automatizados utilizando Pytest
* Integração contínua com Travis-CI
* Utilização do Isort e Flake8
* Construção do projeto documentada utilizando Git com criação de Issues e Pull Requests
* Deploy no Heroku com PostgreSQL

# Requisitos
* Python (3.6)
* Django (2.1)

# Informações gerais
* O arquivo principal do scrapper está neste link [https://github.com/Guilehm/crawler/blob/master/utils.py](https://github.com/Guilehm/crawler/blob/master/utils.py)
* Os testes podem ser encontrados em [https://github.com/Guilehm/crawler/tree/master/api/tests](https://github.com/Guilehm/crawler/tree/master/api/tests)
* Para facilidade dos usuários, deixei o projeto flexível para ser opcional rodar com Docker.

# Instalação

Clone este repositório

    $ git clone https://github.com/Guilehm/crawler.git

Entre no diretório

    $ cd crawler

Instale o pipenv* (opcional, caso queira pode utilizar o virtualenv, criei o arquivo requirements.txt)

    $ pip install pipenv

Crie o ambiente virtual

    $ pipenv install

Ative o ambiente virtual

    $ pipenv shell

OBS.: Caso queira rodar o projeto utilizando o Docker, pule para a próxima seção.

Crie o banco de dados

    $ python manage.py migrate


Inicie o servidor

    $ python manage.py runserver

O servidor estará rodando em [http://localhost:8000/](http://localhost:8000/).


# Instalação com Docker

É necessário ter o Docker instalado em sua máquina.
Recomendo este tutorial de instalação para o Linux [https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-18-04-pt)

Após ter concluído as etapas anteriores e estar com o serviço do Docker rodando, execute:


    $ docker-compose up
    
Neste ponto o app deverá estar rodando em [http://localhost:8000](http://localhost:8000), mas ainda temos que fazer algumas coisas.

Liste os contêineres

    $ docker container ls
    
Procure pelo contêiner chamado `crawler_web_1` e copie seu ID

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
cda44253a6a9        crawler_web         "python3 manage.py r…"   About an hour ago   Up 19 seconds       0.0.0.0:8000->8000/tcp   crawler_web_1

```
    
Acesse o bash do contêiner com o seguinte comando:

    $ docker exec -it <id_do_conteiner> bash

    
E crie o banco de dados:

    $ python manage.py migrate

    
Finalizamos :)


# Utilização

Crie seu usuário em [http://localhost:8000/accounts/signup/](http://localhost:8000/accounts/signup/)

Faça um POST em [http://localhost:8000/api/token/](http://localhost:8000/api/token/) com o seguinte payload

```json
{
	"username": "<seu_usuario>",
	"password": "<seu_password>"
}
```

Anote seu Token
```json
{
    "token": "5fd7ce97ec265cb2483b18670001a915b0a65dad"
}
```

O endpoint [http://localhost:8000/api/feed/detail/](http://localhost:8000/api/feed/detail/) só é acessível para usuários cadastrados e com Token.

Faça um GET em [http://localhost:8000/api/feed/detail/](http://localhost:8000/api/feed/detail/) e envie seu token no headers no formato descrito abaixo
```
Authorization: Token 5fd7ce97ec265cb2483b18670001a915b0a65dad
```

Caso não queira autenticar, disponibilizei um endpoint sem restrição de acessos: [http://localhost:8000/api/feed/detail/no-auth/](http://localhost:8000/api/feed/detail/no-auth/)

Criei também um endpoint que salva a resposta em um arquivo `.json` devidamente formatado para uma melhor visualização da resposta:
[http://localhost:8000/api/feed/detail/save/](http://localhost:8000/api/feed/detail/save/)

# Testes

O Projeto está em Integração Contínua com o [TravisCI](https://travis-ci.org/) e todos os testes são executados em todos commits antes de irem para branch master.

Para executar os testes localmente:

Verifique se os imports estão ordenados corretamente

    isort
    
Verifique se o código está em ordem

    flake8

Execute os testes

    pytest -vv
    
Ou rode todos de uma só vez

    make test
