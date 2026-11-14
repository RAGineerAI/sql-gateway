"""
Главный модуль FastAPI.

Точка входа приложения.
"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.transactions import router as transactions_router
from app.db.session import get_db

app = FastAPI(
    title="SQL Gateway",
    description="Безопасный доступ к PostgreSQL",
    version="0.1.0"
)

# Подключаем роутеры
app.include_router(transactions_router)


@app.get("/health")
async def health_check():
    """Проверка работоспособности"""
    return {"status": "ok"}

@app.get("/health/db")
async def health_db(db: AsyncSession = Depends(get_db)):
    """Проверка подключения к БД."""
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"БД недоступна: {e}")