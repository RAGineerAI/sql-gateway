# 🗄️ SQL Gateway

[![Status](https://img.shields.io/badge/status-MVP_completed-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-✓-009688.svg)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)]()

FastAPI-сервис для безопасного доступа к PostgreSQL.

**Ключевая идея:** AI-агенты и CRM не ходят в БД напрямую — только через API.

## 🎯 Что умеет

- ✅ REST API (FastAPI)
- ✅ Асинхронная работа с PostgreSQL
- ✅ Валидация данных (Pydantic)
- ✅ Миграции (Alembic)
- ✅ Health checks (`/health`, `/health/db`)
- ✅ Swagger UI (`/docs`)

## 🚀 Быстрый старт

```bash
# 1. Клонировать
git clone https://github.com/RAGineerAI/sql-gateway.git
cd sql-gateway

# 2. Окружение
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Настроить .env
cp .env.example .env
nano .env

# 4. Запустить PostgreSQL
docker compose up -d

# 5. Миграции
alembic upgrade head

# 6. Запустить API
uvicorn app.main:app --reload
```
## 📊 Пример

**Создать транзакцию:**

```bash
curl -X POST http://localhost:8000/api/transactions \
  -H "Content-Type: application/json" \
  -d '{"amount": 1000, "description": "Тест"}'
```
**Ответ:**

```json
{
  "id": 1,
  "amount": "1000.00",
  "currency": "RUB",
  "description": "Тест",
  "created_at": "2026-11-14T..."
}
```
## 🏗️ Архитектура

```text
Клиент → FastAPI → PostgreSQL
           ↓
     Pydantic + SQLAlchemy
```
**Подробно:** [docs/ARCHITECTURE.md](https://docs/ARCHITECTURE.md)
## 📁 Структура

```text

sql-gateway/
├── app/
│   ├── api/           # Эндпоинты
│   ├── core/          # Настройки
│   ├── db/            # Подключение к БД
│   ├── models/        # ORM-модели
│   ├── schemas/       # Pydantic-схемы
│   └── main.py        # FastAPI
├── migrations/        # Alembic
├── docs/              # Документация
└── docker-compose.yml
```
## 🛠️ Стек

|Компонент|Технология|
|---|---|
|API|FastAPI|
|БД|PostgreSQL 16|
|ORM|SQLAlchemy 2.0 (async)|
|Миграции|Alembic|
|Валидация|Pydantic 2|
|Драйвер|asyncpg|

## 👤 Автор

**RAGineerAI** — [GitHub](https://github.com/RAGineerAI)

## 📄 Лицензия

MIT