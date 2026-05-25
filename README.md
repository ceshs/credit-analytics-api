# Credit Analytics API

Backend em FastAPI para importacao, analise e insights de credito.

## Stack

- FastAPI
- Uvicorn
- Pandas
- SQLAlchemy
- Alembic
- Pydantic
- Openpyxl
- Psycopg2

## Setup local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000/api/health
```

Docs:

```text
http://127.0.0.1:8000/docs
```

## Docker

```bash
docker compose up --build
```

API:

```text
http://127.0.0.1:8000/api/health
```

Postgres:

```text
localhost:5432
database: credit_analytics
user: postgres
password: postgres
```

Health check do banco:

```text
http://127.0.0.1:8000/api/health/db
```

## Banco de dados

O backend usa Postgres via SQLAlchemy e migrations com Alembic.

Subir API + banco:

```bash
docker compose up --build -d
```

Rodar migrations:

```bash
docker compose exec api alembic upgrade head
```

Criar uma migration a partir dos models:

```bash
docker compose exec api alembic revision --autogenerate -m "create tables"
```

Abrir o `psql` no container:

```bash
docker compose exec db psql -U postgres -d credit_analytics
```

## Postman

Importe os arquivos:

```text
postman/credit-analytics-api.postman_collection.json
postman/local.postman_environment.json
```

Selecione o environment `Credit Analytics Local` e rode:

```text
GET {{base_url}}/api/health
```
