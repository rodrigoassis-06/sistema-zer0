from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse

router = APIRouter(prefix="/services", tags=["Serviços"])

@router.get("/", response_model=List[ServiceResponse])
def list_services(
    active_only: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Service).filter(Service.tenant_id == current_user.tenant_id)
    if active_only:
        query = query.filter(Service.is_active.is_(True))
    return query.order_by(Service.name.asc()).all()

@router.post("/", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(
    service_in: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = Service(
        tenant_id=current_user.tenant_id,
        **service_in.model_dump()
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(
    service_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = db.query(Service).filter(
        Service.id == service_id,
        Service.tenant_id == current_user.tenant_id
    ).first()
    if not service:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return service

@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(
    service_id: str,
    service_in: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = db.query(Service).filter(
        Service.id == service_id,
        Service.tenant_id == current_user.tenant_id
    ).first()
    if not service:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    for field, val in service_in.model_dump(exclude_unset=True).items():
        setattr(service, field, val)

    db.commit()
    db.refresh(service)
    return service

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = db.query(Service).filter(
        Service.id == service_id,
        Service.tenant_id == current_user.tenant_id
    ).first()
    if not service:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    db.delete(service)
    db.commit()
    return None

