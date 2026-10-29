from datetime import datetime, date, time
from decimal import Decimal
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.appointment import Appointment
from app.models.transaction import Transaction
from app.schemas.dashboard import DashboardOverview, AppointmentMetrics
from app.schemas.transaction import FinancialSummary

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/overview", response_model=DashboardOverview)
def get_dashboard_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    today = date.today()
    start_of_today = datetime.combine(today, time.min)
    end_of_today = datetime.combine(today, time.max)

    # 1. Appointments Today
    today_appts = db.query(Appointment).filter(
        Appointment.tenant_id == current_user.tenant_id,
        Appointment.start_time >= start_of_today,
        Appointment.start_time <= end_of_today
    ).all()

    total_today = len(today_appts)
    pending_today = sum(1 for a in today_appts if a.status == "PENDING")
    confirmed_today = sum(1 for a in today_appts if a.status == "CONFIRMED")
    completed_today = sum(1 for a in today_appts if a.status == "COMPLETED")

    appointment_metrics = AppointmentMetrics(
        total_today=total_today,
        pending_today=pending_today,
        confirmed_today=confirmed_today,
        completed_today=completed_today
    )

    # 2. Financial Summary of the Month
    def sum_by(trx_type: str, trx_status: str) -> Decimal:
        val = (
            db.query(func.coalesce(func.sum(Transaction.amount), 0))
            .filter(
                Transaction.tenant_id == current_user.tenant_id,
                Transaction.type == trx_type,
                Transaction.status == trx_status,
                func.extract("month", Transaction.due_date) == today.month,
                func.extract("year", Transaction.due_date) == today.year
            )
            .scalar()
        )
        return Decimal(str(val))

    income_paid = sum_by("INCOME", "PAID")
    income_pending = sum_by("INCOME", "PENDING")
    expense_paid = sum_by("EXPENSE", "PAID")
    expense_pending = sum_by("EXPENSE", "PENDING")

    financial_summary = FinancialSummary(
        total_income_paid=income_paid,
        total_income_pending=income_pending,
        total_expense_paid=expense_paid,
        total_expense_pending=expense_pending,
        net_realized_balance=income_paid - expense_paid,
        net_projected_balance=(income_paid + income_pending) - (expense_paid + expense_pending)
    )

    # 3. Next 5 Upcoming Appointments
    now = datetime.now()
    upcoming = (
        db.query(Appointment)
        .options(joinedload(Appointment.customer), joinedload(Appointment.service))
        .filter(
            Appointment.tenant_id == current_user.tenant_id,
            Appointment.start_time >= now,
            Appointment.status.in_(["PENDING", "CONFIRMED"])
        )
        .order_by(Appointment.start_time.asc())
        .limit(5)
        .all()
    )

    return DashboardOverview(
        appointment_metrics=appointment_metrics,
        financial_summary_month=financial_summary,
        upcoming_appointments=upcoming
    )

