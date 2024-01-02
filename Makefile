#!make
include .env

requirements:
	pip install -r requirements.txt


docker-compose-up:
	docker compose up -d


run:
	python src/main.py
