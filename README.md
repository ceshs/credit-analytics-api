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
