run-sql:
	docker run --name sqlcontainer -d -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=1 imgsql 

run-api-docker:
	docker run --name apicontainer -d -p 5000:5000 docker-api

run-api:
	python3 -m flask --app main run --host=0.0.0.0

test-api:
	python3 -m pytest