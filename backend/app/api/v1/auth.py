import re
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.core.security import verify_password, get_password_hash, create_access_token
from app.models.tenant import Tenant
from app.models.user import User
from app.schemas.auth import Token, LoginRequest, RegisterRequest

router = APIRouter(prefix="/auth", tags=["Autenticação"])

def slugify(text: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    slug = re.sub(r"[\s_-]+", "-", slug)
    return slug

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    base_slug = slugify(request.company_name) or "empresa"
    slug = base_slug
    counter = 1
    while db.query(Tenant).filter(Tenant.slug == slug).first():
        slug = f"{base_slug}-{counter}"
        counter += 1

    tenant = Tenant(name=request.company_name, slug=slug)
    db.add(tenant)
    db.flush()

    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        db.rollback()
        raise HTTPException(status_code=400, detail="Este e-mail já está em uso")

    user = User(
        tenant_id=tenant.id,
        name=request.admin_name,
        email=request.email,
        password_hash=get_password_hash(request.password),
        role="ADMIN",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(subject=user.id, tenant_id=tenant.id, role=user.role)
    return Token(
        access_token=token,
        tenant_id=tenant.id,
        user_id=user.id,
        role=user.role,
        user_name=user.name
    )

@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    clean_email = request.email.strip().lower()
    user = db.query(User).filter(User.email == clean_email).first()

    # Fallback auto-seed se o banco estiver vazio ou usuário demo estiver faltando
    if not user and (clean_email in ["admin@demo.com", "teste@demo.com", "teste@teste.com"] or db.query(User).count() == 0):
        try:
            from app.seed import seed_database
            seed_database()
            user = db.query(User).filter(User.email == clean_email).first()
        except Exception:
            pass

    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos"
        )
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuário inativo")

    token = create_access_token(subject=user.id, tenant_id=user.tenant_id, role=user.role)
    return Token(
        access_token=token,
        tenant_id=user.tenant_id,
        user_id=user.id,
        role=user.role,
        user_name=user.name
    )

@router.post("/token", response_model=Token)
def login_for_swagger(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )
    token = create_access_token(subject=user.id, tenant_id=user.tenant_id, role=user.role)
    return Token(
        access_token=token,
        tenant_id=user.tenant_id,
        user_id=user.id,
        role=user.role,
        user_name=user.name
    )

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == current_user.tenant_id).first()
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
        "tenant": {
            "id": tenant.id if tenant else None,
            "name": tenant.name if tenant else None,
            "slug": tenant.slug if tenant else None
        }
    }

