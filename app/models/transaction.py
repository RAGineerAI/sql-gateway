"""
Модель транзакции.

Пример модели для демонстрации.
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Transaction(Base):
    """Транзакция (доход или расход)."""
    
    __tablename__ = "transactions"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    currency: Mapped[str] = mapped_column(String(3), default="RUB")
    description: Mapped[str] = mapped_column(String(500), default="")
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
