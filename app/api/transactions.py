"""
API для транзакций.

Эндпоинты:
    - POST /api/transactions — создать
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionRead

router = APIRouter(prefix="/api/transactions", tags=["transactions"])


@router.post(
    "",
    response_model=TransactionRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_transaction(
    data: TransactionCreate,
    db: AsyncSession = Depends(get_db),
):
    """Создать новую транзакцию."""
    transaction = Transaction(**data.model_dump())

    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)
    # 2. Возвращаем объект. FastAPI сам превратит его в JSON
    #    по модели TransactionRead
    return transaction