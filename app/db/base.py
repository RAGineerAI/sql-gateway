"""
Базовый класс для всех моделей.

Все модели наследуются от Base.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Базовый класс для ORM-моделей."""
    pass