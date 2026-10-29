from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import date, datetime

class TransactionBase(BaseModel):
    customer_id: Optional[str] = None
    appointment_id: Optional[str] = None
    type: str # INCOME, EXPENSE
    category: str = "Geral"
    amount: Decimal
    due_date: date
    payment_date: Optional[date] = None
    status: str = "PENDING" # PENDING, PAID, CANCELLED
    payment_method: Optional[str] = None # PIX, CREDIT_CARD, DEBIT_CARD, CASH, TRANSFER
    notes: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    customer_id: Optional[str] = None
    category: Optional[str] = None
    amount: Optional[Decimal] = None
    due_date: Optional[date] = None
    payment_date: Optional[date] = None
    status: Optional[str] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None

class TransactionResponse(TransactionBase):
    id: str
    tenant_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class FinancialSummary(BaseModel):
    total_income_paid: Decimal
    total_income_pending: Decimal
    total_expense_paid: Decimal
    total_expense_pending: Decimal
    net_realized_balance: Decimal
    net_projected_balance: Decimal

