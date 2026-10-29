from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TenantBase(BaseModel):
    name: str
    slug: str
    document: Optional[str] = None
    is_active: bool = True

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

