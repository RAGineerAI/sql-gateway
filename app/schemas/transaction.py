"""
Pydantic-схемы для Transaction.

Описывают формат данных в API.
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
    """Общие поля для всех схем."""
    
    amount: Decimal = Field(..., gt=0, description="Сумма (> 0)")
    currency: str = Field(default="RUB", max_length=3)
    description: str = Field(default="", max_length=500)


class TransactionCreate(TransactionBase):
    """Схема для создания транзакции."""
    pass


class TransactionRead(TransactionBase):
    """Схема для ответа."""
    
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}


class TransactionUpdate(BaseModel):
    """Схема для обновления (все поля опциональны)."""
    
    amount: Optional[Decimal] = Field(None, gt=0)
    description: Optional[str] = Field(None, max_length=500)