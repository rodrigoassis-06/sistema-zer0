import pytest
from datetime import datetime, timedelta, timezone, date
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database import Base
from app.api.deps import get_db
from app.main import app

from sqlalchemy.pool import StaticPool

# Test database in memory with StaticPool so all connections share the memory DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

def test_full_system_flow(client):
    # 1. Register Tenant A
    resp_a = client.post("/api/v1/auth/register", json={
        "company_name": "Clinica Alfa",
        "admin_name": "Dr. Alfa",
        "email": "alfa@clinica.com",
        "password": "secretpassword"
    })
    assert resp_a.status_code == 201
    token_a = resp_a.json()["access_token"]
    headers_a = {"Authorization": f"Bearer {token_a}"}

    # 2. Register Tenant B (to test multi-tenant isolation)
    resp_b = client.post("/api/v1/auth/register", json={
        "company_name": "Studio Beta",
        "admin_name": "Ana Beta",
        "email": "beta@studio.com",
        "password": "secretpassword"
    })
    assert resp_b.status_code == 201
    token_b = resp_b.json()["access_token"]
    headers_b = {"Authorization": f"Bearer {token_b}"}

    # 3. Create Service for Tenant A
    srv_resp = client.post("/api/v1/services/", headers=headers_a, json={
        "name": "Consulta Inicial",
        "description": "Avaliação clínica",
        "duration_minutes": 30,
        "price": 120.00
    })
    assert srv_resp.status_code == 201
    service_a_id = srv_resp.json()["id"]

    # Verify Tenant B does NOT see Tenant A's service
    list_b = client.get("/api/v1/services/", headers=headers_b)
    assert len(list_b.json()) == 0

    # 4. Create Customer for Tenant A
    cust_resp = client.post("/api/v1/customers/", headers=headers_a, json={
        "name": "João Paciente",
        "phone": "11999998888",
        "email": "joao@email.com"
    })
    assert cust_resp.status_code == 201
    customer_a_id = cust_resp.json()["id"]

    # Verify Tenant B cannot access Tenant A's customer
    cust_b_access = client.get(f"/api/v1/customers/{customer_a_id}", headers=headers_b)
    assert cust_b_access.status_code == 404

    # 5. Create Appointment for Tenant A (Tomorrow at 10:00)
    now = datetime.now()
    start_time_1 = (now + timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0)
    appt_resp = client.post("/api/v1/appointments/", headers=headers_a, json={
        "customer_id": customer_a_id,
        "service_id": service_a_id,
        "start_time": start_time_1.isoformat()
    })
    assert appt_resp.status_code == 201
    appt_1_id = appt_resp.json()["id"]

    # 6. Test Conflict Detection (Same professional/time overlap)
    conflict_time = start_time_1 + timedelta(minutes=10) # 10 minutes into the 30-min slot
    conflict_resp = client.post("/api/v1/appointments/", headers=headers_a, json={
        "customer_id": customer_a_id,
        "service_id": service_a_id,
        "start_time": conflict_time.isoformat()
    })
    assert conflict_resp.status_code == 409
    assert "Conflito de horário" in conflict_resp.json()["detail"]

    # 7. Complete Appointment and trigger financial entry
    complete_resp = client.post(
        f"/api/v1/appointments/{appt_1_id}/complete",
        headers=headers_a,
        json={"generate_financial_entry": True, "payment_method": "PIX"}
    )
    assert complete_resp.status_code == 200
    assert complete_resp.json()["status"] == "COMPLETED"

    # 8. Check that Financial Transaction was created automatically
    trx_list = client.get("/api/v1/financial/transactions", headers=headers_a)
    assert trx_list.status_code == 200
    transactions = trx_list.json()
    assert len(transactions) == 1
    assert transactions[0]["type"] == "INCOME"
    assert transactions[0]["status"] == "PAID"
    assert float(transactions[0]["amount"]) == 120.00
    assert transactions[0]["payment_method"] == "PIX"

    # 9. Test Financial Summary
    summary_resp = client.get("/api/v1/financial/summary", headers=headers_a)
    assert summary_resp.status_code == 200
    summary = summary_resp.json()
    assert float(summary["total_income_paid"]) == 120.00
    assert float(summary["net_realized_balance"]) == 120.00

    # 10. Test Dashboard Overview
    dash_resp = client.get("/api/v1/dashboard/overview", headers=headers_a)
    assert dash_resp.status_code == 200
    dash_data = dash_resp.json()
    assert "appointment_metrics" in dash_data
    assert "financial_summary_month" in dash_data
