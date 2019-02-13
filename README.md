# Crawler 
[![Build Status](https://travis-ci.org/Guilehm/crawler.svg?branch=master)](https://travis-ci.org/Guilehm/crawler)

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
    

# Exemplo de resposta formatada
```json
{
    "feed": [
        {
            "item": {
                "title": "Honda CG 125 se despede depois de 42 anos em linha e mais de sete milhões de unidades vendidas",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/honda-cg-125-se-despede-depois-de-42-anos-em-linha-e-mais-de-sete-milhoes-de-unidades-vendidas.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/sZqUGH3xECWEqH0oPypDqwy4tLs=/620x413/e.glbimg.com/og/ed/f/original/2016/08/11/honda_cg_125_i_fan_2016_719ac26289.jpg"
                    },
                    {
                        "type": "text",
                        "content": "AHondaCG 125foi descontinuada depois de ficar 42 anos em produção. A moto criada para ser um veículo urbano prático, e com bom custo benefício, foi por muitos anos a moto mais vendida no Brasil, comsete milhões de unidades comercializadas entre 1976 e 2019."
                    },
                    {
                        "type": "text",
                        "content": "Os motivos para a descontinuação vão damudança do perfil do motociclistabrasileiro ao longo desses anos. Hoje, grande parte dos antigos clientes mudaram para o segmento dos scooters (práticos, econômicos e modernos). Outro fator importante foi aobrigação de renovar a frota das motoscom a implementação de freios ABS (ou combinados do tipo CBS) – melhoria que a marca resolveu não investir."
                    },
                    {
                        "type": "text",
                        "content": "Isso sem falar na queda das vendas. Em 2018, por exemplo,a CG 125 vendeu “apenas” 28.401 exemplares. Ficando em sétimo lugar no ranking das mais vendidas do país."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/10-motos-mais-vendidas-de-2018.html",
                            "https://revistaautoesporte.globo.com/Videos/noticia/2018/10/video-por-que-honda-cg-vende-tanto.html",
                            "https://revistaautoesporte.globo.com/Analises/noticia/2016/12/honda-cg-completa-40-anos.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "História"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/zhBXzCPu2B7ZMAflEjr8DTA8TVk=/620x413/e.glbimg.com/og/ed/f/original/2016/12/02/cg_125_1976.jpg"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Volkswagen convoca recall de 1.225 unidades do Tiguan Allspace por falha elétrica",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/volkswagen-tiguan-allspace-recall-falha-eletrica-1225-unidades.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/mKjrL506xLEkj4U9zik3BxA7jEk=/620x413/e.glbimg.com/og/ed/f/original/2018/04/27/mgbf3479.jpg"
                    },
                    {
                        "type": "text",
                        "content": "AVolkswagen do Brasilanunciou nesta terça-feira (05) que algumas unidades doTiguan Allspaceprecisam passar por um recall para substituir o chicote elétrico do carro. Isso porque uma falha nos conectores dessa peças podem causar curto-circuito, com risco de incêndio, em casos extremos. No total, 1.225 carros fazem parte deste recall."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2015/08/guia-de-recall-tudo-o-que-voce-precisa-saber-antes-de-consertar-seu-carro.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/volkswagen-do-brasil-tera-que-recomprar-194-carros-experimentais-por-venda-irregular.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Segundo a montadora, a falha afeta o Tiguan Allspaceano/modelo 2018, fabricados entre 27 de outubro de 2017 e 22 de junho de 2018. A numeração de chassi (não-sequencial) varia de JM067487 a JM183498. A falha afeta o sistema de iluminação interna."
                    },
                    {
                        "type": "text",
                        "content": "A substituição do chicote elétrico leva cerca de 4 horas e 30 minutos para ser concluída e o processo é feito gratuitamente, conforme previsto em lei. Os proprietários do Volkswagen Tiguan Allspace devem entrar em contato com a empresa pelo telefone 0800 019 8866."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/procon-pede-esclarecimentos-volkswagen-por-recall-inusitado.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/volkswagen-e-multada-em-mais-r-72-milhoes-por-conta-do-dieselgate-no-brasil.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/wEHUFFRUSFsP8RO6KEKm4uhiEG8=/620x413/e.glbimg.com/og/ed/f/original/2018/04/27/mgbf3488.jpg"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Fim das autobahns: Alemanha estuda acabar com as estradas sem limite de velocidade",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/fim-das-autobahns-alemanha-estuda-acabar-com-estradas-sem-limite-de-velocidade.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/baWelXB7vi0ewA-PLu_M8E-MwfI=/e.glbimg.com/og/ed/f/original/2019/02/05/autobahn.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O governo alemão está estudando propostas para limitar a velocidade dos carros nos diversos segmentos “livres” das rodovias do país, a contragosto dos motoristas. Asautobahnssão famosas no mundo todo por permitirem que seus usuários façam uso de toda a escala do velocímetro sem o risco de multas ou punições."
                    },
                    {
                        "type": "text",
                        "content": "Não sabia disso? Pois é isso mesmo: em determinados trechos das vias expressas, é possível dirigir em altas velocidades sem criar problemas com a lei. Porém, uma discussão recente pretende impor barreiras à agulha do mostrador, limitando os veículos a máxima de 130 km/h."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/7UgT2OyqNy9-19Cf5sNDWhzXht8=/e.glbimg.com/og/ed/f/original/2019/02/05/autobahn1.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Com a adoção de veículos elétricos, Paris, por exemplo, já prevê o banimento de carros a combustão até 2025. Na terra deMichael Schumacher, Sebastian VetteleWalter Röhrl, as estradas sem limite de velocidade são tradicionais e, de certa forma, um símbolo nacional, como a Oktoberfest, a Bratwurst e o Apfelstrudel."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/r7skx5_CU2Cxs8QTRARodQnu9p4=/e.glbimg.com/og/ed/f/original/2019/02/05/autobahn5.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Naquele país, o governo não interfere nas decisões sobre o pedal direito alheio por realmente entender que o motorista é responsável pelas escolhas que faz. Eles têm três características que não temos aqui: 1) de fato o condutor entender que faz parte de um sistema integrado e que suas ações interferem na vida dos outros, 2) as regras de trânsito são cumpridas à risca e os infratores são punidos e 3) o treinamento de motoristas é rigoroso."
                    },
                    {
                        "type": "text",
                        "content": "A primeiraautobahnsurgiu em 1932, antes da Segunda Guerra, portanto, período que contou com restrições à população com o intuito de economizar combustível por causa do conflito. É por isso que mesmo cidadãos sêniores, homens e mulheres de cabelos totalmente brancos, se irritam profundamente quando alguém trava a pista da esquerda a 140 km/h. Essa atitude é uma das raras que fazem os alemães perderem a compostura."
                    },
                    {
                        "type": "text",
                        "content": "Como a regra é a mesma, imutável, e universalmente respeitada a três gerações, ninguém se atreve a alugar a pista rápida para cruzar o país. Lá, a faixa mais à esquerda da via é exclusiva para ultrapassagens. Na Alemanha, o controle de velocidade é, paradoxalmente, extremamente rigoroso em áreas urbanas. O controle é fiscalizado por radares, majoritariamente."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/os-carros-mais-legais-que-equipe-da-autoesporte-dirigiu-em-2018.html",
                            "https://revistaautoesporte.globo.com/testes/noticia/2018/02/teste-nova-ferrari-portofino-esportivo.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Mesmo com as estradas sem imposição de limite de velocidade, o índice de mortes no trânsito é baixíssimo, com registro de 4,3 mortes por 100.000 habitantes. No Brasil, a taxa é de 23,4 fatalidades a cada 100.000 pessoas. A média mundial é de 17,4. O país com o pior índice é a Líbia, com 73,4 mortes em 100.000 cidadãos."
                    },
                    {
                        "type": "text",
                        "content": "Mais um bônus para você que está invejando os alemães: não há cobrança de pedágios nas estradas da Alemanha. Durma com essa."
                    }
                ]
            }
        }
    ]
}
```
