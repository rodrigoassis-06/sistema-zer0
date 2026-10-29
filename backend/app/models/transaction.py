import uuid
from datetime import datetime, date, timezone
from sqlalchemy import Column, String, Text, Numeric, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False, index=True)
    customer_id = Column(String(36), ForeignKey("customers.id", ondelete="SET NULL"), nullable=True, index=True)
    appointment_id = Column(String(36), ForeignKey("appointments.id", ondelete="SET NULL"), nullable=True, index=True)
    
    type = Column(String(20), nullable=False) # INCOME, EXPENSE
    category = Column(String(80), nullable=False, default="Geral")
    amount = Column(Numeric(10, 2), nullable=False)
    due_date = Column(Date, nullable=False, default=date.today)
    payment_date = Column(Date, nullable=True)
    status = Column(String(20), default="PENDING", index=True) # PENDING, PAID, CANCELLED
    payment_method = Column(String(30), nullable=True) # PIX, CREDIT_CARD, DEBIT_CARD, CASH, TRANSFER
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    tenant = relationship("Tenant", back_populates="transactions")
    customer = relationship("Customer", back_populates="transactions")
    appointment = relationship("Appointment", back_populates="transaction")

