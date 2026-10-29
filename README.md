# Sistema 0 — Boilerplate Base (Agendamento & Financeiro Multi-tenant)

O **Sistema 0** é uma fundação desacoplada, moderna e pronta para produção concebida para servir como ponto de partida (*starter base*) para novos softwares e SaaS que necessitam de:
- **Gestão de Agendamentos** (com bloqueio automático de conflitos de horário).
- **Controle Financeiro Integrado** (contas a pagar, receber, fluxo de caixa e geração automática de receita na conclusão do atendimento).
- **Base Cadastral Integrada** (Clientes/CRM e Catálogo de Serviços com tempo e preço).
- **Arquitetura Multi-Tenant Nativa** (`tenant_id` em todas as tabelas e isolamento por token JWT).
- **Dashboard Operacional e Financeiro** consolidado.

---

## 🛠️ Stack Tecnológica

- **Backend:** Python 3.12+ / FastAPI / SQLAlchemy 2.0 / Pydantic v2 / Uvicorn
- **Banco de Dados:** SQLite (padrão local plug-and-play) ou PostgreSQL (basta alterar a variável `DATABASE_URL` no `.env`)
- **Frontend SPA / Dashboard:** HTML5 + Tailwind CSS + Vanilla JS integrado (e 100% pronto para conectar via API com Next.js / Flutter)
- **Autenticação:** JWT Stateless com suporte a RBAC (`ADMIN`, `OPERATOR`)

---

## 🚀 Como Executar em 3 Passos

### 1. Criar ambiente virtual e instalar dependências
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate   # No Windows (ou source .venv/bin/activate no Linux/Mac)
pip install -r requirements.txt
```

### 2. Popular o banco com dados de teste (Seed)
```bash
python app/seed.py
```
Isso criará uma empresa de teste (*Empresa Modelo Demo*), um usuário administrador, serviços, clientes, agendamentos e transações financeiras.
- **Login Demo:** `admin@demo.com`
- **Senha Demo:** `admin123`

### 3. Iniciar o Servidor
```bash
uvicorn app.main:app --reload --port 8000
```
- Acesse o **Dashboard Web:** [http://localhost:8000/](http://localhost:8000/)
- Acesse a **Documentação Interativa (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- Acesse o **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Executar Testes Automatizados

Para rodar a suíte completa de testes (cobre registro multi-tenant, bloqueio de conflitos, geração financeira automática e dashboards):
```bash
cd backend
.\.venv\Scripts\pytest -v
```

---

## 📂 Estrutura do Projeto

```text
sistema-zero/
├── backend/
│   ├── app/
│   │   ├── core/           # Configurações globais, banco e segurança JWT
│   │   ├── models/         # Modelos SQLAlchemy (Tenant, User, Customer, Service, Appointment, Transaction)
│   │   ├── schemas/        # Schemas Pydantic v2 para validação e serialização
│   │   ├── api/
│   │   │   ├── deps.py     # Dependências (sessão do banco, auth, multi-tenant extractor)
│   │   │   └── v1/         # Endpoints REST (auth, customers, services, appointments, financial, dashboard)
│   │   ├── main.py         # Entrypoint da aplicação FastAPI
│   │   └── seed.py         # Script para população inicial
│   ├── tests/              # Testes automatizados (pytest)
│   └── requirements.txt
├── frontend/
│   └── index.html          # Dashboard moderno, responsivo e integrado à API
└── README.md
```

---

## 💡 Como Usar como Base para Novos Sistemas

1. **Clonar a pasta:** Duplique a pasta `sistema-zero` para o nome do seu novo projeto (ex: `clinica-app`, `barber-pro`, `consultoria-flow`).
2. **Adicionar campos específicos:** Acrescente novas colunas nos modelos existentes em `backend/app/models/` conforme o nicho (ex: prontuário para clínicas, modelo de veículo para oficinas).
3. **Plugar frontend dedicado (Opcional):** Se optar por construir um app mobile (Flutter/React Native) ou um portal avançado (Next.js), basta consumir os endpoints documentados em `/docs`.

