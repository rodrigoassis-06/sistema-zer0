from datetime import datetime, timedelta, date, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.customer import Customer
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.transaction import Transaction
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
    AppointmentCompleteRequest
)

router = APIRouter(prefix="/appointments", tags=["Agendamentos"])

def check_time_conflict(
    db: Session,
    tenant_id: str,
    start_time: datetime,
    end_time: datetime,
    professional_id: Optional[str] = None,
    exclude_id: Optional[str] = None
) -> bool:
    query = db.query(Appointment).filter(
        Appointment.tenant_id == tenant_id,
        Appointment.status.in_(["PENDING", "CONFIRMED"]),
        Appointment.start_time < end_time,
        Appointment.end_time > start_time
    )
    if professional_id:
        query = query.filter(Appointment.professional_id == professional_id)
    if exclude_id:
        query = query.filter(Appointment.id != exclude_id)
    return query.first() is not None

@router.get("/", response_model=List[AppointmentResponse])
def list_appointments(
    start_date: Optional[datetime] = Query(None, description="Início do intervalo"),
    end_date: Optional[datetime] = Query(None, description="Fim do intervalo"),
    status: Optional[str] = Query(None, description="Filtrar por status"),
    customer_id: Optional[str] = Query(None),
    professional_id: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = (
        db.query(Appointment)
        .options(joinedload(Appointment.customer), joinedload(Appointment.service))
        .filter(Appointment.tenant_id == current_user.tenant_id)
    )
    if start_date:
        query = query.filter(Appointment.start_time >= start_date)
    if end_date:
        query = query.filter(Appointment.start_time <= end_date)
    if status:
        query = query.filter(Appointment.status == status)
    if customer_id:
        query = query.filter(Appointment.customer_id == customer_id)
    if professional_id:
        query = query.filter(Appointment.professional_id == professional_id)

    return query.order_by(Appointment.start_time.asc()).all()

@router.post("/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(
    appointment_in: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    customer = db.query(Customer).filter(
        Customer.id == appointment_in.customer_id,
        Customer.tenant_id == current_user.tenant_id
    ).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    service = db.query(Service).filter(
        Service.id == appointment_in.service_id,
        Service.tenant_id == current_user.tenant_id
    ).first()
    if not service:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    professional_id = appointment_in.professional_id or current_user.id
    end_time = appointment_in.start_time + timedelta(minutes=service.duration_minutes)

    if check_time_conflict(db, current_user.tenant_id, appointment_in.start_time, end_time, professional_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Conflito de horário: o profissional já possui agendamento neste horário."
        )

    appointment = Appointment(
        tenant_id=current_user.tenant_id,
        customer_id=customer.id,
        service_id=service.id,
        professional_id=professional_id,
        start_time=appointment_in.start_time,
        end_time=end_time,
        status="CONFIRMED",
        notes=appointment_in.notes
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(
    appointment_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointment = (
        db.query(Appointment)
        .options(joinedload(Appointment.customer), joinedload(Appointment.service))
        .filter(
            Appointment.id == appointment_id,
            Appointment.tenant_id == current_user.tenant_id
        ).first()
    )
    if not appointment:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return appointment

@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(
    appointment_id: str,
    appointment_in: AppointmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.tenant_id == current_user.tenant_id
    ).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    new_start = appointment_in.start_time or appointment.start_time
    service = appointment.service
    if appointment_in.service_id and appointment_in.service_id != appointment.service_id:
        service = db.query(Service).filter(
            Service.id == appointment_in.service_id,
            Service.tenant_id == current_user.tenant_id
        ).first()
        if not service:
            raise HTTPException(status_code=404, detail="Serviço não encontrado")

    new_end = new_start + timedelta(minutes=service.duration_minutes)
    professional_id = appointment_in.professional_id or appointment.professional_id

    if (new_start != appointment.start_time or new_end != appointment.end_time or professional_id != appointment.professional_id):
        if check_time_conflict(db, current_user.tenant_id, new_start, new_end, professional_id, exclude_id=appointment.id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Conflito de horário no reagendamento."
            )

    appointment.start_time = new_start
    appointment.end_time = new_end
    if appointment_in.customer_id:
        appointment.customer_id = appointment_in.customer_id
    if appointment_in.service_id:
        appointment.service_id = appointment_in.service_id
    if appointment_in.professional_id:
        appointment.professional_id = appointment_in.professional_id
    if appointment_in.status:
        appointment.status = appointment_in.status
    if appointment_in.notes is not None:
        appointment.notes = appointment_in.notes

    db.commit()
    db.refresh(appointment)
    return appointment


@router.post("/{appointment_id}/complete", response_model=AppointmentResponse)
def complete_appointment(
    appointment_id: str,
    complete_in: AppointmentCompleteRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointment = (
        db.query(Appointment)
        .options(joinedload(Appointment.service))
        .filter(
            Appointment.id == appointment_id,
            Appointment.tenant_id == current_user.tenant_id
        ).first()
    )
    if not appointment:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    appointment.status = "COMPLETED"

    if complete_in.generate_financial_entry:
        existing_trx = db.query(Transaction).filter(
            Transaction.appointment_id == appointment.id,
            Transaction.tenant_id == current_user.tenant_id
        ).first()
        if not existing_trx:
            pay_date = complete_in.payment_date.date() if complete_in.payment_date else date.today()
            trx = Transaction(
                tenant_id=current_user.tenant_id,
                customer_id=appointment.customer_id,
                appointment_id=appointment.id,
                type="INCOME",
                category="Serviços",
                amount=appointment.service.price,
                due_date=pay_date,
                payment_date=pay_date,
                status="PAID",
                payment_method=complete_in.payment_method or "PIX",
                notes=f"Recebimento referente ao agendamento #{appointment.id[:8]} - {appointment.service.name}"
            )
            db.add(trx)

    db.commit()
    db.refresh(appointment)
    return appointment

@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(
    appointment_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.tenant_id == current_user.tenant_id
    ).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    db.delete(appointment)
    db.commit()
    return None


