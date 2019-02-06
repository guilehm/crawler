# Crawler [![Build Status](https://travis-ci.org/Guilehm/crawler.svg?branch=master)](https://travis-ci.org/Guilehm/crawler)

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
                        "content": "https://s2.glbimg.com/8Fnigx0pfGbrjTAFTqo09G0vNno=/620x413/e.glbimg.com/og/ed/f/original/2016/12/02/honda_cg_125_today_1989.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A história da CG 125 se confunde com a própria história da montadora japonesa no Brasil."
                    },
                    {
                        "type": "text",
                        "content": "- Aprimeira geração(1976 a 1982) marcou a chegada das motos japonesas ao Brasil. E em 1981 veio a primeira motocicleta do mundo equipada com um motor a álcool.- Asegunda geração(1983 a 1988) trouxe linhas mais retas e em 1985 vieram os faróis retangulares e câmbio de cinco marchas.- Com a chegada daterceira geração(1989 a 1994) a linha ganhou a versão “Today”, com alterações de design, no painel e no assento. Em 1991, vieram muitas modificações que incluíram alterações estruturais inclusive no quadro e no motor.- A configuração “Titan viria com a apresentação daquarta geração(1994 a 1999). O modelo apresentava design novamente renovado, e trazia atualizações de freios, embreagem, além de melhorias na parte elétrica.- Naquinta geração(2000 a 2003) a Titan ganhou opção de versões com partida elétrica, ou a pedal, e com freio a disco ou a tambor.- De 2004 a 2009 veio asexta geração. Foi quando a 125 começou a perder espaço para a nova integrante da família, a CG 150. Período em que a irmã mais potente já começava a dominar o mercado.- Asétima geração(2009 a 2013) trouxe os incrementos de injeção eletrônica, novos chassis e versões flex de motorização.- Aoitava e atual geração(2013 até hoje) modernizou muito a aparência da CG. Além das mudanças estruturais em design e chassi, o motor também recebeu atualizações que, segundo a montadora, deixaram a motocicleta com melhor desempenho."
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
                        "content": "Como era de se esperar, o debate está superaquecido entre a população motorizada, que não está disposta a aliviar o pé em nome da qualidade do ar (que, na Alemanha, não é ruim).A alegação do governo é que as emissões de gases oriundos do transporte não caem desde os anos 90, apesar do aumento de eficiência energética dos automóveis. Individualmente os carros estão mais limpos, porém a frota nacional crescente relativiza o ganho tecnológico."
                    },
                    {
                        "type": "text",
                        "content": "AADAC, principal clube de automobilismo alemão, já se posicionou contra a medida, e a organização representa os interesses de pelo menos 20 milhões de integrantes. Atualmente, cerca de 30% dos 12.900 quilômetros de rodovias já têm restrições aos pé-de-chumbo, porém nenhuma delas relacionadas ao que sai do escapamento. Onde há limites, existem razões de segurança ou por conta de proximidade com áreas densamente populosas – o que requer a redução das emissões de ruídos."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/H0t2hFYSqQXDGiQz1xbRqPQDnhA=/e.glbimg.com/og/ed/f/original/2019/02/05/autobahn3.jpg"
                    },
                    {
                        "type": "text",
                        "content": "As discussões acerca da proibição de velocidades insanas ainda estão em estágio preliminar, mas devem estar finalizadas até março (eles são alemães, gente). Fóruns governamentais de toda a união europeia discutem a redução de poluentes e a Alemanha é signatária de vários acordos, inclusive o de reforçar os requisitos legais para a homologação de novos veículos."
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
        },
        {
            "item": {
                "title": "Volkswagen é multada em mais R$ 7,2 milhões por conta do Dieselgate no Brasil",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/volkswagen-e-multada-em-mais-r-72-milhoes-por-conta-do-dieselgate-no-brasil.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/yi_ib9tkJHj76-cFfwOw6bT5JUg=/620x413/e.glbimg.com/og/ed/f/original/2015/09/11/volkswagen-amarok-12.jpg"
                    },
                    {
                        "type": "text",
                        "content": "AVolkswagen do Brasilfoi multada novamente nesta semana emR$ 7,2 milhõespor conta do episódio conhecido comoDieselgate. A decisão é da Secretaria Nacional do Consumidor, órgão ligado ao Ministério da Justiça e Segurança Pública, que considerou que a montadora \"violou a boa-fé que o fornecedor deve buscar nas relações de consumo\". A montadora pode recorrer em um prazo de 10 dias."
                    },
                    {
                        "type": "text",
                        "content": "Segundo nota divulgada pela Senacon, a multa foi aplicada \"em razão de uso de software que otimizava as emissões de óxidos de nitrogênio durante os testes laboratoriais, a fim de alterar os resultados sobre a emissão de poluentes\". O caso afeta17.057 unidades da picapeAmaroka diesel, que foram vendidas no Brasil como ano/modelo 2011 (totalmente) e 2012 (parcialmente)."
                    },
                    {
                        "type": "text",
                        "content": "O órgão de defesa do consumidor argumenta que \"o consumidor não poderia supor que existia a adulteração, configurando a violação da boa-fé que o fornecedor deve buscar nas relações de consumo\". Em todo o mundo, diferentes marcas do grupo Volkswagen comercializaram cerca de 11 milhões de carros com este dispositivo que altera os índices de emissões durante os testes."
                    },
                    {
                        "type": "text",
                        "content": "A Senacon considera que \"o dever de transparência é manifestado por meio da clareza das informações prestadas aos consumidores, o que deve ser buscado em todas as etapas da relação consumerista. Assim, não se pode induzir o consumidor a crer que adquiriria um veículo com redução da emissão de poluentes quando tal informação não apresentasse relação exata com a realidade\"."
                    },
                    {
                        "type": "text",
                        "content": "Em resposta àAutoesporte, a Volkswagen afirma que o caso daAmarokno Brasil é diferente do que acontece em outros países. Segundo a empresa, \"o software não otimiza os níveis de emissões de NOx das picapesAmarokcomercializadas no mercado brasileiro com o objetivo de atender os limites legais. Portanto, o os carros envolvidos atendem a legislação brasileira mesmo antes dos softwares serem removidos destes carros\"."
                    },
                    {
                        "type": "text",
                        "content": "A montadora não detalha os testes que apontariam que o dispositivo não está ativo nas picapes vendidas no Brasil.Em abril de 2016,Autoesporterevelou detalhes do documento enviado pela montadora ao Ministério da Justiça com essas informações. Nele, a empresa afirma que asAmarok2011 testadas emitem de 0,7 g/km a 0,8 g/km de óxido de nitrogênio, menos do que o índice permitido pela legislação da época (1,0 g/km)."
                    },
                    {
                        "type": "text",
                        "content": "Já o laudo divulgado pelo Ibama aponta que \"se não fosse pela ação do dispositivo, as emissões de óxidos de nitrogênio superariam o limite regulamentado e, portanto, os veículos teriam sido reprovados nos testes\". Segundo este documento,as Amarok testadas emitiriam, em média, 1,101 g/km, índice acima do permitido. Uma estimativa do órgão aponta que as 17 mil Amarok juntas emitiriam no meio-ambiente 100 toneladas de poluentes a mais do que o permitido."
                    },
                    {
                        "type": "text",
                        "content": "Em novembro de 2015,a montadora foi multada em R$ 50 milhõespelo Ibama por conta do mesmo caso. A Volkswagen recorreu e ainda não há uma decisão final. Já o Procon multou a empresa em R$ 8,3 milhões. Na Justiça,a companhia foi condenada em primeira instância a pagar um total de R$ 1 bilhãoaos consumidores que adquiriram alguma das unidades das Amarok envolvidas nesse caso."
                    },
                    {
                        "type": "text",
                        "content": "Processo administrativo sobre suposta venda casada"
                    },
                    {
                        "type": "text",
                        "content": "Além da multa, o órgão decidiu abrir novo processo administrativo contra a Volkswagen e o Consórcio Nacional Volkswagen – Administradora Consórcio Ltda. para apurar uma denúncia feita pelo Banco Central do Brasil. O objetivo é apurar indícios de \"suposta prática de venda casada, consistente na obrigatoriedade da contratação de seguros de vida, prestamista ou de quebra de garantia quando da aquisição de cotas de consórcio\"."
                    },
                    {
                        "type": "text",
                        "content": "Caso seja comprovado que a prática \"viola a liberdade de contratação do consumidor por condicionar a aquisição de um produto ou serviço a outro\", as empresas poderão ser multadas em até R$ 9,7 milhões. Ambas têm prazo de 10 dias para apresentar defesa sobre o caso."
                    },
                    {
                        "type": "text",
                        "content": "Leia a íntegra do posicionamento da Volkswagen sobre a multa da Senacon"
                    },
                    {
                        "type": "text",
                        "content": "“No Brasil, o tema Diesel difere de outros mercados, uma vez que o software não otimiza os níveis de emissões de NOx das picapes Amarok comercializadas no mercado brasileiro com o objetivo de atender os limites legais. Portanto, o os carros envolvidos atendem a legislação brasileira mesmo antes dos softwares serem removidos destes carros."
                    },
                    {
                        "type": "text",
                        "content": "Em 2017, a Volkswagen convocou os modelos Amarok para substituir o software da unidade de comando eletrônico do motor visando retomar a confiança dos consumidores. O recall foi iniciado em 3 de maio de 2017 e envolve um total de 17.057 veículos."
                    },
                    {
                        "type": "text",
                        "content": "Com relação à sansão divulgada nessa segunda-feira (4 de fevereiro), a Volkswagen tomou conhecimento pelo Diário Oficial da União e entrará em contato com o DPDC para entendimento das razões da decisão.”"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Toyota em quarto lugar, Renegade líder dos SUVs e Onix implacável: o primeiro balanço de vendas de 2019",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/toyota-em-quarto-lugar-renegade-lider-dos-suvs-e-onix-implacavel-o-primeiro-balanco-de-vendas-de-2019.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/5bdy9tZZsu1O-dt1jdJ58u-3X6g=/620x413/e.glbimg.com/og/ed/f/original/2019/02/05/logos-mercado-chevrolet-toyota-jeep-2019.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O ano de 2019 está apenas começando, mas o balanço de vendas de janeiro mostra que teremos disputas intensas em várias frentes.O líder geralChevrolet Onixsegue implacável, tal como se manteve ao longo de 2018. Já no primeiro mês do ano, o hatch acumula mais que o dobro de emplacamentos do segundo colocado, oFord Ka.Mas o Onix é exceção.O ranking indica que a briga será travada mês a mês, unidade a unidade."
                    },
                    {
                        "type": "text",
                        "content": "Uma boa disputa no topo de tabela será entreVolkswagen PoloeFiat Argo, rivais diretos e referências atuais entre os compactos premium. Na luta por volume, oFord Kadeve enfim levar vantagem sobre oHyundai HB20, queserá renovado no segundo semestre. Já entre os sedãs, oChevrolet Prisma(tal como o irmão Onix) mantém a soberania e aparece isolado na frente. OVolkswagen Virtus, segundo colocado, vendeu quase a metade."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/--KRnncWFBu5m8FYVVMgL-7aV6s=/620x413/e.glbimg.com/og/ed/f/original/2018/10/16/trailhawk_089.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A disputa mais quente continua entre os SUVs. Depois de ficar na terceira colocação na categoria em 2018, oJeep Renegadesurpreendeu e foi o líder de vendas em janeiro, com boa folga em relação ao irmão maiorCompass, segundo colocado. E vejam só, oHyundai Creta, que foi líder entre os compactos no ano passado, foi apenas o quinto utilitário mais emplacado em janeiro, atrás deNissan Kickse (o outrora líder)Honda HR-V."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/c2xSTj7Xb8wvN_rtZhz4_0v_Yuk=/620x413/e.glbimg.com/og/ed/f/original/2018/08/20/mg_7397.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Entre as montadoras, janeiro foi um mês histórico para aToyota.A marca japonesa ficou com a quarta colocação geral, que tradicionalmente pertence à Ford. A liderança segue nas mãos daGeneral Motors, mesmo com toda apolêmica envolvendo o futuro da empresa no país.VolkswageneFiatmantém a segunda e terceira posições."
                    },
                    {
                        "type": "text",
                        "content": "O miolo de tabela será o mais acirrado, sem dúvida.Basta ver que Ford, Renault e Toyota venderam 16 mil unidades cada uma. O equilíbrio entre os fabricantes continua realmente impressionante, e aHyundaitambém aparece próxima do pelotão, com 13,5 mil emplacamentos. Outros destaques sãoCitroëneChery, ambas começam 2019 bem."
                    },
                    {
                        "type": "text",
                        "content": "Confira abaixo os 50 carros mais vendidos de janeiro:"
                    },
                    {
                        "type": "text",
                        "content": "1º)Chevrolet Onix— 18.842 unidades2º)Ford Ka— 8.023 unidades3º)Hyundai HB20— 7.249 unidades4º)Chevrolet Prisma— 6.924 unidades5º)Volkswagen Polo— 5.433 unidades6º)Renault Kwid— 5.336 unidades7º)Volkswagen Gol— 4.966 unidades8º)Fiat Argo— 4.920 unidades9º)Fiat Strada— 4.790 unidades10º)Jeep Renegade— 4.783 unidades11º)Fiat Mobi— 4.413 unidades12º)Jeep Compass— 4.109 unidades13º)Volkswagen Fox— 4.085 unidades14º)Toyota Corolla— 4.075 unidades15º)Fiat Toro— 4.033 unidades16º)Honda HR-V— 3.667 unidades17º)Renault Sandero— 3.650 unidades18º)Volkswagen Virtus— 3.591 unidades19º)Nissan Kicks— 3.486 unidades20º)Toyota Hilux— 3.257 unidades21º)Hyundai Creta— 3.236 unidades22º)Toyota Yaris hatch— 2.890 unidades23º)Volkswagen Saveiro— 2.849 unidades24º)Ford Ecosport— 2.798 unidades25º)Ford Ka sedã— 2.685 unidades26º)Volkswagen Voyage— 2.645 unidades27º)Fiat Cronos— 2.577 unidades28º)Renault Captur— 2.557 unidades29º)Chevrolet S10— 2.183 unidades30º)Honda Fit— 2.101 unidades31º)Hyundai HB20S—  2.068 unidades32º)Toyota Yaris sedã— 2.027 unidades33º)Chevrolet Spin— 1.970 unidades34º)Renault Duster— 1.911 unidades35º)Honda Civic— 1.840 unidades36º)Nissan Versa— 1.795 unidades37º)Fiat Uno— 1.758 unidades38º)Fiat Grand Siena— 1.664 unidades39º)Chevrolet Cruze— 1.611 unidades40º)Ford Ranger— 1.531 unidades41º)Chevrolet Tracker— 1.514 unidades42º)Volkswagen Amarok— 1.431 unidades43º)Toyota Etios hatch— 1.313 unidades44º)Honda City— 1.229 unidades45º)Toyota SW4— 1.187 unidades46º)Fiat Fiorino— 1.134 unidades47º)Toyota Etios sedã— 1.129 unidades48º)Renault Logan— 1.078 unidades49º)Renault Duster Oroch— 1.028 unidades50º)Citroën C4 Cactus— 1.016 unidades"
                    },
                    {
                        "type": "text",
                        "content": "Veja também oranking das montadoras (com participação nas vendas) em janeiro:"
                    },
                    {
                        "type": "text",
                        "content": "1º)General Motors— 36.215 unidades (18,99%)2º)Volkswagen— 28.057 unidades (14,71%)3º)Fiat— 26.166 unidades (13,72%)4º)Toyota— 16.396 unidades (8,60%)5º)Renault— 16.346 unidades (8,57%)6º)Ford— 16.250 unidades (8,52%)7º)Hyundai— 13.591 unidades (7,12%)8º)Honda— 9.888 unidades (5,18%)9º)Jeep— 8.912 unidades (4,67%)10º)Nissan— 6.506 unidades (3,41%)11º)Citroën— 2.074 unidades (1,09%)12º)Peugeot— 1.746 unidades (0,92%)13º)Mitsubishi— 1.633 unidades (0,86%)14º)Mercedes-Benz— 1.172 unidades (0,61%)15º)Chery— 998 unidades (0,52%)16º)Kia Motors— 885 unidades (0,46%)17º)Audi— 768 unidades (0,40%)18º)BMW— 708 unidades (0,37%)19º)Volvo— 485 unidades (0,25%)20º)Land Rover— 442 unidades (0,23%)"
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/os-carros-mais-vendidos-de-2018.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/toyota-corolla-segue-na-lideranca-como-carro-mais-vendido-do-mundo-em-2018.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/top-50-os-carros-mais-vendidos-de-2018.html"
                        ]
                    }
                ]
            }
        },
        {
            "item": {
                "title": "MItsubishi L200 reestilizada chega em 2020 com tecnologias para peitar S10 e Ranger",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/mitsubishi-l200-reestilizada-chega-em-2020-com-tecnologias-para-peitar-s10-e-ranger.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/cRhiKACLhyRQGOUIkbUZgDfh5LQ=/620x413/e.glbimg.com/og/ed/f/original/2018/11/09/tritonfrentao.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A Mitsubishi começou a vender a L200 Triton Sport reestilizada em outros mercados, um ciclo de lançamentos que ainda inclui outros países. Porém o Brasil ainda vai demorar um pouco para receber a novidade. A picape média reformada será lançada por aqui apenas no final de 2020."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/11/mitsubishi-l200-triton-e-reestilizada-no-exterior-mas-ainda-vai-demorar-chegar.htm",
                            "https://revistaautoesporte.globo.com/Analises/noticia/2016/09/teste-mitsubishi-l200-triton-sport-24-turbodiesel.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/11/mitsubishi-apresenta-novo-pajero-sport-para-peitar-chevrolet-trailblazer-e-toyota-sw4.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "O desenho do modelo foi registrado no Instituto Nacional de Propriedade Industrial (INPI), prática que garante a propriedade intelectual sobre qualquer produto. Não raro, fabricantes registram automóveis, utilitários e motos que sequer serão lançados no nosso mercado."
                    },
                    {
                        "type": "text",
                        "content": "Não é o caso da picape Mitsubishi. A previsão de chegada para o segundo semestre do ano que vem era esperada, uma vez que a L200 de nova geração demorou um pouco mais para chegar ao Brasil. Ela foi lançada em setembro de 2016, quase um ano depois do lançamento estrangeiro."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/Whoz3FBU2NA7iUrLU17uxvHOMpc=/620x413/e.glbimg.com/og/ed/f/original/2019/02/05/screenshot_20190205-113446_drive.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O visual ousado é ainda mais rebuscado do que o visto na Pajero Sport. Os faróis auxiliares e principais são divididos e há luzes de LEDs por todas as partes. As lanternas também passaram a ser blocadas e ostentam filetes verticais como os aplicados no SUV."
                    },
                    {
                        "type": "text",
                        "content": "A mecânica manteve o motor 2.4 turbodiesel (190 cv e 43,9 kgfm), mas passou a contar com um novo câmbio automático de seis marchas, face o antigo de cinco velocidades. A tração integral ganhou sistema de gerenciamento eletrônico com cinco modos de funcionamento (cascalho, lama/neve, areia e rocha)."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/HAa266ltkxBvf1IHm1voi8gfglI=/620x413/e.glbimg.com/og/ed/f/original/2019/02/05/mitsubishi-l200-2019_2.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Para se destacar em um segmento cercado de picapes tecnologicamente avançadas, exemplos da Chevrolet S10 e Ford Ranger, a L200 Triton Sport recebeu novos itens de condução semiautônoma, ponto que a atual fica devendo."
                    },
                    {
                        "type": "text",
                        "content": "Há detector de pedestres e de tráfego à frente, capaz de parar a picape automaticamente se necessário. Além disso, foram incorporados alerta de ponto cego e de tráfego cruzado, que alerta caso tenha carros passando na hora em que você aciona a ré."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jvbYLfUh9TH8Emp0VFHoqoh3oTk=/620x413/e.glbimg.com/og/ed/f/original/2018/11/30/l_2.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Nas horas das manobras, momento sempre sensível em veículos deste tamanho, o sistema Ultrasonic Misacceleration Mitigation System (UMS) detecta acelerações indevidas no estacionamento. É uma forma de não danificar a L200 ou, pior, algum carrinho nos arredores. A Triton traz ainda câmera de 360 graus."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Volkswagen Golf GTI encarece R$ 5.500",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/volkswagen-golf-gti-encarece-r-5500.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/TfZG2S8nTUqnanduE61CWKE-HsA=/620x413/e.glbimg.com/og/ed/f/original/2018/06/15/honda-civic-si-versus-vw-golf-gti-autoesporte-2018-02.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Se você achou que, porque oGolftinhaescapado do aumento de preços de início de ano da Volkswagen, o preço do modelo ficaria igual por muito tempo, temos uma má notícia - e das grandes.O começo de fevereiro de 2019 trouxe um encarecimento significativo para a versão topo de linha do carro, o esportivoGolf GTI. O hatch médio, que era vendido por R$ 143.790 até mês passado,agora custa R$ 149.290, ou seja,está R$ 5.500 mais caro."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/testes/noticia/2018/06/comparativo-volkswagen-golf-gti-encara-o-honda-civic-si.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/volkswagen-jetta-gli-com-motor-de-golf-gti-sera-lancado-em-fevereiro-de-2019.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/volkswagen-golf-gti-ganha-versao-de-290-cv-na-europa.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "O modelo, quejá tinha um preço mais salgado do que a versão intermediária do Golf- a TSI Highline, deR$ 112.190-, agora ampliou ainda mais essa distância. Considerando os preços atualizados,a diferença de valor de uma versão para a outra é de R$ 37.100."
                    },
                    {
                        "type": "text",
                        "content": "E se você não quer nem pensar na possibilidade do preço doGolfGTI acabar maior ainda, fique bem longe da lista de opcionais, acessórios e cores disponíveis para o carro. Para ter um hatch esportivo decor metálica, contabilize maisR$ 1.820. Paracor perolada, então, tem que desembolsar ainda mais:R$ 2.285. E que tal umteto solar panorâmico por R$ 4.985? Se tudo isso ainda não for o bastante, ainda existe a opção de adicionar aoGolf GTIumPacote Sport, deR$ 6.125, que inclui ajuste da altura dos bancos, apoio lombar ajustável eletricamente e revestimentos dos bancos parcialmente em couro."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/wq1PRTYIfD1Vl7jnf3q69fWx6FM=/620x413/e.glbimg.com/og/ed/f/original/2018/06/15/honda-civic-si-versus-vw-golf-gti-autoesporte-2018-05.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Mas tem mais: existe a opção doPacote Premium, deR$ 9.550. Ele inclui ajuste de distância automático, assistente de estacionamento, assistente para luz alta, farol principal com LED com luz para trânsito em curvas, Front Assist inclusive de freio de emergência automático para trânsito na cidade e reconhecimento de cansaço.A soma de tudo isso? R$ 172.235- mais de R$ 7 mil a mais do que o cobrado peloPassat, sedã premium da marca alemã (atualmente vendido por R$ 164.620)."
                    },
                    {
                        "type": "text",
                        "content": "OVWGolf GTI é aversão mais potente do modelo disponível no mercado brasileiro. Ele é o único da linha commotor 2.0- e também a única das três versões disponíveis que é movida apenas à gasolina. Ele é capaz de entregar220 cv de potência e torque de 35,7 kgfm. Já ocâmbio é automático de seis velocidades."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Executivo da Mercedes-Benz é o novo presidente da Anfavea até 2022",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/executivo-da-mercedes-benz-e-o-novo-presidente-da-anfavea-ate-2022.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/h81iT3WEO0ySisgkhtV01_wj3Ok=/e.glbimg.com/og/ed/f/original/2018/04/03/luiz-carlos-moraes--4.jpg"
                    },
                    {
                        "type": "text",
                        "content": "AAnfavea, associação que reúne os fabricantes de veículos no Brasil, conseguiu articular um acordo para indicar uma chapa única para a eleição da sua nova direção. Dessa forma, a organização terá como próximo presidente o diretor de comunicação e relações institucionais daMercedes-Benz do Brasil,Luiz Carlos Moraes."
                    },
                    {
                        "type": "text",
                        "content": "Moraes, que irá suceder o atual presidente,Antônio Megale, terá como vice em sua chapaFabricio Biondo, vice-presidente de comunicação, relações externas e digital doGrupo PSA(PeugeotCitroën) na América Latina. O mandato dos próximos líderes da Anfavea é de três anos e compreende o períodoentre 2019 e 2022."
                    },
                    {
                        "type": "text",
                        "content": "A posse dos novos comandantes da entidade acontecerá no próximo dia 23 de abril, quando Megale completa três anos de mandato. Moraes acumulará, simultaneamente, a presidência do Sindicato Nacional da Indústria de Tratores, Caminhões, Automóveis e Veículos Similares (Sinfavea).A escolha de Moraes e Biondo quebra uma tradição de revezamento entre cinco marcas ao longo da história da entidade. Quando Fiat, Ford, GM, Mercedes-Benz e Volkswagen nomeavam, em chapa única, os presidentes e vices da Anfavea."
                    },
                    {
                        "type": "text",
                        "content": "Se o processo de transição fosse mantido da forma como vinha acontecendo há anos, com a indicação de uma chapa única, o esperado é que Rogelio Golfarb, vice-presidente de estratégia da Ford América do Sul, fosse eleito presidente da Associação, uma vez que é o atual vice-presidente da organização. E o futuro presidente, Moraes, seria o seu vice."
                    },
                    {
                        "type": "text",
                        "content": "Mas, não é de hoje que outras marcas também pleiteiam poder concorrer ao cargo mais alto da Anfavea. Por isso, na última eleição surgiu outra chapa com Ricardo Martins, gerente de assuntos corporativos da Hyundai Motor Brasil, saindo como candidato a presidente. Ele comporia uma administração com Fabricio Biondo, como seu vice."
                    },
                    {
                        "type": "text",
                        "content": "No final, os diretores da Anfavea chegaram a um consenso e a aliança dissidente concordou em desistir do pleito. E dessa forma o processo se deu com candidatos únicos para a eleição deste ano."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Beber e dirigir? A ciência pode\nmudar esse comportamento",
                "link": "https://revistaautoesporte.globo.com/Publicidade/Heineken/noticia/2019/02/beber-e-dirigir-ciencia-pode-mudar-esse-comportamento.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/uoJcN2s2apBj14A5PXRcu61f0HA=/e.glbimg.com/og/ed/f/original/2019/02/04/fotos_mariana_pekin__94a2662.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Imagine entrar em um bar repleto de pequenos “empurrõezinhos” para os motoristas não beberem antes de dirigir. Nas paredes, no balcão e até no espelho do banheiro, cartazes e adesivos com mensagens alertando sobre a perigosa combinação. Na mesa, petiscos de cortesia para quem assinar um juramento se comprometendo a não beber naquela noite. Tem mais: um cardápio especial com caprichados drinques sem álcool para a turma do volante. Diante de tantos estímulos, você deixaria de ingerir bebidas alcoólicas antes de dirigir?"
                    },
                    {
                        "type": "text",
                        "content": "A Heineken decidiu tirar isso à prova. Em parceria com a consultoria especializada InBehavior Lab, a marca realizou um experimento social pioneiro no Brasil utilizando conceitos e técnicas das ciências comportamentais para conscientizar e mudar o hábito dos motoristas que misturam álcool e direção. A estratégia foi distribuir em 18 bares das cidades de São Paulo e Porto Alegre diferentes tipos dos chamados nudges, como os cartazes e o cardápio de drinques não alcoólicos."
                    },
                    {
                        "type": "text",
                        "content": "Sem tradução exata para o português, o nudge pode ser definido como um “leve empurrãozinho” no contexto de tomada de decisão. “Eles são uma das principais ferramentas utilizadas pelos praticantes e pesquisadores da área comportamental e têm como objetivo promover um determinado resultado ao trabalhar a arquitetura da escolha e aspectos conscientes e inconscientes do comportamento humano, sem modificar a estrutura dos incentivos ou limitar a escolha do indivíduo”, explica Flávia Ávila, CEO da InBehavior Lab. “A ideia é usar os nudges para o bem e para melhorar a vida das pessoas”, completa."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jw1OGvRB92J1Ht5m25o3t8ZuLoA=/e.glbimg.com/og/ed/f/original/2019/02/04/fotos_mariana_pekin__94a2249.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Base científica"
                    },
                    {
                        "type": "text",
                        "content": "Cada intervenção realizada nos bares pela Heineken foi baseada em vieses e propensões do ser humano estudadas pela economia comportamental. As peças gráficas com mensagens de alerta e incentivo, por exemplo, tinham o objetivo de acionar no cérebro o chamado sistema 2 (devagar, analítico, racional) em detrimento do sistema 1 (rápido, emocional, sujeito a erros e vieses) e fazer os motoristas refletirem sobre as consequências do ato de beber antes de dirigir."
                    },
                    {
                        "type": "text",
                        "content": "Já ao facilitar o acesso a drinques sem álcool, dribla-se o processo normal do cérebro de ignorar aquilo que não está rapidamente disponível, para economizar recursos cognitivos. Dessa forma, ter o cardápio especial à mão diminui o custo mental de pensar em alternativas para bebidas alcoólicas. Além disso, há o efeito social: ao ver outras pessoas bebendo esses drinques e se divertindo, os motoristas se sentem encorajados a fazer o mesmo."
                    },
                    {
                        "type": "text",
                        "content": "Fazer parte de um grupo também foi o princípio-chave para a colocação nos bares de um mural no qual foram dispostos todos os cartões do “juramento do motorista”, assinados por aqueles que se comprometiam a não beber naquela noite. Este estímulo ajuda na tendência de assumir um comportamento que reflete o que é aceitável. A ideia é que, ao ver o mural, os motoristas que desejassem permanecer abstêmios passassem a perceber essa conduta como “normal” e com suporte social."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/IdXS4Jyr10pFjyN1R0EI7fwVki8=/e.glbimg.com/og/ed/f/original/2019/02/04/fotos_mariana_pekin__94a2350.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Adaptações para o Brasil"
                    },
                    {
                        "type": "text",
                        "content": "Realizado inicialmente na Inglaterra, em dez pubs das cidades de Reading e Manchester, o experimento teve modificações para a aplicação em terras brasileiras. Os times da Heineken e da InBehavior estudaram as diferenças culturais entre os dois países para adaptar os nudges de acordo com a nossa cultura. Nesse processo, foram realizadas entrevistas com 81 consumidores e testada a compreensão das peças criadas. As informações dessa etapa ajudaram os pesquisadores a definir os “empurrõezinhos” mais efetivos para a ação no Brasil."
                    },
                    {
                        "type": "text",
                        "content": "A primeira semana do experimento foi dedicada à fase chamada controle. Observadores visitaram os locais, entrevistaram 427 motoristas e avaliaram o consumo e o comportamento real dos frequentadores sem as intervenções da marca. Essa etapa forneceu os dados de comparação para a segunda fase, agora com os bares sinalizados com os nudges. Entre os dias 17 e 19 de outubro, foram entrevistadas 460 pessoas e constatada uma redução de 25,2% no número de motoristas que beberam e dirigiram. Os efeitos da ação foram maiores dentro do grupo de menores de 32 anos de idade, e entre as mulheres. A pesquisa avaliou ainda que, nos bares mais engajados, a cada 100 motoristas, 35 foram impactados a não consumir álcool naquela noite."
                    },
                    {
                        "type": "text",
                        "content": "Os resultados obtidos reforçam a eficácia dos nudges e a importância deste recurso para as ciências comportamentais. “O avanço da economia comportamental e suas descobertas sobre tendências do comportamento humano e muitos dos vieses utilizados pelos indivíduos em suas decisões têm proporcionado novos espaços e ferramentas para um dos maiores desafios atuais do mundo: gerar ações concretas e mudar comportamentos”, diz Ávila."
                    },
                    {
                        "type": "text",
                        "content": "“É realmente impressionante analisar como eles agem de forma inconsciente em nossa mente e incentivam mudanças positivas”, diz Vanessa Brandão, diretora da marca Heineken. “Estamos muito orgulhosos de mergulhar em um projeto que vai além de uma ação tradicional de marketing e consumo consciente. Esperamos que os resultados do experimento atraiam ainda mais a atenção para este tema e inspirem diferentes empresas a promover ‘empurrões’ que beneficiem seus consumidores de alguma forma.”"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Volkswagen T-Cross já está à venda na Europa; confira os preços",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/volkswagen-t-cross-ja-esta-venda-na-europa-confira-os-precos.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/aVWH4AmoWwgSNunUYSRVOF0p41o=/620x413/e.glbimg.com/og/ed/f/original/2018/10/30/volkswagen_t-cross__2_.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Ainda faltam algumas semanas para o início das vendas doVolkswagen T-Crossno mercado brasileiro, e cresce a expectativa para saber quais preços o SUV terá. No fim de outubro,Autoesporte apurou que o modelo deve custarentre R$ 90 mil e R$ 120 mil. Na ocasião, uma fonte apontou os valores. Agora,já é possível configurar o utilitário no site de alguns países. Na Alemanha, o T-Cross parte de cerca de R$ 75 mil."
                    },
                    {
                        "type": "text",
                        "content": "No site alemão da VW, o SUV aparece disponível em três versões.A básica (apenas \"T-Cross\") custa a partir de 17.975 euros, o equivalente a R$ 75,5 mil na conversão direta. O intermediário Life tem valor sugerido de 20.075 euros (algo como R$ 84,3 mil), eo topo de linha Style vai de 23.700 euros (R$ 99,6 mil) a 28.995 euros com todos os opcionais que estavam em oferta — são R$ 121,7 mil na cotação do dia."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/2019-sera-sacudido-pelos-suvs-uma-onda-que-inclui-t-cross-santa-fe-e-tiggo-7.html",
                            "https://revistaautoesporte.globo.com/Blogs/noticia/2018/10/opiniao-como-o-volkswagen-t-cross-promete-liderar-o-segmento-de-suvs-compactos.html",
                            "https://revistaautoesporte.globo.com/Videos/noticia/2018/11/video-novo-volkswagen-t-cross-honda-hr-v-turbo-e-outros-suvs-do-salao-de-sao-paulo.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/e-1-pnJ_bx75GOQSDjXYNaTWujY=/620x413/e.glbimg.com/og/ed/f/original/2018/10/30/volkswagen_t-cross__3_.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Os valores, claro, não incluem taxas. É o preço do T-Cross europeu, produzido na Espanha. Para quem ainda não conhece o SUV, haverá muitas diferenças entre o daqui e o de lá. Como o Brasil não terá oT-Roc, utilitário derivado do Golf, o T-Cross nacional (feito sobre a base modular da dupla Polo e Virtus) tem o entre-eixos maior, para ampliar o espaço na cabine. Os modelos também guardam diferenças de design exterior e mecânica."
                    },
                    {
                        "type": "text",
                        "content": "No mercado alemão, o utilitário está disponível apenas com o motor 1.0 TSI a gasolina em duas faixas de potência: 95 cv ou 115 cv. Este pode vir associado a câmbios manuais de cinco e seis marchas, ou a transmissão automática DSG de dupla embreagem e sete marchas. A tração é sempre dianteira, mas, opcionalmente, há um controle nas versões automáticas com quatro ajustes eletrônicos, incluindo um modo para o off-road."
                    },
                    {
                        "type": "text",
                        "content": "No Brasil, o T-Cross terá opções de motores 1.0 turbo e 1.4 turbo, ambos flex e referenciados pelas novas nomenclaturas — 200 TSI e 250 TSI. O 1.0 (até 128 cv) é o mesmo usado por Polo e Virtus, e será associado a câmbios manual de cinco marchas e automático de seis velocidades, enquanto o 1.4 de até 150 cv será sempre automático.A tração também é dianteira e haverá o mesmo programa de ajustes de condução."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/zt9JmKXBk1SNGXGMeQDyWtr_fwM=/620x413/e.glbimg.com/og/ed/f/original/2018/10/30/volkswagen_t-cross__7_.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O T-Cross básico deverá ser o Trendline 200 TSI manual, com preço pouco abaixo dos R$ 90 mil estimados inicialmente. Como parâmetro, o HR-V 2019 parte de R$ 92.500, enquanto o Renegade Sport 1.8 têm iniciais de R$ 78.490 (manual) e R$ 83.990 (automático). Mais acima virá o Comfortline 200 TSI automático, seguido do Comfortline 250 TSI — sim, o 1.4 turbo estará na configuração intermediária. Seu preço deve ficar na casa dos R$ 110 mil."
                    },
                    {
                        "type": "text",
                        "content": "No topo virá o T-Cross Highline 250 TSI, que é o modelo das fotos. Este deve partir de R$ 115 mil e vai superar os R$ 120 mil, tal como a versão europeia.Completo, o T-Cross ficará emparelhado com a versão de acesso do Tiguan, entre R$ 125 mil e R$ 130 mil. Se aHondanão pegar pesado com a futura versão turbo doHR-V, o T-Cross deve se tornar oSUV compacto mais caro do mercado. Se bem que oJeep Renegadetem valor sugerido de R$ 139.990 na versão 4x4 Trailhawk a diesel. Pedreira..."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/volkswagen-t-cross-aparece-com-motores-turbo-e-boas-tecnologias-mas-nao-e-referencia-em-porta-malas.html",
                            "https://revistaautoesporte.globo.com/Analises/noticia/2018/10/teste-vw-t-cross-14-tsi-suv-com-motor-de-golf-e-porte-de-hrv-ecosport.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/5-coisas-que-mudam-no-volkswagen-t-cross-nacional-em-relacao-ao-europeu.html",
                            "https://revistaautoesporte.globo.com/testes/noticia/2019/02/exclusivo-aceleramos-o-volkswagen-tarek-futuro-rival-do-jeep-compass-que-sera-lancado-no-brasil-em-2020.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/volkswagen-amarok-v6-picape-mais-rapida-que-um-golf-turbo.html"
                        ]
                    }
                ]
            }
        },
        {
            "item": {
                "title": "GNV fica 40,1% mais caro",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/preco-do-gnv-fica-401-mais-caro.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/SMj30cuwGPHb_8CM57U7nHGFpeo=/top/e.glbimg.com/og/ed/f/original/2017/03/23/084_085_ae623-01.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Essa não é uma boa notícia para quem colocou okit gásno carro para economizar. Desde sexta-feira (1/02), o preço do GNV ficou 40,1% mais caro em São Paulo, na Grande Campinas, na Baixada Santista e no Vale do Paraíba. A Agência Reguladora de Saneamento e Energia do Estado de São Paulo (Arsesp) divulgou a nova tabela de preços do gás natural fornecido pela Comgás (Companhia de Gás de São Paulo)."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/testes/noticia/2018/08/testamos-o-audi-a5-g-tron-que-tem-gnv-de-fabrica.html",
                            "https://revistaautoesporte.globo.com/Noticias/cbn/noticia/2017/04/boletim-cbn-autoesporte-kit-gnv-exige-manutencao-constante-para-manter-seguranca.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "A mudança também atinge consumidores residenciais: os aumentos variaram de 9,63% para a faixa mais baixa de consumo e vai até 17,93% para o perfil de gasto mais alto. Os clientes comerciais tiveram reajustes entre 12%, para os que tem menor consumo, até 25% para a faixa mais alta. As indústrias também vão pagar entre 24,1% e 37,6% mais caro pelo gás.De acordo com a Comgás, o que teria motivado a alta de 40,1% no combustível seria uma “atualização do custo do gás natural, que reflete variações de preço do petróleo e da taxa de câmbio, e não impacta as margens da companhia, que permanecem inalteradas\", afirmou em comunidado."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "GM pretende investir R$ 10 bilhões no Brasil até 2024, apesar da alegação de prejuízo no país",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/gm-pretende-investir-r-10-bilhoes-no-brasil-ate-2024-apesar-da-alegacao-de-prejuizo-no-pais.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/fQppkDvV16IVQi1Z4sBNBH-CWjw=/e.glbimg.com/og/ed/f/original/2015/06/12/gm.jpg"
                    },
                    {
                        "type": "text",
                        "content": "AGeneral Motors do Brasildivulgou mais um comunicado, desta vezsobre os planos de investimento da montadora até 2024, no Brasil. A nota divulgada no último sábado (2) chega dias depois que o presidente da GM Mercosul, Carlos Zarlenga,fez um anúncio para os funcionários de fábricas brasileiras da fabricante."
                    },
                    {
                        "type": "text",
                        "content": "Confira a íntegra do texto direcionado à imprensa, com os esclarecimentos da GM"
                    },
                    {
                        "type": "text",
                        "content": "“A GM está concluindo o plano de investimento de R$ 13 bilhões no período de 2014 a 2019. A GM está negociando condições de viabilidade para o novo e adicional investimento de R$ 10 bilhões no período de 2020 a 2024. Caso as negociações tenham sucesso, a GM investiria R$ 23 bilhões entre 2014 e 2024 (R$ 13 bilhões de 2014 a 2019 e R$ 10 bilhões de 2020 a 2024).O plano de investimento que está sendo concluído, no total de R$ 13 bilhões de 2014 a 2019, contempla: renovação completa da linha de produtos Chevrolet. Desenvolvimento de novas tecnologias de eficiência energética dentro do Programa INOVAR Auto.Ressaltando que a GM alcançou neste processo os melhores resultados do programa, com uma média de economia de combustível de 22% na linha, muito superior à média do mercado, que foi de 15,9%. Novas tecnologias de conectividade incluindo a nova geração do sistema multimídia MyLink e o sistema de telemática OnStar.Expansões nas fábricas de São Caetano do Sul e de Gravataí. Ampliação da fábrica de Joinville, que teve a capacidade elevada de 120 mil para 450 mil motores por ano. Implementação de inovadoras tecnologias de manufatura 4.0 nas fábricas de São Caetano do Sul, Gravataí e Joinville."
                    },
                    {
                        "type": "text",
                        "content": "Estes investimentos levaram a marca Chevrolet à liderança do mercado, posição que mantém desde outubro de 2015.\"Como líderes de mercado, estamos assumindo a responsabilidade de encarar de frente os desafios de competividade que vive a indústria para viabilizar um futuro sustentável aos nossos negócios e o devido retorno aos acionistas.Continuamos trabalhando com os sindicatos, concessionários, fornecedores e governo com o objetivo de viabilizar este novo e adicional investimento de R$ 10 bilhões nas fábricas de São Caetano do Sul e São José dos Campos\", ressalta Carlos Zarlenga, presidente da GM Mercosul.”"
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/afinal-carros-compactos-sao-lucrativos-ou-nao-para-os-fabricantes.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/os-4-erros-que-fizeram-chevrolet-pensar-em-sair-do-brasil-e-o-que-ela-pretende-fazer-agora.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/opiniao-rede-chevrolet-e-que-mais-vende-carros-por-loja-confira-o-ranking-exclusivo.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Em Gravataí"
                    },
                    {
                        "type": "text",
                        "content": "Na última sexta-feira (1),a fabricante informou que desistiu das 21 reivindicações que havia feito no início da semana no sentido de reduzir custos trabalhistas. Diminuindo o piso salarial de novos trabalhadores, e a participação nos lucros, bem como alterando a jornada de trabalho. A decisão se aplica apenas à unidade de Gravataí (RS) da General Motors. Na ocasião, o Sindicato local comemorou a decisão. Contudo, a exemplo de outras montadoras no país, o momento da Chevrolet no país é de atenção."
                    },
                    {
                        "type": "text",
                        "content": "Apesar do anúncio sobre os investimentos, para tentar diminuir seus custos, a empresa iniciou um processo de negociação e de flexibilizações trabalhistas com os sindicatos dos metalúrgicos das cidades de São Caetano do Sul (SP) e São José dos Campos (SP). E também com Governos de alguns Estados da Federação.À administração paulista, por exemplo, foi solicitado a antecipação de créditos acumulados no ICMS. Enquanto ao Estado do Rio Grande do Sul, a montadora pediu o retorno da isenção no ICMS cobrado sobre o frete interestadual, e diminuição dos custos de exportação a partir do Porto de Rio Grande.As tratativas começaram depois que a empresa divulgou comunicado interno afirmando que a operação estava dando prejuízo no Brasil, há três anos, o que foi interpretado como uma sinalização de que a marca poderia deixar de produzir no país, caso não voltasse a ter lucro em 2019."
                    },
                    {
                        "type": "text",
                        "content": "A voz do Sindicato"
                    },
                    {
                        "type": "text",
                        "content": "Depois de ter recusado a propsota da GM de reduzir salários e direitos trabalhistas, o Sindicato dos Metalúrgicos de São José dos Campos divulgou nota em que diz unir trabalhadores de diversas categorias para barrar a retirada de direitos proposta pela General Motors no Brasil. No comunicado, o representante da categoria diz que nas próximas semanas essa será a principal tarefa das entidades que integram o Brasil Metalúrgico. O grupo se reuniu na sexta-feira (1), na sede do Sindicato dos Metalúrgicos de São Paulo."
                    },
                    {
                        "type": "text",
                        "content": "“Essa grave ameaça da GM afeta toda cadeia produtiva de automóveis. Por isso, o Brasil Metalúrgico organiza hoje essa reunião ampliada”, afirmou Miguel Torres, vice-presidente da Força Sindical, durante a abertura da reunião."
                    },
                    {
                        "type": "text",
                        "content": "Para os participantes, a montadora faz chantagem ao ameaçar deixar a América Latina, caso não volte a ter lucros. Além disso, ao pressionar pela retirada de direitos, a GM atua como ponta de lança da implementação da reforma trabalhista no Brasil."
                    },
                    {
                        "type": "text",
                        "content": "Ao final da reunião, os participantes aprovaram a produção de um jornal dedicado à população para explicar, segundo o Sindicato, os impactos negativos que o plano de reestruturação da montadora pode causar na sociedade."
                    },
                    {
                        "type": "text",
                        "content": "Como tudo começou"
                    },
                    {
                        "type": "text",
                        "content": "Em 18 de janeiro o presidente da GM Mercosul, Carlos Zarlenga, enviou um comunicado para os funcionários de fábricas brasileiras da montadora com trechos de uma reportagem do  jornalThe Detroit News, sobre entrevista com a presidente global, Mary Barra. E as notícias não eram boas."
                    },
                    {
                        "type": "text",
                        "content": "O comunicado preocupou o Sindicato dos Metalúrgicos de São José do Campos, e região. Para o jornal norte-americano, Mary Barra poderia estar indicando que deixaria a América Latina, caso o quadro não se revertesse. \"Barra deu sinais de que a GM está considerando sair da América do Sul\", e \"não vamos continuar investindo para perder dinheiro\", escreveu o Detroit News. A informação foi divulgada primeiramente pelo jornal \"O Estado de S.Paulo\"."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/os-4-erros-que-fizeram-chevrolet-pensar-em-sair-do-brasil-e-o-que-ela-pretende-fazer-agora.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "No mesmo comunicado,Carlos Zarlenga disse que a GM teve um prejuízo agregado significativo no Brasil no período entre 2016 e 2018, que não poderia se repetir. “2019 será um ano decisivo para nossa história”, afirmou o executivo.Tudo indica que a GM está estudando condições para viabilizar este plano de investimentos no país, até 2024. A estratégia poderá depender não apenas de investimentos, mas também de incentivos e até de mudança de estratégia de market share e de linha de produção."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Teste: Mini Cooper John Cooper Works prova que a tração dianteira também pode ser divertida",
                "link": "https://revistaautoesporte.globo.com/Analises/noticia/2019/02/teste-mini-cooper-john-cooper-works-prova-que-tracao-dianteira-tambem-pode-ser-divertida.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/kpueKOXkuoXrX7OMgDVVc4BOfD0=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/p90331924_highres_mini-john-cooper-wor_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Em um fim de semana de janeiro, fui com onovo Mini Cooper John Cooper WorksConversível a um casamento na Serra da Cantareira, que fica ao norte da cidade de São Paulo. A boa notícia: consegui testar o desempenho do carro nas subidas íngremes do caminho. A má: eu tinha prometido dar carona a um casal de amigos."
                    },
                    {
                        "type": "text",
                        "content": "Mesmo tendo visto o modelo só por fotos, eu já imaginava que um Mini duas portas não seria espaçoso e confortável para eles, ainda mais de vestido e salto, terno e sapato. Dito e feito! Foi difícil acomodar duas pessoas de 1,80 metro nos bancos de trás, que ficam praticamente encostados nos da frente."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/flagra-mini-eletrico-e-visto-rodando-camuflado-na-alemanha.html",
                            "https://revistaautoesporte.globo.com/testes/noticia/2019/02/exclusivo-aceleramos-o-volkswagen-tarek-futuro-rival-do-jeep-compass-que-sera-lancado-no-brasil-em-2020.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Apesar da minha preocupação, o aperto não pareceu ter incomodado. Na verdade, eu não pensava que um carro pudesse gerar tantas perguntas curiosas. A primeira? O preço: R$ 201.990."
                    },
                    {
                        "type": "text",
                        "content": "Expliquei que oMinivinha da Inglaterra e que era o mais caroJohn Cooper Works, equipado com um 2.0 turbo de 231 cv entre 5.200 e 6.200 rpm e 32,6 kgfm a 1.250 rpm. No caso do hatch fechado (mais leve), o zero a 100 km/h leva apenas 5,8 segundos. É a primeira vez que o Cabrio tem opção JCW."
                    },
                    {
                        "type": "text",
                        "content": "Falei de uma das grandes novidades: o câmbio automático de oito marchas. Até a linha anterior, todas as versões eram equipadas com câmbio automático de seis velocidades. A manopla, inclusive, também é nova, em forma de joystick."
                    },
                    {
                        "type": "text",
                        "content": "As trocas manuais podem ser feitas pelas práticas borboletas no volante. Mas deixei claro que era possível comprar a configuração de entrada por R$ 120 mil, equipada com um 1.5 turbo de 136 cv."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jIXtNLPUidpBP0HgCcTrVQ_sY7U=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/img_9636_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Os detalhes do interior também chamaram a atenção: o casal perguntou sobre a bandeira do Reino Unido no painel, uma das novidades da reestilização. Mostrei que ela era iluminada por LEDs e que também era possível escolher a cor das luzes do interior do carro. Contei que a principal novidade no exterior, inclusive, eram as luzes de LED da lanterna, que também formam o desenho da bandeira."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/qyhbzkxJ0b9mQZqj_q0PHrPQ2R0=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/img_9646_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Como estavam muito interessados, eu me senti à vontade para eleger o que achava mais legal e o que poderia melhorar no carro. Falei do visual da central multimídia de 8,8 polegadas, que finalmente ganhou o sistema Apple CarPlay, mas que ainda não é compatível com Android Auto."
                    },
                    {
                        "type": "text",
                        "content": "Mostrei o volante, com ótima pegada e bom acabamento, e os bancos do tipo concha, muito confortáveis e feitos com bons materiais, um mix de couro e alcantara, aquele revestimento acamurçado. Falta freio de mão eletrônico e função auto hold (que segura o freio nas paradas), mas o Mini tem o forro do teto preto, revestimento interno em preto brilhante e sistema de som Harman Kardon, com um microfone competente para ligações via Bluetooth."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/m8Y9I0JC0DvFFpnZjqB-V3bIE6E=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/img_9635_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "No geral, a ergonomia do carro é ótima, todos os controles ficam à mão, mas a visibilidade deixa a desejar — culpa do pequeno retrovisor central. Expliquei como funciona o head-up display e o sistema start-stop, que pode, sim, incomodar, mas que é eficiente para economizar gasolina, o único combustível possível para o carro. São bons 10,6 km/l na cidade e 13,2 km/l na estrada, de acordo com o Inmetro."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/bmw-x2-ganha-nova-versao-de-entrada-com-motor-de-mini-so-que-flex.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/flagra-novo-chevrolet-prisma-sera-praticamente-um-mini-cruze.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Os dois acharam os números de consumo ótimos para um carro capaz de entregar tanto desempenho. Expliquei que, além do conjunto mecânico, existem outras razões: o peso e o tamanho do carro. São 1.320 kg (100 kg a mais que o convencional) e 3,85 metros de comprimento, o que também explica a agilidade e a facilidade para estacioná-lo."
                    },
                    {
                        "type": "text",
                        "content": "Mas o sensor de estacionamento traseiro é neurótico demais e se torna praticamente dispensável, graças à câmera de ré de boa qualidade. A baliza automática com sensor dianteiro é opcional."
                    },
                    {
                        "type": "text",
                        "content": "Hora de subir a serra e mudar o modo de condução de Green para Sport — são três no total: econômico, intermediário ou esportivo. Além do ronco do motor ter saído mais intenso pelo escapamento duplo central, o acelerador ficou mais sensível a cada pisada."
                    },
                    {
                        "type": "text",
                        "content": "O resultado, em minha opinião, é que o Mini se mostrou um dos carros com tração dianteira mais divertidos e ágeis do mercado. As retomadas são estupidamente rápidas: apenas 2,9 segundos para ir de 60 km/h a 100 km/h."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/JPlpfA6VZub1XmWGPTRqtCTjKw0=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/p90331925_highres_mini-john-cooper-wor_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A conversa foi interrompida por uma frase que eu não esperava: “Suspensão de Mini não é feita para o Brasil, né? É dura demais”. De fato, bastava passar por qualquer buraco para ver os dois pularem no banco de trás. Inicialmente, fiquei preocupada com o espaço, mas a falta de maciez do carro é que foi, sem dúvidas, o principal ponto negativo para as minhas caronas. O chacoalhar em asfalto irregular também me incomodou."
                    },
                    {
                        "type": "text",
                        "content": "Para deixar a viagem mais agradável, diminuí a velocidade e abri a capota elétrica. O teto de tecido dobrável pode ser aberto e fechado em 18 segundos, a velocidades de até 30 km/h. A capota possui uma dobra em formato de Z, com um mecanismo que opera em três estágios: aberta, fechada ou \"teto solar\" — que possibilita a entrada do vento sem a necessidade de abrir todo o teto. Pena que ela rouba espaço do porta-malas de 215 litros (160 litros com a capota recolhida). Uma alternativa é rebater os bancos de trás e ficar com bons 941 litros, de acordo com a montadora."
                    },
                    {
                        "type": "text",
                        "content": "Depois de 50 minutos de viagem, hora de descer do carro. Não dá para negar que o novo Mini não é um carro para dar carona. Sorte a minha eles terem se distraído com tanta informação e detalhes diferentes."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/3aABSJ8qqYz09PjeajsohWiVOos=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/img_9659_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Pontos fortes:"
                    },
                    {
                        "type": "text",
                        "content": "É extremamente divertido, ágil nas curvas e forte nas respostas do motor e câmbio. A ergonomia e o acabamento estão na lista dos principais pontos fortes do JCW Cabrio."
                    },
                    {
                        "type": "text",
                        "content": "Pontos fracos:"
                    },
                    {
                        "type": "text",
                        "content": "Suspensão é dura demais para o asfalto brasileiro, os sensores de estacionamento não refletem a realidade e sobra pouco espaço para os ocupantes do banco de trás"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/wdU-cxnMWriwc2BEXDLcoEiW6do=/620x413/e.glbimg.com/og/ed/f/original/2019/01/31/img_9661_edit.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Teste"
                    },
                    {
                        "type": "text",
                        "content": "Aceleração"
                    },
                    {
                        "type": "text",
                        "content": "0 - 100 km/h: 5,8 s0 - 400 m: 14 s0 - 1.000 m: 25,3 sVel. a 1.000 m: 213,8 km/hVel. real a 100 km/h: 98 km/h"
                    },
                    {
                        "type": "text",
                        "content": "Retomada"
                    },
                    {
                        "type": "text",
                        "content": "40 - 80 km/h (Drive): 2,5 s60 - 100 km/h (D): 2,9 s80 - 120 km/h (D): 3,5 s"
                    },
                    {
                        "type": "text",
                        "content": "Frenagem"
                    },
                    {
                        "type": "text",
                        "content": "100 - 0 km/h: 40,2 m80 - 0 km/h: 26,6 m60 - 0 km/h: 14,2 m"
                    },
                    {
                        "type": "text",
                        "content": "Consumo"
                    },
                    {
                        "type": "text",
                        "content": "Urbano: 10,2 km/lRodoviário: 14 km/lMédia: 12,1 km/lAut. em estrada: 616 km"
                    },
                    {
                        "type": "text",
                        "content": "Ficha técnica"
                    },
                    {
                        "type": "text",
                        "content": "Motor: Dianteiro, transversal, quatro cilindros em linha, 2.0, 16V, turbocompressor, injeção direta, gasolina"
                    },
                    {
                        "type": "text",
                        "content": "Potência: 231 cv entre 5.200 e 6.200 rpm"
                    },
                    {
                        "type": "text",
                        "content": "Torque: 32,6 kgfm entre 1.250 e  4.800 rpm"
                    },
                    {
                        "type": "text",
                        "content": "Câmbio: Automático, 8 marchas sequenciais, tração dianteira"
                    },
                    {
                        "type": "text",
                        "content": "Direção: Elétrica"
                    },
                    {
                        "type": "text",
                        "content": "Suspensão: Independente, McPherson (diant.) e multilink (tras.)"
                    },
                    {
                        "type": "text",
                        "content": "Freios: Discos ventilados (diant.) e discos sólidos (tras.)"
                    },
                    {
                        "type": "text",
                        "content": "Pneus: 205/40 R18"
                    },
                    {
                        "type": "text",
                        "content": "Dimensões"
                    },
                    {
                        "type": "text",
                        "content": "Compr.: 3,85 m"
                    },
                    {
                        "type": "text",
                        "content": "Largura: 1,72 m"
                    },
                    {
                        "type": "text",
                        "content": "Altura: 1,41 m"
                    },
                    {
                        "type": "text",
                        "content": "Entre-eixos: 2,49 m"
                    },
                    {
                        "type": "text",
                        "content": "Tanque: 44 litros"
                    },
                    {
                        "type": "text",
                        "content": "Porta-malas: 215/160 litros (fabricante)"
                    },
                    {
                        "type": "text",
                        "content": "Peso: 1.320 kg"
                    },
                    {
                        "type": "text",
                        "content": "Central multimídia: 8,8 pol., sensível ao toque"
                    },
                    {
                        "type": "text",
                        "content": "Garantia: 2 anos"
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/testes/noticia/2019/02/exclusivo-aceleramos-o-volkswagen-tarek-futuro-rival-do-jeep-compass-que-sera-lancado-no-brasil-em-2020.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/ford-ecosport-2020-todos-os-precos-versoes-e-custos-para-manter.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/opiniao-rede-chevrolet-e-que-mais-vende-carros-por-loja-confira-o-ranking-exclusivo.html"
                        ]
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Ford EcoSport 2020: todos os preços, versões e custos para manter",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/ford-ecosport-2020-todos-os-precos-versoes-e-custos-para-manter.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/qg7X2HqKoFEayR7dZavmIOTlhC0=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/ford-ecosport-2020.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Alinha 2020 daFordEcoSporttrouxe algumas novidades para o SUV lançado em 2003 e que anos atrás foi líder da categoria. A mais importante delas é olançamento de umaversão inéditaque chegasem o controverso estepe na tampa do porta-malas do carro."
                    },
                    {
                        "type": "text",
                        "content": "Mas, a novidade éexclusiva à topo de linha Titanium, que também ficoumenos potentecom a atualização da linha do utilitário.Isso porque agora essa versão tem o motor 1.5 de 137 cv. Agora, o 2.0 de 176 cv é exclusivo da configuração Storm 4x4. Aausência do estepe na tampa traseiratambém encareceu a versão, que é mais de R$ 10 mil mais cara que a versão anterior, de mesma motorização."
                    },
                    {
                        "type": "text",
                        "content": "Quer saber tudo sobre a nova linha daEcoSport? Veja detalhes de todas as versões, o que elas incluem e quanto custam abaixo:"
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/novo-suv-que-substituira-o-ecosport-em-2020-pode-se-chamar-puma.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/porque-os-consumidores-preferem-suvs-e-picapes.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/opiniao-tudo-vai-virar-suv-depois-das-peruas-sedas-comecam-desaparecer.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "EcoSport SE 1.5 - R$ 78.990"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: Controle eletrônico de estabilidade (ESC) e tração (TCS), dois airbags - frontais -, assistente de partida em rampa (HLA), sistema multimídia com tela touch screen de sete polegadas, entrada USB, conexão Bluetooth e conectividade completa comAndroid AutoeApple CarPlay, retrovisores externos com indicador de direção, roda liga leve de 15 polegadas, ar condicionado, alarme anti furto, luz elevada de freio, assistente de frenagem em emergência (EBA), aviso de utilização do cinto de segurança para motorista e passageiros, cintos de segurança traseiros laterais e central de três pontos, controle automático em descidas (HDC), freios ABS com EBD, Isofix, tomada 12V, travamento automático das portas e sistema de proteção anticapotamento."
                    },
                    {
                        "type": "text",
                        "content": "EcoSport SE 1.5 AT - R$ 84.990"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: todos os itens da versão anterior, além de piloto automático, transmissão automática de seis velocidades, vidro elétrico do motorista com sistema de abertura e fechamento um-toque para cima ou para baixo e volante revestido em couro."
                    },
                    {
                        "type": "text",
                        "content": "EcoSport FreeStyle 1.5 - R$ 85.890"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: todos os da versão anterior - exceto piloto automático e transmissão automática. Ar-condicionado automático e digital, câmera de ré, roda de liga leve de 16 polegadas, sensor de estacionamento traseiro, tela de LCD multifuncional touch screen de sete polegadas, assoalho inteligente no porta-malas, luzes diurnas em LED, bancos revestidos em tecido e couro ecológico, farol de neblina dianteiro e sistema anticapotamento (RSC)."
                    },
                    {
                        "type": "text",
                        "content": "EcoSport FreeStyle 1.5 AT - R$ 91.890"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: todos os itens da versão anterior, acrescidos de piloto automático e transmissão automática de seis velocidades."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/jeep-renegade-todos-os-precos-versoes-e-custos.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/10/honda-hr-v-2019-todos-os-precos-versoes-e-custos.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/08/citroen-c4-cactus-2019-precos-versoes-e-custos.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "EcoSport Titanium 1.5 AT - R$ 103.890"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: todos os da versão anterior, além de pneus run flat, roda liga leve de 17 polegadas, sensor de monitoramento individual de pressão dos pneus (TPMS), sistema de monitoramento do ponto cego com alerta de tráfego cruzado (BLIS), teto solar elétrico, sistema multimídia com tela touch screen de oito polegadas com GPS, ajuste lombar do banco do motorista, bancos revestidos em couro ecológico, sete airbags - frontais, laterais e cortina e joelhos para motorista -, aviso de pressão baixa dos pneus (DDS), acendimento automático dos faróis, AppLink, assistência de emergência, chave com sensor de presença - acesso inteligente e partida sem chave -, comandos de voz com funções de áudio, telefone e navegador, sensor de chuva, sistema de navegação e Sony Premium Sound"
                    },
                    {
                        "type": "text",
                        "content": "EcoSport Storm 2.0 4WD AT - R$ 108.390"
                    },
                    {
                        "type": "text",
                        "content": "Itens de série: todos os itens da versão FreeStyle 1.5 AT, além de faróis de xenon, roda de liga leve de 17 polegadas, tela de LCD multifuncional touch screen de oito polegadas, teto solar elétrico, transmissão automática de seis velocidades com trocas de marchas manuais no volante, tração dianteira e traseira, capa de estepe rígida, faróis com acabamento escurecido, Kit Storm (aplique frontal, traseiro e adesivos frontais e laterais), lanternas traseiras fumê, ajuste lombar do banco do motorista, bancos revestidos em couro ecológico, sete air bags - frontais, laterais e cortina e joelhos para motorista -, faróis bi-xenon adaptativos com ajuste de altura automática e lavadores, acendimento automático dos faróis, alto falantes, AppLink, assistência de emergência, chave com sensor de presença - acesso inteligente e partida sem chave -, comandos de voz com funções de áudio, telefone e navegador, sistema de navegação e Sony Premium Sound."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/bb3o-kTE23bRbOse1CQtGKMH_qM=/620x413/e.glbimg.com/og/ed/f/original/2018/01/29/ecosportstorm_2.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Farol dianteiro: R$ 1.134,37"
                    },
                    {
                        "type": "text",
                        "content": "Retrovisor externo completo: R$ 1.348,68"
                    },
                    {
                        "type": "text",
                        "content": "Espelho retrovisor externo com controle interno elétrico (sem cobertura): R$ 882,17"
                    },
                    {
                        "type": "text",
                        "content": "Cobertura externa do espelho retrovisor externo: R$ 87,00"
                    },
                    {
                        "type": "text",
                        "content": "Vidro e placa do espelho retrovisor externo: R$ 305,80"
                    },
                    {
                        "type": "text",
                        "content": "Carcaça e lente do pisca do espelho retrovisor externo: R$ 87,71"
                    },
                    {
                        "type": "text",
                        "content": "Parachoque dianteiro: R$ 969,00"
                    },
                    {
                        "type": "text",
                        "content": "Lanterna traseira direita: R$ 288,25"
                    },
                    {
                        "type": "text",
                        "content": "Elemento filtro de pólen da caixa de ventilação: R$ 61,14"
                    },
                    {
                        "type": "text",
                        "content": "Elemento do filtro de ar: R$ 90,84"
                    },
                    {
                        "type": "text",
                        "content": "Pastilhas de freio dianteiras: R$ 554,70"
                    },
                    {
                        "type": "text",
                        "content": "Filtro de óleo do motor: R$ 40,36"
                    },
                    {
                        "type": "text",
                        "content": "Filtro de combustível: R$ 42,21"
                    },
                    {
                        "type": "text",
                        "content": "Amortecedor da suspensão dianteira - lado direito: R$ 497,81"
                    },
                    {
                        "type": "text",
                        "content": "Amortecedor da suspensão dianteira - lado esquerdo: R$ 438,54"
                    },
                    {
                        "type": "text",
                        "content": "Amortecedor da suspensão traseira (duas unidades): R$ 485,94"
                    },
                    {
                        "type": "text",
                        "content": "Total: R$ 5.078,84"
                    },
                    {
                        "type": "text",
                        "content": "*Valores referentes a peças da versão Titanium 1.5 AT"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/JWLMErFIn5ReJUIVmHqMm21aYAQ=/620x300/e.glbimg.com/og/ed/f/original/2018/02/15/ecosport-1.5_se_direct.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Estribo tubular"
                    },
                    {
                        "type": "text",
                        "content": "Dispositivo antifurto para rodas"
                    },
                    {
                        "type": "text",
                        "content": "Assoalho inteligente do porta malas"
                    },
                    {
                        "type": "text",
                        "content": "Cadeirinha para pet"
                    },
                    {
                        "type": "text",
                        "content": "Engate"
                    },
                    {
                        "type": "text",
                        "content": "Geladeira Portátil"
                    },
                    {
                        "type": "text",
                        "content": "Protetor de Carter"
                    },
                    {
                        "type": "text",
                        "content": "Protetor de Porta Malas"
                    },
                    {
                        "type": "text",
                        "content": "Rede organizadora do porta-malas"
                    },
                    {
                        "type": "text",
                        "content": "Rede porta-objetos da tampa"
                    },
                    {
                        "type": "text",
                        "content": "*Preços sob consulta nas concessionárias da marca"
                    },
                    {
                        "type": "text",
                        "content": "Vermelho Arpoador (sólida):sem custo adicional - disponível para todas as versões, exceto Storm"
                    },
                    {
                        "type": "text",
                        "content": "Branco Ártico (sólida):R$ 700 - disponível para todas as versões"
                    },
                    {
                        "type": "text",
                        "content": "Cinza Moscou (perolizada):R$ 700 - disponível para todas as versões"
                    },
                    {
                        "type": "text",
                        "content": "Prata Dublin (metálica):R$ 1.450  - disponível para todas as versões"
                    },
                    {
                        "type": "text",
                        "content": "Azul Belize (perolizada):R$ 1.450 - disponível para todas as versões, exceto Storm"
                    },
                    {
                        "type": "text",
                        "content": "Preto Bristol (perolizada):R$ 1.450 - disponível para todas as versões"
                    },
                    {
                        "type": "text",
                        "content": "Marrom Trancoso (metalizada):sem custo adicional - disponível apenas para a versão Storm"
                    },
                    {
                        "type": "text",
                        "content": "10 mil km:R$ 439,00"
                    },
                    {
                        "type": "text",
                        "content": "20 mil km:R$ 599,00"
                    },
                    {
                        "type": "text",
                        "content": "30 mil km:R$ 799,00"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Mercedes-Benz Classe X só será lançada no fim de 2019, dizem lojistas; montadora confirma atraso com a picape",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/mercedes-benz-classe-x-so-sera-lancada-no-fim-de-2019-dizem-lojistas-montadora-confirma-atraso-com-picape.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/g-BuxmFIO1UTcXRUyOAiRmQ_Rmc=/e.glbimg.com/og/ed/f/original/2018/03/18/mercedes_classe_x_flagrada_em_teste_no_brasil.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Era para ser neste primeiro semestre de 2019, mas o lançamento dapicape Classe Xainda vai demorar. Autoesporte procurou várias concessionárias daMercedes-Benzpara descobrir quando será o início das vendas, e todos os vendedores nos deram a mesma previsão:a picape só será lançada no fim do ano, possivelmente em novembro. A justificativa é de que houve um atraso na homologação do utilitário.Procurada pela redação, a montadora também confirmou que o projeto está atrasado, mas sem dizer o porquê."
                    },
                    {
                        "type": "text",
                        "content": "A demora do lançamento em relação aos mercados europeus tem sua razão estratégica.Os países da América do Sul (incluindo o Brasil) receberão as unidades produzidas na fábrica do grupo Renault-Nissan em Córdoba, na Argentina. A produção está programada para começar neste início de ano. Ou seja, de uma forma ou de outra, a picape só chegaria às concessionárias daqui a uns meses. Como a procura anda alta, os vendedores lamentam."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/4vecRRyGhhKsZoOypM6AuSYNQjE=/e.glbimg.com/og/ed/f/original/2018/03/18/mercedes_classe_x_flagrada_em_testes_no_brasil_3.jpg"
                    },
                    {
                        "type": "text",
                        "content": "No fim de 2017,Autoesporte publicou uma projeção exclusiva dos preçosque a picape deve ter no Brasil. A estimativa inicial era de valores entre R$ 180 mil e R$ 240 mil. Como o dólar norte-americano está mais estável, ainda apostamos nestes números.No momento, apenas as versões estão confirmadas: Pure, Progressive e Power. A picape já tem até um site dedicado no Brasil, com muitas informações."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/05/precos-versoes-e-motores-o-que-ja-sabemos-sobre-mercedes-benz-classe-x.html",
                            "https://revistaautoesporte.globo.com/testes/noticia/2017/10/picape-mercedes-benz-classe-x-primeiras-impressoes.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2017/07/comparamos-dimensoes-da-picape-da-mercedes-com-outras-medias.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2017/09/mercedes-benz-classe-x-pode-ter-precos-entre-r-180-mil-e-r-240-mil.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/ANUEqrrkuTsJa3Jtb-0pHrxOb1k=/e.glbimg.com/og/ed/f/original/2018/05/02/mercedes-benz-classe-x-pure-autoesporte-1.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Apesar dos questionamentos em torno do uso do diesel, a Classe X não fará experiências mecânicas. A picape deverá oferecer três opções de motores, sempre movidos pelo combustível fóssil.A opção de entrada Pure X220d usará o mesmo 2.3 da Frontier, porém ajustado pela engenharia da alemã e com apenas um turbo.Nesta configuração gera 163 cv de potência e 40 kgfm de torque, associado ao câmbio automático de sete marchas."
                    },
                    {
                        "type": "text",
                        "content": "Na opção Progressive X250d, o motor 2.3 passa a contar com os dois turbos presentes na picape Nissan.A potência e o torque sobem a 190 cv e 45 kgfm, com a mesma transmissão de sete velocidades, que deverá ser padrão no modelo. Quem quiser um motor maior terá de pedir pelatopo de linha Power X350d, que terá o 3.0 V6 turbo de 258 cv e 56 kgfm.Ao que parece, todas as combinações terão tração integral 4x4 e cabine dupla."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/0bufIib3ABJqnDEDyYDWDM3YhWI=/e.glbimg.com/og/ed/f/original/2017/12/01/mercedes.gif"
                    },
                    {
                        "type": "text",
                        "content": "Ainda sem concorrentes entre as marcas de luxo, aMercedes Classe Xenfrentará versões de topo deToyota Hilux,Volkswagen Amaroke cia. Estas, por sua vez, ganharão outra rival inédita derivada daNissan Frontier: aRenault Alaskan. No fim do ano ainda virá aRAM 1500para bagunçar a disputa na categoria."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/2019-sera-o-ano-das-picapes-com-volkswagen-tarok-mercedes-classe-x-e-muito-mais.html",
                            "https://revistaautoesporte.globo.com/Videos/noticia/2018/11/video-vw-tarok-futura-rival-da-fiat-toro-toyota-hilux-gr-s-e-outras-picapes-do-salao-de-sp.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/flagra-sucessora-da-fiat-strada-encara-testes-na-neve-nova-picape-estreia-em-2020.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/ford-tera-picape-menor-do-que-ranger-para-desafiar-fiat-toro-e-futura-volkswagen-tarok.html"
                        ]
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Google Maps passa a dedurar radares de velocidade no Brasil, para evitar multas",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/google-maps-passa-dedurar-radares-de-velocidade-no-brasil-para-evitar-multas.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/CZu-W5lY5kz0nU80RJDM-FZHGUc=/620x413/e.glbimg.com/og/ed/f/original/2019/01/23/maps.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O aplicativoGoogle Mapspassou a disponibilizar uma função de detecção de radares de velocidade para os usuários do serviço, tanto para sistemasAndroid como iOS (iPhone).A ferramenta deve evitar que muitas pessoas colecionem correspondências dos Departamentos de Trânsito Estaduais. Em um primeiro momento, o serviço estava sendo testado apenas na cidade do Rio de Janeiro, mas agora a função \"dedo duro\" já está liberada para todas as cidades do Brasil.Autoesporteratifica a importânica de se respeitar os limites de velocidade, e de dirigir de forma segura e responsável a fim de evitar acidentes."
                    },
                    {
                        "type": "text",
                        "content": "Neste caso específico, a ferramenta pode estimular atitudes inconsequentes ao volante."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/06/apple-carplay-waze-google-maps.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2017/04/google-lanca-atalho-que-lembra-onde-veiculo-foi-estacionado.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/05/google-aposta-na-realidade-aumentada-para-sua-plataforma-de-mapas.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Como funciona"
                    },
                    {
                        "type": "text",
                        "content": "Além de um sinal sonoro,o aplicativo destaca os equipamentos na tela do celular toda vez que o condutor estiver se aproximando de um radar. Além disso, os \"pardais\", como ficaram conhecidos os radares, poderão também ser visualizados na telinha quando o usuário ampliar o campo de alcance do mapa."
                    },
                    {
                        "type": "text",
                        "content": "Os ícones azuis representam os radares móveis, e os laranjas apontam os fixos."
                    },
                    {
                        "type": "text",
                        "content": "Em outros países, o serviço indica ainda o limite de velocidade estipulado para a via, mas essa utilidade ainda não está em funcionamento por aqui."
                    },
                    {
                        "type": "text",
                        "content": "PolêmicaMas o tema é polêmico. Afinal,se por um lado a ferramenta é útil para motoristas desatentos — os que não costumam infringir os limites de velocidade, por outro, ela pode estimular atitudes imprudentes como a de acelerar acima da velocidade permitida, antes e depois dos radares."
                    },
                    {
                        "type": "text",
                        "content": "Fizemos, então, essa pergunta sobre o comportamento dos usuários aoGoogle. E a resposta do porta-voz da gigante de tecnologia você confere a seguir:\"A segurança foi uma das principais prioridades do Google ao criar esse recurso. Desenvolvemos a ferramenta para tornar mais fácil o ato de dirigir de forma mais segura, cumprindo as leis locais. Estamos sempre preocupados em desenvolver recursos que beneficiem a vida dos usuários.\", disse o porta-voz."
                    },
                    {
                        "type": "text",
                        "content": "Questionado sobre quando a outra ferramenta (do limite de velocidade estipulado para a via) estará em funcionamento por aqui, o porta-voz do Google foi menos enfático:"
                    },
                    {
                        "type": "text",
                        "content": "\"Estamos sempre testando novas funcionalidades, mas ainda não temos previsão de lançamento no Brasil\", disse."
                    },
                    {
                        "type": "text",
                        "content": "Outra funcionalidade que está na ponta dos dedos é a possibilidade de interagir e compartilhar informações com a ferramenta. Os motoristas podem contribuir para o aperfeiçoamento constante do software de maneira simples.Ao tocar em um radar durante a navegação é possível informar ao sistema se a câmera realmente ainda está no local ou não.Assim como acontece noWaze, o Maps também avisará quando houver obras na estrada. E os usuários poderão postar atualizações sobre os alertas para que o sistema do Google faça atualização em tempo real."
                    },
                    {
                        "type": "text",
                        "content": "Há ainda uma função que parece intuitiva e fácil de operar:a possibilidade de se adicionar outros radares no mapa, apertando o balão com sinal de \"+\" na tela de navegação. A novidade feita para os sistemas da Google e da Apple não requer nem mesmo que os sistemas estejam atualizados."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Opinião: Rede Chevrolet é a que mais vende carros por loja. Confira o ranking exclusivo!",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/opiniao-rede-chevrolet-e-que-mais-vende-carros-por-loja-confira-o-ranking-exclusivo.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/meJ0wNlHIu5jAwLZl5qblBEUE_g=/620x413/e.glbimg.com/og/ed/f/original/2018/05/25/05_gm_chevrolet_onix_lt1_25-05-2018.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A longa crise de 2013 a 2016 dizimou não só os números deprodução e vendas de carrosno Brasil, mas também levou muitas concessionárias à bancarrota. Aos poucos as marcas foram adaptando o tamanho de suas redes ao novo volume (reduzido) de vendas."
                    },
                    {
                        "type": "text",
                        "content": "As quatro mais tradicionais, que chegavam perto de 600 concessionárias nos tempos áureos, agora ostentam redes de 400 pontos, em média. No total de associadas daAnfavea(associação das montadoras), o número de concessionárias de veículos leves e pesados caiu de 4.287 em 2017 para 4.016 no ano passado."
                    },
                    {
                        "type": "text",
                        "content": "Num movimento contrário, marcas emergentes comoJeep, Hyundai, Nissan, Toyota e Cheryforam ampliando suas estruturas de negócios, mas em volume incapaz de compensar as perdas das marcas mais tradicionais."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jNcT9yaF7E37ZT_oTsX00O-xdbM=/e.glbimg.com/og/ed/f/original/2018/12/29/t__6HeVPlw.jpg"
                    },
                    {
                        "type": "text",
                        "content": "De 2017 para 2018, a Nissan foi a que mais expandiu sua rede, com 26 novos pontos, embalada pelo sucesso do Kicks. AVW, mesmo em alta no mercado, fechou 30 concessionárias, enquantoFord, Mitsubishi/Suzuki e Hondafecharam em torno de 20 cada.Peugeot e Citroën, irmãs no Grupo PSA, fecharam pontos e transformaram outros em multimarca."
                    },
                    {
                        "type": "text",
                        "content": "Claramente o mercado passa por um momento de adaptação das estruturas de venda e pós-venda ao tamanho de mercado de cada empresa."
                    },
                    {
                        "type": "text",
                        "content": "O ranking abaixo mostra a média de vendas de veículos por loja em cada marca, com base nas vendas em 2018 e no tamanho da rede declarada por cada montadora. Não estão incluídas as marcas sem fábrica no país, nem aCaoa-Chery, cuja rede só foi ampliada na reta final do ano."
                    },
                    {
                        "type": "text",
                        "content": "RANKING DE VENDAS POR CONCESSIONÁRIA – 2018"
                    },
                    {
                        "type": "text",
                        "content": "1) Chevrolet: 1.180 veículos (368 lojas)2) Toyota: 1.163 (172 lojas)3) Hyundai: 979 (211 lojas)4) Volkswagen: 905 (407 lojas)5) Renault: 870 (247 lojas)6) Honda: 639 (206 lojas)7) Fiat: 625 (521 lojas)8) Ford: 620 (365 lojas)9) Jeep: 560 (191 lojas)10) Nissan: 554 (176 lojas)11) Peugeot: 263 (90 lojas)12) Mercedes: 261 (55 lojas)13) Jaguar/Land Rover: 220 (39 lojas)14) Citroën: 219 (93 lojas)15) BMW/Mini: 177 (74 lojas)16) Audi: 177 (49 lojas)17) Mitsubishi/Suzuki: 142 (188 lojas)"
                    },
                    {
                        "type": "text",
                        "content": "A folgada liderança daGMchama a atenção, com quase 1.200 carros vendidos por loja em 2018 (cerca de quatro por dia útil). Mas esse bom desempenho não parece fazer a montadora americana tão feliz, já que ela alega seguidos prejuízos no país."
                    },
                    {
                        "type": "text",
                        "content": "Um dos motivos é que quase dois terços de suas vendas estão concentradas na dupla Onix e Prisma, modelos de entrada, com baixa margem de lucro."
                    },
                    {
                        "type": "text",
                        "content": "Entre as quatro grandes, a Volkswagen é a que está mais saciando as necessidades de seus revendedores. A rede foi enxuta, e a marca está fincando o pé em modelos de maior lucratividade comoPolo, Virtus, e em breve o SUV compactoT-Cross, deixando modelos de baixo valor agregado para as vendas diretas, caso de Gol e Voyage."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/3pMdgEjOUFFtRLdgntj8nQDMao0=/620x466/e.glbimg.com/og/ed/f/original/2018/10/30/volkswagen_t-cross__2_.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Na outra ponta da tabela estão marcas premium, que vendem menos de um carro por dia útil, mas com margens bem mais elevadas. Ao que parece, as redes mais saudáveis são as do bloco intermediário, que conseguem mesclar bons volumes, vendendo carros do segmento médio, mais lucrativos."
                    },
                    {
                        "type": "text",
                        "content": "Pergunte a revendedores Toyota, Jeep, Honda e Hyundai se eles estão felizes, e verá um sorriso no rosto de cada um. Em especial a rede Toyota, que quase se iguala à média da líder GM, porém com carros de maior valor agregado. Situação oposta vivem suas conterrâneas Mitsubishi e Suzuki, do Grupo HPE: a rede ainda parece grande para os atuais volumes de venda."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/opiniao-marcas-francesas-invertem-papel-em-10-anos-no-brasil.html",
                            "https://revistaautoesporte.globo.com/Blogs/noticia/2018/10/opiniao-com-o-polo-volkswagen-se-arriscou-num-segmento-em-decadencia-o-resultado-foi-um-fenomeno.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/opiniao-tudo-vai-virar-suv-depois-das-peruas-sedas-comecam-desaparecer.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Numa fase em que boa parte das negociações com carros 0-km se dão no ambiente digital, o desafio das montadoras é manter o fluxo de loja e de oficinas capaz de manter a saúde de sua rede autorizada. Outro fator complicador são as dimensões continentais do Brasil. Como enxugar o tamanho da rede sem perder capilaridade?"
                    },
                    {
                        "type": "text",
                        "content": "O fato é que, se as montadoras sofrem com esse momento disruptivo de seu tradicional modelo de negócio, as concessionárias estão ainda mais na berlinda."
                    },
                    {
                        "type": "text",
                        "content": "Glauco Lucenaescreve neste espaço às terças. Jornalista com 28 anos de experiência no setor automotivo, foi redator-chefe de Autoesporte até 2013 e gerente de imprensa da Jeep. Hoje é consultor automotivo e mantém o site AutoBuzz."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Jeep e Chrysler incluem mais unidades do Wrangler e Chrysler 300C no megarecall de airbags",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/jeep-e-chrysler-incluem-mais-unidades-do-wrangler-e-chrysler-300c-no-megarecall-de-airbags.html",
                "description": [
                    {
                        "type": "text",
                        "content": "O grupo FCA, responsável pelaJeepeChrysler, anunciou hoje que mais unidades dos modelosWranglere300Ctêm os airbags com nitrato de amônio da fabricanteTakatae, por isso, foram incluídos nomegarecall mundial de airbags. O caso é considerado o maior recall do mundo e tem como objetivo retirar de circulação os airbags que podem se romper e ferir os ocupantes. Há registros de vítimas fatais por conta do problema em diversos países. No Brasil,Autoesporterevelou a primeira vítima, que sofreu lesões e sobreviveu."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/04/megarecall-de-airbags-cinco-anos-depois-23-milhoes-de-carros-no-brasil-ainda-precisam-ser-consertados.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2016/07/eu-acredito-na-sobrevivencia-da-empresa-diz-presidente-da-takata-brasil.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Agora, os donos de 670 unidades doJeep Wranglerano/modelo 2014 a 2016 e de outras 70 unidades doChrysler 300Cano/modelo 2014/2015 terão que agendar o reparo gratuito em uma concessionária autorizada. No total, são 740 carros."
                    },
                    {
                        "type": "text",
                        "content": "Os consertos poderão ser feitos a partir de 4 de fevereiro. Neste caso, o defeito afeta o airbag do lado do passageiro, apenas. Para saber se o seu está envolvido, é preciso consultar a numeração dos chassis convocados abaixo."
                    },
                    {
                        "type": "text",
                        "content": "Para esclarecer dúvidas e fazer o agendamento, a Jeep disponibiliza o telefone 0800 703 7150, enquanto o da Chrysler é 0800 703 7130. Além disso, os consumidores podem acessar mais informações nos sites das duas marcas."
                    },
                    {
                        "type": "text",
                        "content": "Numeração dos chassis convocados"
                    },
                    {
                        "type": "text",
                        "content": "Chrysler 300C - chassis (6 últimos dígitos, não sequenciais): de 237744 a 926635"
                    },
                    {
                        "type": "text",
                        "content": "Jeep Wrangler - chassis (6 últimos dígitos, não sequenciais) de 117037 a 738079"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/b84tfC_jl5dhQ5MNaqdB7kYfBn4=/e.glbimg.com/og/ed/f/original/2015/06/02/jeep.jpg"
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Por que as vendas do Hyundai Creta - e de outros carros para o público PcD - são suspensas e retomadas?",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/por-que-vendas-do-hyundai-creta-e-de-outros-carros-para-o-publico-pcd-sao-suspensas-e-retomadas.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/sVhF7vZbQWPcfqZsWQVh-O75h3w=/620x413/e.glbimg.com/og/ed/f/original/2017/11/01/creta_sport-034_tDLvfc7.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Em agosto de 2018, aHyundaisuspendeu,por tempo indeterminado, as vendas da versão para pessoas com deficiência (PcD) do Creta. Cinco meses depois,em janeiro de 2019, a fabricante divulgou a retomada da comercialização do SUV com isenção fiscal.O carro, além de ter sidolíder de vendas do ano passado dentro do segmento de utilitários, éum dos mais procurados pelo público PcD. Segundo concessionárias da marca, o Creta PcD é não só a versão mais vendida do modelo, como tambéma mais popular entre os veículos que se enquadram na isenção de impostos. Então,diante de tanta demanda, por que a oferta do Creta PcD sofre interrupções?"
                    },
                    {
                        "type": "text",
                        "content": "saiba mais"
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/11/como-adaptar-seu-carro-com-acessorios-para-pessoa-com-deficiencia-pcd.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/02/13-carros-e-versoes-para-pessoas-com-deficiencia-pcd-ate-r-70-mil.html"
                        ]
                    },
                    {
                        "type": "text",
                        "content": "Procurada porAutoesporte, a Hyundai declarou que suspender temporariamente as vendas do Creta para PcD “foi umamedida necessária para que a capacidade de produção pudesse ser totalmente dedicada aospedidos registradosaté o momento da interrupção, em agosto de 2018”."
                    },
                    {
                        "type": "text",
                        "content": "Uma fonte da montadora sul-coreana explicou que, antes da entrada do Creta no programa de isenção de impostos,o outro carro da marca ofertado para o público PcD, o compactoHB20, vendia em torno de200 a 300 unidades mensais. Já com o início das vendas da versão PcD do SUV,os números saltaram para 500 unidades comercializadas mensalmente em 2017, valor que dobrou no ano seguinte.Com perto de mil unidades do Creta PcD sendo vendidas por mês, a oferta de outras versões do veículo foram reduzidas. Paraequilibrar a oferta, a montadora optou por tirar do mercado justamente essa versão com forte demanda."
                    },
                    {
                        "type": "text",
                        "content": "Como o carro voltado para pessoas com deficiência tem, necessariamente,preço inferior a outras versões- no caso do Creta,a versão de entrada custa R$ 77.890, enquanto aPcD sai por R$ 69.990-, fica a dúvida de se a medida tem alguma relação com alucratividade.Segundo a fonte da Hyundai, no entanto, não é o caso. Segundo ele, “produzir PcDnão afeta o fluxo da linha de montagem nem a rentabilidade da empresa”."
                    },
                    {
                        "type": "text",
                        "content": "Mesmo assim pode haver algum tipo de impacto, uma vez que as versões paras PcD são menos equipadas.A fonte da fabricante concorda que a versão do Creta com menos componentes afeta a imagem do produto. “Não achamos bom vender o carro sem tela multimídia, com rodas de ferro”, diz. Além disso, a questão pode ter desdobramentos ainda maiores: o funcionário daHyundaiacredita queo Creta pode até mesmo sair de vez do programa PcD, quando o preço do modelo subir acima dos R$ 70 mil, teto estabelecido pela lei de isenção de impostos."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/t3aGQ3lPY98wKtmBjpuqZaBFzgQ=/620x413/e.glbimg.com/og/ed/f/original/2018/08/13/kicks_my19_01_2.jpg"
                    },
                    {
                        "type": "text",
                        "content": "A interrupção temporária da produção daversão PcDpara equilibrar a oferta de outras versões do mesmo modelo não é exclusividade da Hyundai. No períodoentre maio e setembro de 2018, a venda da versão PcD doNissanKickstambém foi suspensa, para ajustar a demanda à oferta. De acordo com a montadora, a medida foi necessária paraevitar que se vendesse mais unidades do SUV do que a fábrica consegue produzir."
                    },
                    {
                        "type": "text",
                        "content": "A Nissan também nega que a interrupção da versão para pessoas com deficiência do Kicks tenha alguma ligação com lucratividade.Eles reforçam que o motivo da suspensão temporária é apenas a limitação de produção. A fábrica da Nissan noComplexo Industrial de Resende, no Rio de Janeiro,funciona em quase total capacidade em dois turnose, segundo a empresa, seria necessário um terceiro turno para ofertar Kicks PcD sem interrupções."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Videos/noticia/2018/11/video-hyundai-saga-o-carro-que-antecipa-o-novo-hb20-e-um-creta-mais-luxuoso.html",
                            "https://revistaautoesporte.globo.com/Videos/noticia/2018/04/video-o-que-o-hyundai-creta-tem-de-bom-e-o-que-pode-melhorar.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jr_uaiz1_UVXT1sI0ttZb4AXduU=/620x413/e.glbimg.com/og/ed/f/original/2018/06/11/toyota-yaris-2019_2.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Situação semelhante aconteceu com aToyota, queparou, em novembro de 2018, a venda do Yaris hatch para PcD. De acordo com a montadora,o cadastro de novos pedidos está suspenso - e sem previsão de retorno- por conta dogrande volume de vendas diretas."
                    },
                    {
                        "type": "text",
                        "content": "Já a francesaCitroënoptou por outra estratégia para lidar com a alta demanda pela versão para o público com deficiência do crossoverC4 Cactus. Em dezembro de 2018, a montadorapassou a oferecer a versão de entrada do carro, Live, ao invés da Feel, configuração intermediária, para PcD. De acordo com um comunicado divulgado pela empresa na época, a substituição - quetirava equipamentos do veículo- permitiria “volumes maiores de produção e consequente diminuição nos prazos de atendimento”."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/gwvGY054_yC5Q7RubK1FKPtH6Gc=/e.glbimg.com/og/ed/f/original/2018/08/28/c4-home.jpg"
                    },
                    {
                        "type": "text",
                        "content": "No entanto, logo naprimeira semana de janeiro de 2019, a Citroën anunciou mais uma mudança para oC4 CactusPcD:o carro passou a ser oferecido em uma versão inédita e com outros equipamentos, denominada Feel Business. Em comunicado oficial,Ana Theresa Borsari, country manager da marca no Brasil, afirmou que a montadora entendeu que “o público PcD ansiava por equipamentos que não estavam presentes na versão Livee decidimos lançar o novo Feel Business”."
                    },
                    {
                        "type": "text",
                        "content": "“Com essa nova versão”, continua Ana Theresa, “esperamos que os nossos clientes aproveitem de maneira ainda mais ampla a experiência com oC4 Cactuse com a própria marca.”A Citroën ainda divulgou que os clientes PcD que já haviam comprado o C4 Cactus Live receberiam a versão Feel Business sem nenhum custo adicional."
                    },
                    {
                        "type": "text",
                        "content": "A lei admite que esse público sejaisento de alguns impostosna aquisição de veículos novos. OICMS(Imposto sobre Circulação de Mercadorias e Serviços), por exemplo, é abatido em casos depessoas com deficiência visual, mental (severa ou profunda) ou autistas, e éválida para veículos até R$ 70 mil fabricados no Brasil ou nos países do Mercosul."
                    },
                    {
                        "type": "text",
                        "content": "OIPI(Imposto sobre Produtos Industrializados) também pode ser abatido. Mas, nesse caso, a isenção vale apenas paraautomóveis de passageiros fabricados no Brasil e no Mercosul até 2.0 flex e no mínimo quatro portas(inclusive a de acesso ao bagageiro). Osdeficientes físicospodem ter desconto doIOF(Imposto sobre Operações Financeiras) em casos deautomóveis de passageiros fabricados no Brasil e com potência de até 128 cv."
                    }
                ]
            }
        },
        {
            "item": {
                "title": "Exclusivo: aceleramos o Volkswagen Tarek, futuro rival do Jeep Compass que será lançado no Brasil em 2020",
                "link": "https://revistaautoesporte.globo.com/testes/noticia/2019/02/exclusivo-aceleramos-o-volkswagen-tarek-futuro-rival-do-jeep-compass-que-sera-lancado-no-brasil-em-2020.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/ksiD2A7AMvu6HfvZ-k_AjK9xZYQ=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_19.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "OVolkswagen Tharué um lançamento da pesada para o mercado chinês.Projetado em conjunto com a parceira Saic, o carro foi apresentado em março de 2018 no Salão de Pequim. Inicialmente ele surgiu comoPowerful Family SUV. A princípio, não sabíamos direito o que isso queria dizer, mas logo ficou claro:o novo VW é o maior rival do Jeep Compass tanto no oriente quanto no Brasil."
                    },
                    {
                        "type": "text",
                        "content": "Na China, o VW é vendido como Tharu, mas não se acostume com o nome, pois a Volkswagenjá identifica o lançamento como Tarek. Para facilitarmos sua leitura, vamos nos referir a ele apenas como Tarek daqui em diante."
                    },
                    {
                        "type": "text",
                        "content": "Segundo a marca,o lançamento no Brasil ocorrerá no início de 2020. A fábrica de Córdoba, na Argentina, já começou a ser adaptada. O SpaceFox deu adeus ao mundo justamente para abrir espaço para o Tarek."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/vw-spacefox-sai-de-linha-e-abre-espaco-para-tarek-rival-do-jeep-renegade.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/08/volkswagen-registra-tarek-no-brasil-suv-concorrente-do-jeep-compass.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/05/volkswagen-tarek-aparece-por-completo.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/07/ofensiva-suv-volkswagen-tera-12-utilitarios-esportivos-ate-2020.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2Le1th9lLt9wyduTUw1hwbkBRfg=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_96.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "O novo SUV se encaixa em uma família cujos rebentos vieram em degrauzinho, um atrás do outro e com tamanhos escalonados. O menor é o T-Roc, feito com base no Golf. O Tarek fica logo acima, como uma opção mais espaçosa. Depois dele vem o Tayron, maior, mas abaixo do Tiguan em posicionamento de preço."
                    },
                    {
                        "type": "text",
                        "content": "Mas por que tantos SUVs? O T-Roc e o Tayron são feitos pela parceira FAW, o que exigiu um novo SUV da compatriota Saic. Daí nasceu o Tarek. Por lá, as montadoras estrangeiras são obrigadas a se associar a uma chinesa. Aqueles que não acreditavam na promessa da Volkswagen de lançar 20 SUVs até 2020 devem estar surpresos."
                    },
                    {
                        "type": "text",
                        "content": "Na prática, o Tarek foi apelidado no mercado chinês como mini Teramont, como o Atlas é chamado por lá. A associação não é por acaso: as linhas retilíneas aproximam um do outro em detalhes como os faróis, os vincos laterais e as lanternas."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/UD8CXH3WbZHZWNCwezitPBOansY=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_64.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "A divisão entre as parceiras chinesas fica explícita até no estilo. Ficou claro que os carros produzidos pela FAW são mais ousados, inspirados no Touareg; já os da Saic buscam inspiração no Teramont."
                    },
                    {
                        "type": "text",
                        "content": "O Tarek pode ser menor do que o Atlas — seu entre-eixos é de 2,68 metros, 30 centímetros a menos. A despeito disso, ficar próximo dos 2,70 m é uma bela marca para os médios, ainda mais diante do comprimento relativamente contido, de 4,45 m."
                    },
                    {
                        "type": "text",
                        "content": "O design quadradinho dá a impressão de que o carro foi esculpido em um bloco maciço. Essa impressão não é fortuita: a própria VW chama esse design de Rock-Cutting, jargão usado pelo pessoal de estilo que designa esse tipo de desenho \"esculpido em rocha\"."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/jmr6XgX4SoLTc0hdqc9luoU_9EQ=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_16.jpeg"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/uDKVKlqVxMFHzZJkKiavIz7Vqyo=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_9.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "Na frente, as linhas são horizontais e dispostas em camadas, o que acentua a sensação de largura, da mesma maneira que a grade inferior em formato de trapézio invertido. O Teramont aplica esses mesmos elementos para parecer mais largo."
                    },
                    {
                        "type": "text",
                        "content": "Mesmo que não pareçam tão detalhadas, as laterais utilizam componentes bem modelados, dos faróis às lanternas.Há um vinco bem demarcado acima das maçanetas."
                    },
                    {
                        "type": "text",
                        "content": "Atrás, as lanternas lembram o Skoda Karoq, com a parte central protuberante e desenho tridimensional. Não é à toa: o Skoda é um dos SUVs do grupo VW que derivou do mesmo projeto; o outro é oSeat Ateca. No geral, a impressão após o teste é de que o Tarek vai agradar mais aos chineses do que os SUVs mais ousados feitos pela FAW."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/BzcOuLl-Db-PVXnO-YoJg8EtIIM=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_793.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "A despeito da aparência tradicional,o Tarek também tem toques jovens. O mais visível é o logotipo da Beats nas colunas, que identifica o sistema de som queridinho da geração Y. A cor azul também é bem jovial, tal como as belas rodas modelo Tomahawk. Para mim, lembra a espada usada pelo personagem Naruto do animê de mesmo nome."
                    },
                    {
                        "type": "text",
                        "content": "E como é a parte interna? Ao entrar no Tarek, dá para ver que o acabamento está alinhado com o que há de melhor na Volkswagen. As linhas são horizontais como na carroceria e o aspecto de modernidade é garantido pelas enormes telas digitais. A principal é o quadro de instrumentos de 10,2 polegadas, totalmente digital e presente em vários modelos mais recentes da marca, do Polo ao Passat."
                    },
                    {
                        "type": "text",
                        "content": "A outra tela é a da central LCD, que pode vir em três tamanhos, de 8 até 13,2 polegadas. O carro testado tinha tela intermediária, de 10,1 polegadas. Mesmo sendo menor, ela tem boa resolução, de 133 dpi (pontos por polegada). Não chega a ser a resolução de um smartphone atual, porém ainda faz bonito diante dos rivais."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/dfCPAWZM72uFzxXMDAHfXcyGPMY=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_2_edit.jpg"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/4_bVwV6-YUX0nEbU5Jy6MUe6UAE=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_1.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "Seguindo a onda do momento de personalizar as centrais, a do VW possibilita a escolha de temas e pode deixar o interior com uma cara bem bacana. O antigo sistema do fabricante era lento e a conectividade com celulares era difícil. O novo melhorou em tudo e,além de ter aplicativos e ser conectado com Android Auto e Apple CarPlay, possui a opção de GPS com informações de tráfego em tempo real."
                    },
                    {
                        "type": "text",
                        "content": "O interior deixa claro que você está em um carro de nova geração em tudo, até mesmo comparado com o mais caro Tiguan. É óbvio quehá toques que são simplificações, você pode ver que o painel tem revestimento que imita couro, mas as portas contam com materiais mais rígidos ao toque, uma decisão de projeto voltada ao corte de custos."
                    },
                    {
                        "type": "text",
                        "content": "Na comparação com outros SUVs do grupo, a impressão é de que o Tarek está mais alinhado com o mais barato Skoda Karoq, enquanto o Tiguan fica mais próximo do requintado primo de grupo Kodiaq.Há pontos que são compartilhados com outros VW, tais como a alavanca de câmbio e comandos do ar-condicionado e de outras funções. Não vi necessidade de mudança, pois a operação dos componentes ainda agrada."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/CtdqB7KTU34H8jguPAbuD-Auk_c=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_36_edit.jpg"
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/7OrdkUG7zSH3n9xnJkD3A-hlMCo=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_3.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "Em termos de praticidade, o Tarek conta com porta-objetos de bom tamanho na parte baixa do painel e no console central, que comportam várias bugigangas e ficam devendo apenas tampas em nome da discrição— afinal, às vezes o carro fica parado na rua."
                    },
                    {
                        "type": "text",
                        "content": "Ao volante, dá para ver que o espaço disponível também lembra o do Tiguan, que se destaca nesse aspecto.O teto solar panorâmico ajuda a dar amplitude e a parte principal pode ser aberta também pelos passageiros de trás, que podem tomar um pouco de sol."
                    },
                    {
                        "type": "text",
                        "content": "Falando do banco traseiro, ao sentar na ponta observo que o vão até o banco da frente acomoda bem inclusive passageiros com 1,80 metro ou pouco mais. Apenas meu cabelo fica rente ao teto, mas minha cabeça não é pressionada.Nesse ponto o carro é tão bom quanto o Tiguan e pode dar trabalho para o Compass."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/OmzZ9bacwxZX2FPQ_xeuJi4Avs0=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_4.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "Ao iniciar o teste, ainda no estacionamento o Tarek prova que tem bom amortecimento ao rodar no piso de pedregulhos. Aumentando a velocidade para 40 km/h, sente-se mais trepidação;a suspensão independente nas quatro rodas tem seu lado firme e repassa um pouco de ruído, mas sem exageros."
                    },
                    {
                        "type": "text",
                        "content": "Ao andar em baixa, a direção elétrica mostra-se macia, mas a sensação de leveza fica impressionante mesmo nas manobras, feitas entre 3 km/h e 5 km/h. Você pode não sentir as mudanças nas curvas de assistência, porém o mecanismo da direção ganha peso linearmente e muda bem ao passar dos 30 km/h."
                    },
                    {
                        "type": "text",
                        "content": "Os motores também são conhecidos, os EA 888 1.4 de 150 cv e 25,5 kgfm da versão 250 TSI, e o 2.0 do 330 TSI, que gera 186 cv e 33,6 kgfm. O mais forte não chega ao ajuste esportivo dos 220 cv e 35,7 kgfm do Tiguan R-Line, mas, após testar a configuração, dá para notar que ele oferece força de sobra. A arrancada de zero a 100 km/h é cumprida em anunciados 7,8 segundos."
                    },
                    {
                        "type": "text",
                        "content": "O ajuste intermediário do 2.0 TSI vai servir também ao projeto dapicape média-pequena Tarok. Novidade na VW, o motor é utilizado no Brasil em carros como oAudi A4."
                    },
                    {
                        "type": "links",
                        "content": [
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/opiniao-os-multiplos-interesses-por-tras-da-alianca-entre-volkswagen-e-ford.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/noivado-entre-ford-e-volkswagen-nao-sera-uma-nova-autolatina.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2019/01/volkswagen-golf-de-nova-geracao-aparece-sem-disfarces-no-mcdonalds.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/volkswagen-amarok-v6-picape-mais-rapida-que-um-golf-turbo.html",
                            "https://revistaautoesporte.globo.com/Noticias/noticia/2018/12/volkswagen-diz-que-lancara-seu-ultimo-motor-combustao-em-2026.html"
                        ]
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/hZnVAKItg4fYTJrs2-uGw4YmJtw=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_47.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "O câmbio automático de dupla embreagem e sete velocidades ajuda na comunicação esperta com o motor.As trocas são feitas em apenas 0,2 segundo e a caixa pode fazer trocas duplas para passar ou diminuir marchas. Ao arrancar, sem que eu pudesse sentir, a transmissão pulou de primeira para terceira. O mesmo vale para reduções. Rodando a 40 km/h, basta pisar levemente no acelerador para o DSG jogar para segunda marcha de forma imperceptível."
                    },
                    {
                        "type": "text",
                        "content": "Não há nunca aquela sensação de \"parar para pensar\", uma hesitação do câmbio.Somente o motor guarda um pouco de turbo lag(atraso na entrada de turbina), mas basta passar dos 2.000 rpm para esse detalhe ficar para trás.E pode-se pisar à vontade, pois o sistema 4Motion de tração integral ajuda no off-road e também nas arrancadas mais empolgadas no asfalto."
                    },
                    {
                        "type": "text",
                        "content": "No modelo avaliado há alguns modos de gerenciamento capazes de alterar respostas de tração, direção, aceleração e outros pontos. Um deles diz respeito ao comando giratório, voltado para off-road (com modos Lama e Neve, entre outros)."
                    },
                    {
                        "type": "text",
                        "content": "Outro é o botão ao centro desse comando que permite ajustar a condução entre os modos Esporte, Econômico, Normal e Individual.O mais divertido é o último: pude regular da tração 4x4 ao ar-condicionado(para ficar mais econômico ou não). Até o controle de cruzeiro adaptativo pode ser ajustado para manter o VW próximo ou distante do carro que vai à frente."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/ny86WeIsR6UY1E1hJi7Vqqo72nA=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_60.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "Em geral, o Tarek tem várias qualidades em comum com os demais modelos da Volkswagen, seja na precisão da direção, seja nas respostas do motor e do câmbio. A dinâmica é acertada para um SUV médio.É espaçoso tanto para os que vão na frente quanto atrás."
                    },
                    {
                        "type": "text",
                        "content": "Eu tenho ressalvas em relação ao acabamento e ao porta-malas (de 374 litros no modelo chinês), inferiores aos de alguns concorrentes— o bagageiro é quase igual ao doT-Cross. De qualquer modo, a impressão é de que o SUV será bom de vendas."
                    },
                    {
                        "type": "text",
                        "content": "No Brasil, o 1.4 TSI será associado ao já manjado câmbio Tiptronic de seis marchas. É uma mudança esperada. Acreditamos que o 2.0 TSI mantenha o DSG de dupla embreagem. Qualquer um deles será mais ligeiro que o Compass 2.0 aspirado. A questão, contudo, é o preço.O Tarek vai ficar entre o T-Cross e o Tiguan, na casa dos R$ 120 mil."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/nyzuIARzPArK9WLMuMMmglTu8UY=/620x413/e.glbimg.com/og/ed/f/original/2019/01/30/volkswagen_tharu_7.jpeg"
                    },
                    {
                        "type": "text",
                        "content": "FICHA TÉCNICA"
                    },
                    {
                        "type": "text",
                        "content": "MotorDianteiro, transversal, 4 cilindros em linha, 2.0, 16V, comando duplo, turbo, injeção direta de gasolina"
                    },
                    {
                        "type": "text",
                        "content": "Potência186 cv a 6.000 rpm"
                    },
                    {
                        "type": "text",
                        "content": "Torque33,6 kgfm entre 1.500 e 4.000 rpm"
                    },
                    {
                        "type": "text",
                        "content": "CâmbioAutomático de dupla embreagem e 7 marchas; tração integral"
                    },
                    {
                        "type": "text",
                        "content": "DireçãoElétrica"
                    },
                    {
                        "type": "text",
                        "content": "SuspensãoIndependente McPherson (dianteira) e Multilink (traseira)"
                    },
                    {
                        "type": "text",
                        "content": "FreiosDiscos ventilados (dianteiro) e discos sólidos (traseiro)"
                    },
                    {
                        "type": "text",
                        "content": "Pneus e rodas215/50 R18"
                    },
                    {
                        "type": "text",
                        "content": "DimensõesComprimento: 4,45 mLargura: 1,84 mAltura: 1,63 mEntre-eixos: 2,68 m"
                    },
                    {
                        "type": "text",
                        "content": "Tanque de combustível56,5 litros"
                    },
                    {
                        "type": "text",
                        "content": "Volume do porta-malas374 litros (fabricante)"
                    },
                    {
                        "type": "text",
                        "content": "Peso(ordem de marcha)1.590 kg"
                    },
                    {
                        "type": "text",
                        "content": "Central multimídia10,1 pol., sensível ao toque; Android Auto e Carplay"
                    },
                    {
                        "type": "text",
                        "content": "Garantia3 anos"
                    }
                ]
            }
        }
    ]
}
```
