include .env

install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py service/*.py

lint:
	pylint --errors-only --disable=R,C *.py service/*.py

test:
	python -m pytest tests

deploy:
	docker build -t transactions-app .

run:
	docker network create data-network || true &&\
	docker run --name=transactions-app-service --net=data-network -p 127.0.0.1:$(PORT):$(PORT) transactions-app 

all: install lint test deploy