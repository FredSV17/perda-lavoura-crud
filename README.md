# perda-lavoura-crud
CRUD que permite cadastrar perdas nas lavouras

O backend foi feito utilizando python, com o framework flask.

O frontend foi feito utilizando angular.

O banco de dados utilizado foi MySQL.

O código foi implementado e testado utilizando uma máquina virtual Ubuntu 20.04.

# Como instalar

Primeiramente, é necessário instalar o docker, abaixo está o link com os passos para instalar o docker:

https://docs.docker.com/engine/install/ubuntu/

Após isso, é necessário instalar o libmysqlclient, make e npm:

    sudo apt-get install libmysqlclient-dev 
    sudo apt-get install make
    sudo apt-get install npm
É necessário também instalar o node e o angular client:

    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
    npm install -g @angular/cli@latest

Com isso podemos instalar as dependências dentro do projeto para começar a executar suas partes.

## Para rodar o banco de dados
Dentro da pasta raíz do projeto, execute os seguintes comandos:

    sudo make build-img-sql
    sudo make run-sql
Verifique se o container está rodando com:

    docker ps
Deverá haver um container listado:

    CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
    fa749fd9252a   imgsql    "docker-entrypoint.s…"   4 seconds ago   Up 2 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sqlcontainer

O banco de dados está executando na porta 3306.

## Para rodar a API:
### Os passos a seguir são para testar a API e executá-la sem docker:
Para o bom funcionamento da API, é necessário que o container SQL esteja executando.

Crie um ambiente virtual na pasta /api:

    python3 -m venv venv
Instale o pip:
    
    sudo apt-get install python3-pip
Ative o ambiente virtual e instale as dependências:
    
    source venv/bin/activate
    pip3 install -r requirements.txt
Para apenas executar a api, use o seguinte comando dentro da pasta raíz:

    sudo make run-api

A aplicação está executando na porta 5000.

Para executar os testes na api, use o seguinte comando dentro da pasta raíz:

    sudo make test-api


## Para rodar a API (Docker):
Dentro da pasta raíz do projeto, execute os seguintes comandos:

    sudo make build-img-api
    sudo make run-api-docker

Verifique se o container está rodando com:

    docker ps
Deverá haver dois containers listados:

    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                                  NAMES
    cbef165202e8   imgapi    "python3 -m flask --…"   4 seconds ago    Up 2 seconds    0.0.0.0:5000->5000/tcp, :::5000->5000/tcp              apicontainer
    fa749fd9252a   imgsql    "docker-entrypoint.s…"   11 minutes ago   Up 11 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   sqlcontainer

O container da API está executando na porta 5000.

## Para rodar o frontend:
Para o bom funcionamento do frontend, é necessário que o banco de dados e a API (dockerizada ou não) estejam sendo executados.

Dentro da pasta /frontend, execute o seguinte comando:
    
    npm install
Volte para a pasta raíz, e execute o comando:

    sudo make run-front
O frontend estará executando na porta 4200.

## Para rodar o frontend (docker):
Para o bom funcionamento do frontend, é necessário que o banco de dados e a API (dockerizada ou não) estejam sendo executados.

Dentro da pasta raíz do projeto, execute os seguintes comandos:

    sudo make build-img-front
    sudo make run-front-docker

Verifique se o container está rodando com:

    docker ps
Deverá haver três container listados:

    CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                                   NAMES
    7f34531814da   imgfront   "/docker-entrypoint.…"   6 seconds ago    Up 4 seconds    0.0.0.0:8080->80/tcp, :::8080->80/tcp                   frontcontainer
    cbef165202e8   imgapi     "python3 -m flask --…"   8 minutes ago    Up 8 minutes    0.0.0.0:5000->5000/tcp, :::5000->5000/tcp               apicontainer
    fa749fd9252a   imgsql     "docker-entrypoint.s…"   19 minutes ago   Up 19 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp    sqlcontainer

O container do front está executando na porta 8080.
