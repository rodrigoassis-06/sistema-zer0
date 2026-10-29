from pydantic import BaseModel
from typing import List
from decimal import Decimal
from app.schemas.appointment import AppointmentResponse
from app.schemas.transaction import FinancialSummary

class AppointmentMetrics(BaseModel):
    total_today: int
    pending_today: int
    confirmed_today: int
    completed_today: int

class DashboardOverview(BaseModel):
    appointment_metrics: AppointmentMetrics
    financial_summary_month: FinancialSummary
    upcoming_appointments: List[AppointmentResponse]

