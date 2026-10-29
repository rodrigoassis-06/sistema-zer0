from datetime import date
from typing import List, Optional
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.transaction import Transaction
from app.models.customer import Customer
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
    FinancialSummary
)

router = APIRouter(prefix="/financial", tags=["Financeiro"])

@router.get("/transactions", response_model=List[TransactionResponse])
def list_transactions(
    type: Optional[str] = Query(None, description="INCOME ou EXPENSE"),
    status: Optional[str] = Query(None, description="PENDING, PAID, CANCELLED"),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Transaction).filter(Transaction.tenant_id == current_user.tenant_id)
    if type:
        query = query.filter(Transaction.type == type)
    if status:
        query = query.filter(Transaction.status == status)
    if start_date:
        query = query.filter(Transaction.due_date >= start_date)
    if end_date:
        query = query.filter(Transaction.due_date <= end_date)
    if category:
        query = query.filter(Transaction.category == category)

    return query.order_by(Transaction.due_date.desc(), Transaction.created_at.desc()).all()

@router.post("/transactions", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(
    trx_in: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if trx_in.customer_id:
        cust = db.query(Customer).filter(
            Customer.id == trx_in.customer_id,
            Customer.tenant_id == current_user.tenant_id
        ).first()
        if not cust:
            raise HTTPException(status_code=404, detail="Cliente associado não encontrado")

    trx = Transaction(
        tenant_id=current_user.tenant_id,
        **trx_in.model_dump()
    )
    db.add(trx)
    db.commit()
    db.refresh(trx)
    return trx

@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    trx = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.tenant_id == current_user.tenant_id
    ).first()
    if not trx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return trx

@router.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction(
    transaction_id: str,
    trx_in: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    trx = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.tenant_id == current_user.tenant_id
    ).first()
    if not trx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    for field, val in trx_in.model_dump(exclude_unset=True).items():
        setattr(trx, field, val)

    db.commit()
    db.refresh(trx)
    return trx

@router.delete("/transactions/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(
    transaction_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    trx = db.query(Transaction).filter(
        Transaction.id == transaction_id,
        Transaction.tenant_id == current_user.tenant_id
    ).first()
    if not trx:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    db.delete(trx)
    db.commit()
    return None

@router.get("/summary", response_model=FinancialSummary)
def get_financial_summary(
    month: Optional[int] = Query(None, ge=1, le=12),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()
    target_month = month or today.month
    target_year = year or today.year

    # Helper to sum amounts
    def sum_by(trx_type: str, trx_status: str) -> Decimal:
        val = (
            db.query(func.coalesce(func.sum(Transaction.amount), 0))
            .filter(
                Transaction.tenant_id == current_user.tenant_id,
                Transaction.type == trx_type,
                Transaction.status == trx_status,
                func.extract("month", Transaction.due_date) == target_month,
                func.extract("year", Transaction.due_date) == target_year
            )
            .scalar()
        )
        return Decimal(str(val))

    income_paid = sum_by("INCOME", "PAID")
    income_pending = sum_by("INCOME", "PENDING")
    expense_paid = sum_by("EXPENSE", "PAID")
    expense_pending = sum_by("EXPENSE", "PENDING")

    net_realized = income_paid - expense_paid
    net_projected = (income_paid + income_pending) - (expense_paid + expense_pending)

    return FinancialSummary(
        total_income_paid=income_paid,
        total_income_pending=income_pending,
        total_expense_paid=expense_paid,
        total_expense_pending=expense_pending,
        net_realized_balance=net_realized,
        net_projected_balance=net_projected
    )

