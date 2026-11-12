"""
Подключение к PostgreSQL.

Создаёт engine и фабрику сессий.
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings

# Асинхронный движок
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,       # логировать SQL в DEBUG
    pool_size=5,               # базовый пул
    max_overflow=10,           # дополнительно
    pool_pre_ping=True,        # проверять соединение
)

# Фабрика сессий
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    """Dependency для FastAPI: открывает сессию и закрывает после."""
    async with async_session_maker() as session:
        yield session