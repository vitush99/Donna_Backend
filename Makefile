.PHONY: run migrate revision test lint format typecheck docker-up

run:
	uvicorn donna.main:app --reload

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate -m "$(m)"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .
	ruff check . --fix

typecheck:
	mypy src

docker-up:
	docker compose up --build
