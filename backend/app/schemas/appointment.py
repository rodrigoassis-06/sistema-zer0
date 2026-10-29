from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.schemas.customer import CustomerResponse
from app.schemas.service import ServiceResponse

class AppointmentBase(BaseModel):
    customer_id: str
    service_id: str
    professional_id: Optional[str] = None
    start_time: datetime
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    customer_id: Optional[str] = None
    service_id: Optional[str] = None
    professional_id: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[str] = None # PENDING, CONFIRMED, COMPLETED, CANCELLED
    notes: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: str
    tenant_id: str
    customer_id: str
    service_id: str
    professional_id: Optional[str] = None
    start_time: datetime
    end_time: datetime
    status: str
    notes: Optional[str] = None
    created_at: datetime
    customer: Optional[CustomerResponse] = None
    service: Optional[ServiceResponse] = None

    model_config = ConfigDict(from_attributes=True)

class AppointmentCompleteRequest(BaseModel):
    generate_financial_entry: bool = True
    payment_method: Optional[str] = "PIX"
    payment_date: Optional[datetime] = None

