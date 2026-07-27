# Developer Landing Backend

Бэкенд-сервис для лендинг-презентации разработчика с интеграцией AI

## Стек

- Python 3.12
- FastAPI
- Poetry
- Docker
- OpenAI API

## Запуск

### Через Poetry

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

### Через Docker
```bash
docker compose up --build
```
