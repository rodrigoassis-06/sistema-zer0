import sys
import os
from datetime import datetime, date, timedelta, time
from decimal import Decimal

# Ensure current directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.database import SessionLocal, engine, Base
import app.models
from app.core.security import get_password_hash
from app.models.tenant import Tenant
from app.models.user import User
from app.models.customer import Customer
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.transaction import Transaction

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 1. Check or Create Tenant
        tenant = db.query(Tenant).filter(Tenant.slug == "demo-business").first()
        if not tenant:
            tenant = Tenant(
                name="Empresa Modelo Demo",
                slug="demo-business",
                document="12.345.678/0001-90",
                is_active=True
            )
            db.add(tenant)
            db.flush()
            print(f"[+] Tenant criado: {tenant.name} ({tenant.slug})")

        # 2. Check or Create Admin User
        admin_email = "admin@demo.com"
        admin_user = db.query(User).filter(User.email == admin_email).first()
        if not admin_user:
            admin_user = User(
                tenant_id=tenant.id,
                name="Administrador Master",
                email=admin_email,
                password_hash=get_password_hash("admin123"),
                role="ADMIN",
                is_active=True
            )
            db.add(admin_user)
            db.flush()
            print(f"[+] Usuário Admin criado: {admin_user.email} / senha: admin123")

        # 3. Services
        existing_services = db.query(Service).filter(Service.tenant_id == tenant.id).count()
        services_data = []
        if existing_services == 0:
            s1 = Service(
                tenant_id=tenant.id,
                name="Consultoria / Atendimento Geral",
                description="Sessão de atendimento individual presencial ou remoto",
                duration_minutes=45,
                price=Decimal("150.00"),
                is_active=True
            )
            s2 = Service(
                tenant_id=tenant.id,
                name="Procedimento Especializado",
                description="Execução de serviço avançado",
                duration_minutes=60,
                price=Decimal("250.00"),
                is_active=True
            )
            db.add_all([s1, s2])
            db.flush()
            services_data = [s1, s2]
            print(f"[+] Serviços cadastrados: {len(services_data)}")
        else:
            services_data = db.query(Service).filter(Service.tenant_id == tenant.id).all()

        # 4. Customers
        existing_customers = db.query(Customer).filter(Customer.tenant_id == tenant.id).count()
        customers_data = []
        if existing_customers == 0:
            c1 = Customer(
                tenant_id=tenant.id,
                name="Carlos Eduardo Silva",
                phone="(11) 98765-4321",
                email="carlos.silva@email.com",
                document="123.456.789-00",
                notes="Cliente assíduo"
            )
            c2 = Customer(
                tenant_id=tenant.id,
                name="Mariana Souza Lima",
                phone="(11) 91234-5678",
                email="mariana.lima@email.com",
                document="987.654.321-11",
                notes="Prefere atendimento no período da tarde"
            )
            db.add_all([c1, c2])
            db.flush()
            customers_data = [c1, c2]
            print(f"[+] Clientes cadastrados: {len(customers_data)}")
        else:
            customers_data = db.query(Customer).filter(Customer.tenant_id == tenant.id).all()

        # 5. Appointments & Transactions
        existing_appts = db.query(Appointment).filter(Appointment.tenant_id == tenant.id).count()
        if existing_appts == 0 and services_data and customers_data:
            today = date.today()
            # Appointment 1: Today at 14:00
            start1 = datetime.combine(today, time(14, 0))
            end1 = start1 + timedelta(minutes=services_data[0].duration_minutes)
            appt1 = Appointment(
                tenant_id=tenant.id,
                customer_id=customers_data[0].id,
                service_id=services_data[0].id,
                professional_id=admin_user.id,
                start_time=start1,
                end_time=end1,
                status="CONFIRMED",
                notes="Primeira sessão"
            )

            # Appointment 2: Today at 16:00
            start2 = datetime.combine(today, time(16, 0))
            end2 = start2 + timedelta(minutes=services_data[1].duration_minutes)
            appt2 = Appointment(
                tenant_id=tenant.id,
                customer_id=customers_data[1].id,
                service_id=services_data[1].id,
                professional_id=admin_user.id,
                start_time=start2,
                end_time=end2,
                status="PENDING",
                notes="Aguardando confirmação do cliente"
            )
            db.add_all([appt1, appt2])
            db.flush()
            print("[+] Agendamentos de exemplo criados")

        # 6. Sample Transactions (Financial)
        existing_trx = db.query(Transaction).filter(Transaction.tenant_id == tenant.id).count()
        if existing_trx == 0:
            today = date.today()
            t1 = Transaction(
                tenant_id=tenant.id,
                customer_id=customers_data[0].id if customers_data else None,
                type="INCOME",
                category="Serviços",
                amount=Decimal("150.00"),
                due_date=today,
                payment_date=today,
                status="PAID",
                payment_method="PIX",
                notes="Entrada referente a atendimento"
            )
            t2 = Transaction(
                tenant_id=tenant.id,
                type="EXPENSE",
                category="Infraestrutura",
                amount=Decimal("89.90"),
                due_date=today,
                payment_date=today,
                status="PAID",
                payment_method="DEBIT_CARD",
                notes="Hospedagem / Software"
            )
            t3 = Transaction(
                tenant_id=tenant.id,
                type="EXPENSE",
                category="Insumos",
                amount=Decimal("120.00"),
                due_date=today + timedelta(days=5),
                payment_date=None,
                status="PENDING",
                payment_method="BOLETO",
                notes="Material de expediente a pagar"
            )
            db.add_all([t1, t2, t3])
            db.flush()
            print("[+] Lançamentos financeiros de exemplo criados")

        db.commit()
        print("\n===> Seed concluído com sucesso!")
        print("Login Demo: admin@demo.com / Senha: admin123")

    except Exception as e:
        db.rollback()
        print(f"Erro no seed: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

