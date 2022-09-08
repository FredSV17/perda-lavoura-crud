export SQL_CONTAINER=sqlcontainer
export SQL_CONNECTION=localhost
PROJ_NETWORK=projnetwork
IMAGE_SQL=imgsql
IMAGE_API=imgapi
IMAGE_FRONT=imgfront
API_CONTAINER=apicontainer
FRONT_CONTAINER=frontcontainer
SHELL := /bin/bash

create-network:
	docker network create $(PROJ_NETWORK)

run-sql:
	docker run --name $(SQL_CONTAINER) --rm --network $(PROJ_NETWORK) -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=1 $(IMAGE_SQL) 

build-img-sql:
	cd db ; \
	docker build -t $(IMAGE_SQL) .
	
build-img-api:
	cd api ; \
	docker build -t $(IMAGE_API) .
	
build-img-front:
	cd frontend ; \
	docker build -t $(IMAGE_FRONT) .	
	
run-api-docker:
	docker run --name $(API_CONTAINER) --rm --network projnetwork -d -p 5000:5000 -e SQL_CONNECTION=$(SQL_CONTAINER) $(IMAGE_API)

run-api:
	cd api ; \
	source venv/bin/activate ; \
	python3 -m flask --app main run --host=0.0.0.0

test-api:
	cd api ; \
	source venv/bin/activate ; \
	python3 -m pytest

run-front:
	cd frontend ; \
	ng serve

run-front-docker:
	docker run --name $(FRONT_CONTAINER) -d -p 8080:80 imgfront 
	
