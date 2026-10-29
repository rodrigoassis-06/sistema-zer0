import uuid
from sqlalchemy import Column, String, Integer, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class BusinessHours(Base):
    __tablename__ = "business_hours"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False, index=True)
    day_of_week = Column(Integer, nullable=False) # 0=Monday .. 6=Sunday
    open_time = Column(Time, nullable=True)
    close_time = Column(Time, nullable=True)
    is_closed = Column(Boolean, default=False)

    tenant = relationship("Tenant", back_populates="business_hours")

