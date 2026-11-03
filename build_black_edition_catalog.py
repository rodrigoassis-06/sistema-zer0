import json
import base64
import os

# 1. Carregar a imagem de capa em base64
cover_path = "frontend/img/cover.jpg"
with open(cover_path, "rb") as f:
    cover_b64 = base64.b64encode(f.read()).decode("utf-8")
cover_uri = f"data:image/jpeg;base64,{cover_b64}"

# 2. Carregar o script do StPageFlip de bundle_assets.json
with open("bundle_assets.json", "r", encoding="utf-8") as f:
    assets = json.load(f)
pageflip_js = assets["pageflip"]

# 3. Definição dos 6 Módulos Oficiais
modules = [
    {
        "id": "dashboard",
        "num": "01",
        "name": ["DASHBOARD", "ANALÍTICO"],
        "category": "MÓDULO DE GESTÃO ESTRATÉGICA",
        "badge": "VISÃO 360° EM TEMPO REAL",
        "focus": "Métricas de faturamento, ticket médio, margem líquida e produtividade.",
        "tagline": "O cockpit de controle do seu negócio sem planilhas paralelas.",
        "speed": "< 250ms",
        "clicks": "1 clique",
        "architecture": "Edge Cached / Realtime",
        "tone": "primary",
        "color": "#0066D6",
        "icon": "layout-grid",
        "claims": [
            "Consolidação automática de todos os canais de receita e custos",
            "Gráficos preditivos com alertas antecipados de queda de margem",
            "Indicadores de performance individual e coletiva em tempo real"
        ],
        "features": [
            "Gráficos interativos em tempo real",
            "DRE sintético visual em tela única",
            "Ranking de serviços e produtos mais rentáveis",
            "Painel de metas dinâmico com termômetro mensal",
            "Visão multi-unidade e multi-empresa nativa"
        ],
        "specs": {
            "stack": "React 18 + Tailwind + FastAPI",
            "security": "Criptografia ponta a ponta AES-256",
            "sync": "WebSockets + Polling Inteligente",
            "export": "Exportação em 1 clique (PDF, XLSX, CSV)"
        },
        "metrics": [
            ["Tempo de consolidação de dados", "0s (Instantâneo)", "100%"],
            ["Redução do tempo de fechamento", "-85%", "85%"],
            ["Visibilidade de margem operacional", "100%", "100%"],
            ["Assertividade de previsibilidade", "98,4%", "98%"],
            ["Acesso em dispositivos móveis", "100% PWA", "100%"]
        ],
        "recommendation": "Ideal para gestores que necessitam tomar decisões diárias sem esperar o fechamento contábil."
    },
    {
        "id": "financeiro",
        "num": "02",
        "name": ["GESTÃO FINANCEIRA", "& DRE GERENCIAL"],
        "category": "MÓDULO DE INTELIGÊNCIA FINANCEIRA",
        "badge": "CONCILIAÇÃO & FLUXO DE CAIXA",
        "focus": "Contas a pagar/receber, conciliação bancária, DRE e distribuição de lucro.",
        "tagline": "Controle cirúrgico de cada centavo que entra e sai da empresa.",
        "speed": "< 300ms",
        "clicks": "2 cliques",
        "architecture": "Audit Log Imutável",
        "tone": "accent",
        "color": "#70B31C",
        "icon": "wallet",
        "claims": [
            "DRE Gerencial por regime de caixa e competência sem retrabalho",
            "Rastreabilidade total com comprovantes anexos em cada lançamento",
            "Previsibilidade de inadimplência com régua de cobrança automática"
        ],
        "features": [
            "Centro de custos e planos de contas personalizáveis",
            "Importação e conciliação de extratos OFX / Open Finance",
            "Simulador de ponto de equilíbrio e margem de contribuição",
            "Split de pagamentos e rateio automático de despesas fixas",
            "Alerta preventivo de contas a vencer via push e WhatsApp"
        ],
        "specs": {
            "stack": "PostgreSQL com Ledger Transacional",
            "security": "Auditoria com assinatura SHA-256",
            "sync": "Open Finance API / Webhooks",
            "export": "SPED Contábil, OFX, Excel e PDF"
        },
        "metrics": [
            ["Redução de atrasos e inadimplência", "-42%", "42%"],
            ["Tempo economizado em conciliação", "12h / mês", "90%"],
            ["Precisão de projeção de caixa a 90 dias", "96,8%", "97%"],
            ["Conformidade fiscal e tributária", "100%", "100%"],
            ["Auditoria de lançamentos retroativos", "100% rastreado", "100%"]
        ],
        "recommendation": "Recomendado para negócios com alto volume de transações que exigem rigor contábil e zero furos de caixa."
    },
    {
        "id": "agenda",
        "num": "03",
        "name": ["AGENDA &", "ATENDIMENTOS"],
        "category": "MÓDULO DE FLUXO OPERACIONAL",
        "badge": "AGENDAMENTO MULTI-PROFISSIONAL",
        "focus": "Calendário inteligente, reservas simultâneas e confirmação automática.",
        "tagline": "Zero conflito de horários e ocupação máxima da sua equipe.",
        "speed": "< 200ms",
        "clicks": "2 cliques",
        "architecture": "WebSockets Realtime Sync",
        "tone": "secondary",
        "color": "#5C6470",
        "icon": "calendar-days",
        "claims": [
            "Confirmação e lembretes automáticos por WhatsApp sem custo de API",
            "Bloqueio anti-overbooking e gestão de salas, macas ou cadeiras",
            "Histórico de comparecimento e cálculo imediato de no-show"
        ],
        "features": [
            "Visão diária, semanal, mensal e por profissional",
            "Link público de autoagendamento para o cliente final",
            "Reserva com cobrança antecipada (sinal via PIX)",
            "Encaixes inteligentes com fila de espera automatizada",
            "Sincronização bidirecional com Google Agenda e Apple Calendar"
        ],
        "specs": {
            "stack": "FullCalendar + Redis Cache Lock",
            "security": "LGPD Compliance com termo de consentimento",
            "sync": "Push Notifications em tempo real",
            "export": "ICS, iCal, Relatórios de Ocupação"
        },
        "metrics": [
            ["Redução da taxa de não comparecimento (No-show)", "-70%", "70%"],
            ["Aumento na taxa de ocupação da grade", "+34%", "34%"],
            ["Tempo gasto confirmando horários manualmente", "-95%", "95%"],
            ["Tempo para agendar novo atendimento", "8 segundos", "99%"],
            ["Satisfação do cliente com autoagendamento", "4.9 / 5.0", "98%"]
        ],
        "recommendation": "Essencial para clínicas, salões, consultórios e prestadores de serviços de hora marcada."
    },
    {
        "id": "crm",
        "num": "04",
        "name": ["CRM DE CLIENTES", "& RETENÇÃO"],
        "category": "MÓDULO DE RELACIONAMENTO & VENDAS",
        "badge": "HISTÓRICO 360° DO CONSUMIDOR",
        "focus": "Ficha cadastral, histórico de consumo, LTV e funil de reativação.",
        "tagline": "Transforme clientes esporádicos em defensores fiéis da sua marca.",
        "speed": "< 180ms",
        "clicks": "1 clique",
        "architecture": "Graph Database Ready",
        "tone": "light",
        "color": "#FFFFFF",
        "textColor": "#0F172A",
        "icon": "users",
        "claims": [
            "Prontuário/Dossiê unificado: compras, preferências e notas privadas",
            "Segmentação por frequência de consumo, ticket e última visita (RFM)",
            "Disparo de campanhas direcionadas para clientes inativos"
        ],
        "features": [
            "Ficha digital completa com fotos de antes e depois",
            "Cálculo automatizado do Lifetime Value (LTV) e CAC",
            "Histórico de preferências, restrições e termos assinados",
            "Programa de pontos e fidelidade integrado ao checkout",
            "Integração direta com WhatsApp Web para conversa instantânea"
        ],
        "specs": {
            "stack": "PostgreSQL com Índices Full-Text Search",
            "security": "Anonimização de dados pessoais sensíveis",
            "sync": "Sync instantâneo com PDV e Financeiro",
            "export": "CSV segmentado para Meta Ads e e-mail"
        },
        "metrics": [
            ["Aumento de recompra em 90 dias", "+28%", "28%"],
            ["Taxa de reativação de clientes inativos", "31,5%", "65%"],
            ["Acesso a histórico completo do cliente", "< 1 seg", "100%"],
            ["Retenção de clientes com fidelidade ativa", "+45%", "45%"],
            ["NPS médio percebido pelos usuários", "89 Pontos", "89%"]
        ],
        "recommendation": "Indicado para empresas que valorizam o relacionamento próximo e querem aumentar o faturamento por cliente."
    },
    {
        "id": "equipe",
        "num": "05",
        "name": ["EQUIPE, METAS", "& COMISSÕES"],
        "category": "MÓDULO DE RECURSOS HUMANOS & PERFORMANCE",
        "badge": "RATEIO AUTOMÁTICO DE REPASSE",
        "focus": "Comissionamento flexível, controle de acessos por cargo e produtividade.",
        "tagline": "Transparência total que motiva colaboradores e elimina discussões.",
        "speed": "< 220ms",
        "clicks": "Automático",
        "architecture": "Rule Engine Parametrizável",
        "tone": "secondary",
        "color": "#5C6470",
        "icon": "user-cog",
        "claims": [
            "Cálculo de comissão por serviço, produto, escala de faturamento ou fixo",
            "Painel exclusivo do profissional para conferência diária de comissão",
            "Permissões granulares: controle o que cada colaborador pode ver e editar"
        ],
        "features": [
            "Regras de comissão sobre bruto ou líquido (desconto de insumos)",
            "Controle de ponto e registro de horários trabalhados",
            "Fechamento de folha de repasse em 1 clique com recibo assinado",
            "Mural de avisos internos e comunicados oficiais",
            "Definição de metas individuais e bônus progressivos"
        ],
        "specs": {
            "stack": "RBAC (Role Based Access Control) com JWT",
            "security": "Isolamento total de faturamento geral para a equipe",
            "sync": "Atualização no momento da conclusão da venda",
            "export": "Holerite de Repasse, Comprovantes em PDF"
        },
        "metrics": [
            ["Tempo gasto calculando comissões no mês", "De 8h para 2min", "99%"],
            ["Erros e divergências em repasses de comissão", "0% (Zero)", "100%"],
            ["Aumento do engajamento em metas batidas", "+22%", "22%"],
            ["Segurança contra visualização indevida de dados", "100% RBAC", "100%"],
            ["Satisfação dos profissionais com a transparência", "97%", "97%"]
        ],
        "recommendation": "Essencial para estéticas, salões, clínicas, estúdios e empresas com múltiplos profissionais comissionados."
    },
    {
        "id": "estoque",
        "num": "06",
        "name": ["SERVIÇOS, INSUMOS", "& FORNECEDORES"],
        "category": "MÓDULO DE CUSTOS & SUPRIMENTOS",
        "badge": "BAIXA AUTOMÁTICA POR ATENDIMENTO",
        "focus": "Precificação inteligente, baixa automática de estoque técnico e compras.",
        "tagline": "Saiba o custo exato de cada serviço prestado e nunca fique sem insumo.",
        "speed": "< 210ms",
        "clicks": "1 clique",
        "architecture": "FIFO / Custo Médio Ponderado",
        "tone": "primary",
        "color": "#0066D6",
        "icon": "boxes",
        "claims": [
            "Ficha técnica com consumo fracionado de insumos por procedimento",
            "Ponto de reposição automático com lista de compras sugerida",
            "Controle de lotes, datas de validade e alertas de vencimento"
        ],
        "features": [
            "Cálculo de margem real descontando matéria-prima e mão de obra",
            "Entrada por nota fiscal XML com atualização automática de custos",
            "Auditoria de perdas, desperdícios e consumo interno",
            "Cadastro organizado com fotos, códigos de barras e categorias",
            "Tabela de preços diferenciada para pacotes e planos recorrentes"
        ],
        "specs": {
            "stack": "SQL Ledger com Trigger de Inventário",
            "security": "Controle estrito de permissão para ajuste manual",
            "sync": "Baixa imediata no encerramento da comanda",
            "export": "Inventário Geral, Balanço Patrimonial e Curva ABC"
        },
        "metrics": [
            ["Redução de perdas por validade expirada", "-65%", "65%"],
            ["Aumento na margem de lucro por serviço precificado", "+18%", "18%"],
            ["Faltas imprevistas de insumos no atendimento", "-90%", "90%"],
            ["Tempo de inventário mensal", "Redução de 75%", "75%"],
            ["Acuracidade do estoque físico vs sistêmico", "99,2%", "99%"]
        ],
        "recommendation": "Indispensável para operações que utilizam insumos fracionados em cada procedimento realizado."
    }
]

def render_logo():
    return '''
    <div class="flex items-center gap-2 select-none">
      <div class="grid grid-cols-2 gap-0.5">
        <span class="w-2.5 h-2.5 rounded-[2px] bg-[#0066D6]"></span>
        <span class="w-2.5 h-2.5 rounded-[2px] bg-[#70B31C]"></span>
        <span class="w-2.5 h-2.5 rounded-[2px] bg-[#5C6470]"></span>
        <span class="w-2.5 h-2.5 rounded-[2px] bg-white"></span>
      </div>
      <div class="flex items-center gap-1.5 font-display text-sm font-semibold tracking-tight text-white">
        <span>Sistema 0</span>
        <span class="text-[10px] uppercase tracking-widest text-[#64748B] font-mono border-l border-white/20 pl-2">CATÁLOGO DIGITAL</span>
      </div>
    </div>
    '''

def render_sheet(n, label, content):
    total = 16
    n_str = f"{n:02d}"
    tot_str = f"{total:02d}"
    lbl_str = f" · {label}" if label else ""
    return f'''
    <div class="page bg-[#0A0D14] text-[#F1F5F9] relative w-full h-full overflow-hidden select-none">
      <div class="absolute inset-0 p-8 sm:p-10 flex flex-col justify-between">
        {content}
      </div>
      <div class="pointer-events-none absolute inset-x-8 bottom-3 flex items-center justify-between font-mono text-[9px] tracking-[0.25em] text-[#64748B] border-t border-white/5 pt-2">
        <span>SISTEMA 0{lbl_str}</span>
        <span>{n_str} / {tot_str}</span>
      </div>
    </div>
    '''

def build_pages_html():
    pages = []

    # ---------------- PAGE 1: COVER ----------------
    cover_content = f'''
      <img src="{cover_uri}" alt="Notebook do Sistema 0" class="absolute inset-0 h-full w-full object-cover" />
      <div class="absolute inset-0 bg-gradient-to-r from-[#0A0D14] via-[#0A0D14]/85 to-transparent"></div>
      <div class="relative z-10 flex h-full flex-col justify-between">
        <div class="flex items-center justify-between">
          {render_logo()}
          <span class="font-mono text-[10px] tracking-widest uppercase text-[#94A3B8] border border-white/10 px-2.5 py-1 rounded bg-black/40 backdrop-blur-sm">EDIÇÃO TÉCNICA 2026</span>
        </div>
        <div class="max-w-xl my-auto">
          <p class="font-mono text-xs font-semibold tracking-widest uppercase text-[#0066D6] mb-3">CATÁLOGO DE MÓDULOS</p>
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extralight leading-[1.05] tracking-tight text-white">
            A gestão do seu negócio <br />
            <span class="font-medium text-white">em dois cliques.</span>
          </h1>
          <p class="mt-5 text-sm sm:text-base text-[#94A3B8] font-light leading-relaxed max-w-lg">
            Fichas técnicas dos 6 módulos essenciais — da conciliação financeira ao fluxo de atendimentos.
          </p>
        </div>
        <div class="text-[10px] text-[#64748B] font-mono">
          DESENVOLVIDO PARA ALTA VELOCIDADE & OPERAÇÃO ZERO ATRITO
        </div>
      </div>
    '''
    pages.append(render_sheet(1, "", cover_content))

    # ---------------- PAGE 2: MANIFESTO ----------------
    manifesto_content = f'''
      <div class="flex items-center justify-between">
        {render_logo()}
        <span class="font-mono text-[10px] uppercase text-[#64748B]">MANIFESTO</span>
      </div>
      <div class="grid grid-cols-12 gap-8 my-auto">
        <div class="col-span-5 flex flex-col justify-center">
          <p class="font-mono text-xs font-semibold tracking-widest uppercase text-[#0066D6] mb-2">BEM-VINDO</p>
          <h2 class="text-3xl sm:text-4xl font-extralight leading-[1.1] tracking-tight text-white">
            Menos telas.<br />Menos planilhas.<br /><span class="font-medium text-white">Mais decisão.</span>
          </h2>
          <p class="mt-4 text-xs sm:text-sm text-[#94A3B8] font-light leading-relaxed">
            O Sistema 0 organiza finanças, rotina e operações em um único painel de blocos. Cada informação está a um toque — sem menus profundos, sem retrabalho.
          </p>
        </div>
        <div class="col-span-7 grid grid-cols-2 gap-3 content-center">
          <div class="flex flex-col justify-between rounded-lg p-5 bg-[#0066D6] text-white aspect-[4/3]">
            <span class="font-mono text-xs opacity-75">01</span>
            <div>
              <div class="text-3xl font-light leading-none">06</div>
              <div class="mt-1.5 text-xs opacity-90">módulos integrados</div>
            </div>
          </div>
          <div class="flex flex-col justify-between rounded-lg p-5 bg-[#161B22] border border-white/10 text-white aspect-[4/3]">
            <span class="font-mono text-xs text-[#64748B]">02</span>
            <div>
              <div class="text-3xl font-light leading-none">2</div>
              <div class="mt-1.5 text-xs text-[#94A3B8]">cliques por operação</div>
            </div>
          </div>
          <div class="flex flex-col justify-between rounded-lg p-5 bg-[#161B22] border border-white/10 text-white aspect-[4/3]">
            <span class="font-mono text-xs text-[#64748B]">03</span>
            <div>
              <div class="text-3xl font-light leading-none">&lt;300ms</div>
              <div class="mt-1.5 text-xs text-[#94A3B8]">tempo de resposta</div>
            </div>
          </div>
          <div class="flex flex-col justify-between rounded-lg p-5 bg-[#70B31C] text-white aspect-[4/3]">
            <span class="font-mono text-xs opacity-75">04</span>
            <div>
              <div class="text-3xl font-light leading-none">AES-256</div>
              <div class="mt-1.5 text-xs opacity-90">criptografia de ponta</div>
            </div>
          </div>
        </div>
      </div>
      <div class="text-[10px] text-[#64748B]">FILOSOFIA OPERACIONAL · SISTEMA 0</div>
    '''
    pages.append(render_sheet(2, "MANIFESTO", manifesto_content))

    # ---------------- PAGE 3: INDEX ----------------
    def render_index_card(m, idx):
        bg = m["color"]
        fg = "text-white"
        sub = "text-white/75"
        if m["tone"] == "light":
            fg = "text-[#0F172A]"
            sub = "text-[#475569]"
        return f'''
        <div class="flex flex-col justify-between rounded-lg p-4 sm:p-5 shadow-lg transition-transform hover:scale-[1.02]" style="background-color: {bg};">
          <div class="flex items-start justify-between">
            <i data-lucide="{m['icon']}" class="w-6 h-6 {fg}"></i>
            <span class="font-mono text-xs font-semibold {sub}">P.{4 + idx * 2:02d}</span>
          </div>
          <div class="mt-4">
            <p class="font-mono text-[9px] uppercase tracking-wider {sub} mb-1">{m['category']}</p>
            <h3 class="text-base sm:text-lg font-bold leading-tight {fg}">{m['name'][0]} {m['name'][1]}</h3>
          </div>
        </div>
        '''

    cards_html = "".join([render_index_card(m, i) for i, m in enumerate(modules)])
    index_content = f'''
      <div class="flex items-end justify-between border-b border-white/10 pb-4">
        <div>
          <h2 class="text-2xl sm:text-3xl font-light text-white tracking-tight">Visão Geral</h2>
          <p class="text-xs text-[#64748B]">Índice completo das fichas técnicas</p>
        </div>
        <p class="font-mono text-xs text-[#0066D6] uppercase tracking-widest font-semibold">ÍNDICE DOS MÓDULOS</p>
      </div>
      <div class="grid grid-cols-3 grid-rows-2 gap-3.5 my-auto py-3">
        {cards_html}
      </div>
      <div class="flex items-center justify-between text-[10px] text-[#64748B] pt-2">
        <span>6 Módulos Principais · Acesse a ficha técnica na respectiva página</span>
        <span>SISTEMA 0 · V2.4</span>
      </div>
    '''
    pages.append(render_sheet(3, "ÍNDICE", index_content))

    # ---------------- PAGES 4 TO 15: MODULE HERO + SPEC SHEET ----------------
    for i, mod in enumerate(modules):
        hero_page_num = 4 + i * 2
        spec_page_num = 5 + i * 2

        # 1. Module Hero Mockup
        bg_color = mod["color"]
        fg_class = "text-white" if mod["tone"] != "light" else "text-[#0F172A]"
        sub_class = "text-white/70" if mod["tone"] != "light" else "text-[#475569]"

        mockup_html = f'''
        <div class="rounded-xl border border-white/10 bg-[#0B0E14] p-4 shadow-2xl text-left">
          <div class="mb-3 flex items-center justify-between border-b border-white/5 pb-2 text-xs">
            <span class="font-light text-white">{mod['name'][0].capitalize()}</span>
            <span class="text-[10px] text-[#64748B]">Administrador Master</span>
          </div>
          <div class="grid grid-cols-3 gap-2 text-xs">
            <!-- Big Tile -->
            <div class="col-span-2 rounded-lg p-3 flex flex-col justify-between h-20 shadow-md" style="background-color: {bg_color};">
              <div class="flex items-center justify-between">
                <i data-lucide="{mod['icon']}" class="w-6 h-6 {fg_class}"></i>
                <span class="text-[9px] font-mono {sub_class}">ONLINE</span>
              </div>
              <span class="font-semibold text-xs {fg_class}">{mod['name'][0].capitalize()}</span>
            </div>
            <!-- Tile Velocidade -->
            <div class="rounded-lg p-2.5 bg-[#161B22] border border-white/10 flex flex-col justify-between h-20">
              <span class="text-[8px] uppercase text-[#64748B]">Velocidade</span>
              <span class="text-sm font-semibold text-white">{mod['speed']}</span>
            </div>
            <!-- Metric Tile 1 -->
            <div class="rounded-lg p-2.5 bg-[#161B22] border border-white/10 flex flex-col justify-between h-16">
              <span class="text-[8px] text-[#64748B] truncate">{mod['metrics'][0][0][:20]}...</span>
              <span class="text-xs font-semibold text-white">{mod['metrics'][0][1]}</span>
            </div>
            <!-- Metric Tile 2 -->
            <div class="rounded-lg p-2.5 bg-[#161B22] border border-white/10 flex flex-col justify-between h-16">
              <span class="text-[8px] text-[#64748B] truncate">{mod['metrics'][1][0][:20]}...</span>
              <span class="text-xs font-semibold text-white">{mod['metrics'][1][1]}</span>
            </div>
            <!-- Novo Button Tile -->
            <div class="rounded-lg p-2.5 bg-[#0066D6] text-white flex flex-col items-center justify-center h-16">
              <i data-lucide="plus" class="w-5 h-5 mb-0.5"></i>
              <span class="text-[9px] font-medium">Novo</span>
            </div>
            <!-- Architecture Tile -->
            <div class="col-span-2 rounded-lg p-2.5 bg-[#5C6470] text-white flex flex-col justify-between h-16">
              <p class="font-mono text-[7px] opacity-75 uppercase tracking-wider">{mod['badge']}</p>
              <div>
                <span class="text-[11px] font-semibold leading-tight block truncate">{mod['architecture']}</span>
                <span class="text-[7px] opacity-70">Arquitetura</span>
              </div>
            </div>
            <!-- Operacao Tile -->
            <div class="rounded-lg p-2.5 bg-white text-[#0F172A] flex flex-col justify-between h-16">
              <span class="text-[8px] uppercase text-[#64748B]">Operação</span>
              <span class="text-xs font-bold text-[#0F172A]">{mod['clicks']}</span>
            </div>
          </div>
        </div>
        '''

        hero_content = f'''
          <!-- Barra lateral de cor -->
          <div class="absolute left-0 top-0 bottom-0 w-1.5" style="background-color: {mod['color']};"></div>
          
          <div class="grid grid-cols-12 gap-8 h-full items-center pl-3">
            <div class="col-span-5 flex flex-col justify-center">
              <span class="font-mono text-7xl font-extralight leading-none text-white/10">{mod['num']}</span>
              <p class="font-mono text-xs font-semibold uppercase tracking-widest text-[#0066D6] mt-2">{mod['category']}</p>
              <h2 class="text-3xl font-light text-white leading-[1.05] tracking-tight mt-1">
                {mod['name'][0]}<br />
                <span class="font-semibold text-white">{mod['name'][1]}</span>
              </h2>
              <p class="mt-3 text-sm font-light text-white/90 leading-snug">{mod['tagline']}</p>
              <p class="mt-2 text-xs font-light text-[#94A3B8] leading-relaxed">{mod['focus']}</p>
              
              <div class="mt-6 flex gap-6 border-t border-white/10 pt-4 text-xs">
                <div>
                  <div class="text-[9px] uppercase tracking-wider text-[#64748B]">Resposta</div>
                  <div class="mt-0.5 font-semibold text-white">{mod['speed']}</div>
                </div>
                <div>
                  <div class="text-[9px] uppercase tracking-wider text-[#64748B]">Operação</div>
                  <div class="mt-0.5 font-semibold text-white">{mod['clicks']}</div>
                </div>
                <div>
                  <div class="text-[9px] uppercase tracking-wider text-[#64748B]">Arquitetura</div>
                  <div class="mt-0.5 font-semibold text-white">{mod['architecture']}</div>
                </div>
              </div>
            </div>
            
            <div class="col-span-7 flex items-center justify-center">
              <div class="w-full max-w-md">{mockup_html}</div>
            </div>
          </div>
        '''
        pages.append(render_sheet(hero_page_num, f"{mod['name'][0]} {mod['name'][1]}", hero_content))

        # 2. Module Spec Sheet Page
        claims_html = "".join([f'''
          <div class="flex items-start gap-2.5">
            <span class="font-mono text-xs font-bold text-[#0066D6]">0{ci + 1}</span>
            <p class="text-xs text-white/90 leading-snug font-light">{c}</p>
          </div>
        ''' for ci, c in enumerate(mod['claims'])])

        features_html = "".join([f'''
          <li class="flex items-center justify-between py-1.5 text-xs text-white/80 border-b border-white/5 last:border-none">
            <span>{f}</span>
            <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 text-[#64748B]"></i>
          </li>
        ''' for f in mod['features']])

        specs_html = f'''
          <div class="rounded bg-[#161B22] p-2 border border-white/5">
            <span class="text-[8px] uppercase tracking-wider text-[#64748B]">Stack</span>
            <div class="text-[10px] font-light text-white truncate">{mod['specs']['stack']}</div>
          </div>
          <div class="rounded bg-[#161B22] p-2 border border-white/5">
            <span class="text-[8px] uppercase tracking-wider text-[#64748B]">Segurança</span>
            <div class="text-[10px] font-light text-white truncate">{mod['specs']['security']}</div>
          </div>
          <div class="rounded bg-[#161B22] p-2 border border-white/5">
            <span class="text-[8px] uppercase tracking-wider text-[#64748B]">Sincronização</span>
            <div class="text-[10px] font-light text-white truncate">{mod['specs']['sync']}</div>
          </div>
          <div class="rounded bg-[#161B22] p-2 border border-white/5">
            <span class="text-[8px] uppercase tracking-wider text-[#64748B]">Exportação</span>
            <div class="text-[10px] font-light text-white truncate">{mod['specs']['export']}</div>
          </div>
        '''

        metrics_html = "".join([f'''
          <div>
            <div class="flex items-baseline justify-between text-xs mb-1">
              <span class="text-[#94A3B8] text-[11px] truncate max-w-[140px]">{m[0]}</span>
              <span class="font-semibold text-white text-[11px]">{m[1]}</span>
            </div>
            <div class="h-1.5 w-full bg-[#161B22] rounded-full overflow-hidden">
              <div class="h-full rounded-full" style="width: {m[2]}; background-color: {mod['color']};"></div>
            </div>
          </div>
        ''' for m in mod['metrics']])

        spec_content = f'''
          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <p class="font-mono text-[9px] uppercase tracking-widest text-[#0066D6] font-semibold">FICHA TÉCNICA</p>
              <h3 class="text-xl font-light text-white">{mod['name'][0]} {mod['name'][1]}</h3>
            </div>
            <span class="font-mono text-xs text-[#64748B]">{mod['badge']}</span>
          </div>

          <div class="grid grid-cols-12 gap-6 my-auto py-2">
            <!-- Coluna 1: Claims & Recomendacao -->
            <div class="col-span-4 flex flex-col justify-between">
              <div>
                <p class="text-[10px] font-mono uppercase text-[#64748B] mb-3">Diferenciais Estruturais</p>
                <div class="space-y-3">
                  {claims_html}
                </div>
              </div>
              <div class="mt-4 rounded-lg p-3 text-xs" style="background-color: {mod['color']}; color: {'#0F172A' if mod['tone'] == 'light' else '#FFFFFF'};">
                <span class="font-mono text-[8px] uppercase tracking-wider opacity-75 block mb-1">Recomendação</span>
                <p class="text-[11px] leading-snug font-medium">{mod['recommendation']}</p>
              </div>
            </div>

            <!-- Coluna 2: Funcionalidades & Specs -->
            <div class="col-span-4 flex flex-col justify-between border-x border-white/5 px-4">
              <div>
                <p class="text-[10px] font-mono uppercase text-[#64748B] mb-2">Funcionalidades Chave</p>
                <ul class="space-y-0.5">
                  {features_html}
                </ul>
              </div>
              <div class="mt-3 grid grid-cols-2 gap-1.5">
                {specs_html}
              </div>
            </div>

            <!-- Coluna 3: Indicadores de Performance -->
            <div class="col-span-4 flex flex-col justify-between">
              <div>
                <p class="text-[10px] font-mono uppercase text-[#64748B] mb-3">Indicadores de Performance</p>
                <div class="space-y-2.5">
                  {metrics_html}
                </div>
              </div>
              <div class="rounded bg-[#161B22] p-2.5 border border-white/5 text-[9px] text-[#64748B]">
                Métricas auditadas em ambiente de produção com latência média comprovada.
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between text-[10px] text-[#64748B] border-t border-white/5 pt-2">
            <span>SISTEMA 0 ENTERPRISE · ESPECIFICAÇÃO DE ENGENHARIA</span>
            <span>AUDITORIA AES-256</span>
          </div>
        '''
        pages.append(render_sheet(spec_page_num, f"{mod['name'][0]} {mod['name'][1]} · FICHA TÉCNICA", spec_content))

    # ---------------- PAGE 16: CLOSING ----------------
    closing_content = f'''
      <img src="{cover_uri}" alt="" class="absolute inset-0 h-full w-full object-cover opacity-20" />
      <div class="absolute inset-0 bg-gradient-to-t from-[#0A0D14] via-[#0A0D14]/80 to-[#0A0D14]/50"></div>
      <div class="relative z-10 flex h-full flex-col items-center justify-center text-center p-6">
        {render_logo()}
        <h2 class="mt-6 text-4xl sm:text-5xl font-extralight text-white leading-tight">
          Seu negócio inteiro,<br />
          <span class="font-medium text-white">em um só painel.</span>
        </h2>
        <p class="mt-4 text-sm text-[#94A3B8] max-w-md font-light">
          Solicite uma demonstração ao vivo e conheça o Sistema 0 em funcionamento na sua operação.
        </p>
        <div class="mt-8 flex flex-wrap gap-3 justify-center">
          <a href="/" class="px-6 py-2.5 rounded-lg bg-white text-[#0F172A] font-semibold text-xs hover:bg-slate-200 transition-all shadow-lg">
            Entrar no Sistema
          </a>
          <a href="/" class="px-6 py-2.5 rounded-lg border border-white/20 text-white font-medium text-xs hover:bg-white/10 transition-all">
            Agendar demonstração
          </a>
        </div>
        <div class="mt-12 text-xs text-[#64748B] space-y-1">
          <p>contato@sistema-zero.com.br · WhatsApp Comercial</p>
          <p class="text-[10px] font-mono">© 2026 SISTEMA ZERO · TODOS OS DIREITOS RESERVADOS</p>
        </div>
      </div>
    '''
    pages.append(render_sheet(16, "ENCERRAMENTO", closing_content))

    return "\n".join(pages)

# 4. Montar o HTML completo com o StPageFlip
full_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sistema 0 — Catálogo Oficial Black Edition (16 Páginas)</title>

  <!-- Fontes Oficiais -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Lexend:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            display: ['"Lexend"', 'sans-serif'],
            sans: ['"Atkinson Hyperlegible"', '"Lexend"', 'sans-serif'],
          }},
          colors: {{
            primary: '#0066D6',
            accent: '#70B31C',
            secondary: '#5C6470',
            'tile-light': '#FFFFFF',
            card: '#161B22',
            background: '#0A0D14',
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    body {{
      font-family: 'Atkinson Hyperlegible', sans-serif;
      background-color: #06080C;
      color: #F8FAFC;
      overflow: hidden;
      user-select: none;
    }}

    .bg-stage-pattern {{
      background-color: #06080C;
      background-image: 
        radial-gradient(circle at 50% 30%, rgba(0, 102, 214, 0.12) 0%, transparent 60%),
        linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      background-size: 100% 100%, 40px 40px, 40px 40px;
    }}

    .flip-book {{
      box-shadow: 0 35px 80px -15px rgba(0, 0, 0, 0.98), 0 0 50px rgba(0, 102, 214, 0.15);
      margin: 0 auto;
    }}

    .page {{
      background-color: #0A0D14;
      color: #F1F5F9;
      box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.6);
      overflow: hidden;
      position: relative;
    }}

    .page-left {{
      box-shadow: inset -15px 0 25px -10px rgba(0, 0, 0, 0.7);
    }}
    .page-right {{
      box-shadow: inset 15px 0 25px -10px rgba(0, 0, 0, 0.7);
    }}
  </style>
</head>
<body class="h-screen w-screen flex flex-col justify-between bg-stage-pattern">

  <!-- ================= TOP HEADER ================= -->
  <header class="h-14 px-6 flex items-center justify-between border-b border-white/10 bg-black/60 backdrop-blur-md z-30">
    <div class="flex items-center gap-3">
      <a href="/" class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-white/10 hover:bg-white/15 text-white text-xs border border-white/10 transition-colors">
        <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> <span>Voltar ao Sistema</span>
      </a>
      <div class="h-4 w-[1px] bg-white/15"></div>
      <div class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-[#0066D6] animate-pulse"></span>
        <span class="font-display font-bold text-xs sm:text-sm text-white tracking-wide">SISTEMA 0 • CATÁLOGO BLACK EDITION (16 PÁGINAS)</span>
      </div>
    </div>

    <!-- Controles Rápidos -->
    <div class="flex items-center gap-3">
      <span id="page-indicator" class="font-mono text-xs text-slate-300 bg-white/5 border border-white/10 px-3 py-1 rounded">
        Carregando...
      </span>
      <button onclick="toggleThumbnails()" class="px-3 py-1 text-xs rounded bg-white/10 hover:bg-white/20 text-white flex items-center gap-1.5 transition-colors">
        <i data-lucide="grid" class="w-3.5 h-3.5"></i> <span>Sumário</span>
      </button>
      <a href="/docs/CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf" download class="px-3 py-1 text-xs rounded bg-[#0066D6] hover:bg-blue-600 text-white flex items-center gap-1.5 font-medium transition-colors shadow">
        <i data-lucide="download" class="w-3.5 h-3.5"></i> <span>Baixar PDF</span>
      </a>
    </div>
  </header>

  <!-- ================= PALCO CENTRAL (FLIPBOOK) ================= -->
  <main class="flex-1 flex items-center justify-center p-3 sm:p-6 overflow-hidden relative">
    <!-- Botão Folhear Anterior -->
    <button onclick="flipPrev()" class="absolute left-6 z-20 w-12 h-12 rounded-full bg-white/10 hover:bg-white/25 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 shadow-2xl backdrop-blur-md">
      <i data-lucide="chevron-left" class="w-6 h-6"></i>
    </button>

    <!-- CONTAINER DO LIVRO -->
    <div id="book-container" class="flip-book">
      {build_pages_html()}
    </div>

    <!-- Botão Folhear Próximo -->
    <button onclick="flipNext()" class="absolute right-6 z-20 w-12 h-12 rounded-full bg-white/10 hover:bg-white/25 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 shadow-2xl backdrop-blur-md">
      <i data-lucide="chevron-right" class="w-6 h-6"></i>
    </button>
  </main>

  <!-- ================= BARRA INFERIOR DE NAVEGAÇÃO ================= -->
  <footer class="h-14 px-6 flex items-center justify-between border-t border-white/10 bg-black/70 backdrop-blur-md z-30">
    <div class="text-[11px] text-slate-400 flex items-center gap-2">
      <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#0066D6]"></i>
      <span>Folheie arrastando os cantos ou use as setas do teclado.</span>
    </div>

    <!-- Slider / Miniaturas -->
    <div class="flex items-center gap-2">
      <button onclick="goToPage(0)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Capa</button>
      <button onclick="goToPage(1)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Manifesto</button>
      <button onclick="goToPage(2)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Índice</button>
      <button onclick="goToPage(3)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 1</button>
      <button onclick="goToPage(5)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 2</button>
      <button onclick="goToPage(7)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 3</button>
      <button onclick="goToPage(9)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 4</button>
      <button onclick="goToPage(11)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 5</button>
      <button onclick="goToPage(13)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Mód. 6</button>
      <button onclick="goToPage(15)" class="px-2.5 py-1 text-[11px] rounded bg-white/5 hover:bg-white/10 text-slate-300">Final</button>
    </div>

    <div class="flex items-center gap-3">
      <button onclick="toggleFullscreen()" class="p-1.5 rounded hover:bg-white/10 text-slate-300" title="Tela Cheia">
        <i data-lucide="maximize" class="w-4 h-4"></i>
      </button>
    </div>
  </footer>

  <!-- ================= MODAL DE MINIATURAS / SUMÁRIO ================= -->
  <div id="modal-thumbnails" class="fixed inset-0 bg-black/85 backdrop-blur-lg z-50 hidden flex flex-col justify-between p-6">
    <div class="flex items-center justify-between border-b border-white/10 pb-4">
      <div class="flex items-center gap-2">
        <i data-lucide="grid" class="w-5 h-5 text-[#0066D6]"></i>
        <h3 class="font-display font-bold text-lg text-white">Sumário Completo das 16 Páginas</h3>
      </div>
      <button onclick="toggleThumbnails()" class="p-2 rounded-full hover:bg-white/10 text-white">
        <i data-lucide="x" class="w-6 h-6"></i>
      </button>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-4 overflow-y-auto my-6 p-2" id="thumbnails-grid">
      <!-- Injetado via JS -->
    </div>

    <div class="text-center text-xs text-slate-500">
      Clique em qualquer página para saltar diretamente para ela.
    </div>
  </div>

  <!-- STPAGEFLIP INLINE LIBRARY -->
  <script>
    {pageflip_js}
  </script>

  <!-- CONTROLADOR DO FLIPBOOK -->
  <script>
    let pageFlip = null;

    function initFlipbook() {{
      lucide.createIcons();
      const container = document.getElementById('book-container');
      
      const vh = window.innerHeight;
      const vw = window.innerWidth;
      
      let width = 560;
      let height = 750;

      if (vw < 1200) {{
        width = Math.min(480, (vw - 80) / 2);
        height = width * 1.34;
      }}
      if (vh < 800) {{
        height = vh - 160;
        width = height / 1.34;
      }}

      pageFlip = new St.PageFlip(container, {{
        width: width,
        height: height,
        size: 'fixed',
        minWidth: 320,
        maxWidth: 700,
        minHeight: 450,
        maxHeight: 950,
        maxShadowOpacity: 0.6,
        showCover: true,
        mobileScrollSupport: false,
        useMouseEvents: true,
        drawShadow: true,
        flippingTime: 700
      }});

      pageFlip.loadFromHTML(document.querySelectorAll('.page'));

      updatePageIndicator(0);

      pageFlip.on('flip', (e) => {{
        updatePageIndicator(e.data);
      }});

      renderThumbnailsGrid();
    }}

    function updatePageIndicator(pageIdx) {{
      const total = 16;
      const indicator = document.getElementById('page-indicator');
      if (pageIdx === 0) {{
        indicator.innerText = 'Capa (Pág. 1 de 16)';
      }} else if (pageIdx >= total - 1) {{
        indicator.innerText = `Contracapa (Pág. ${{total}} de ${{total}})`;
      }} else {{
        const p1 = pageIdx + 1;
        const p2 = Math.min(pageIdx + 2, total);
        indicator.innerText = `Páginas ${{p1}}-${{p2}} de ${{total}}`;
      }}
    }}

    function flipNext() {{
      if (pageFlip) pageFlip.flipNext();
    }}

    function flipPrev() {{
      if (pageFlip) pageFlip.flipPrev();
    }}

    function goToPage(pageIndex) {{
      if (pageFlip) {{
        pageFlip.flip(pageIndex);
        const modal = document.getElementById('modal-thumbnails');
        if (modal) modal.classList.add('hidden');
      }}
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen();
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    function toggleThumbnails() {{
      const modal = document.getElementById('modal-thumbnails');
      modal.classList.toggle('hidden');
    }}

    function renderThumbnailsGrid() {{
      const grid = document.getElementById('thumbnails-grid');
      if (!grid) return;

      const titles = [
        "01. Capa Oficial",
        "02. Manifesto",
        "03. Índice dos Módulos",
        "04. Hero: Dashboard",
        "05. Ficha: Dashboard",
        "06. Hero: Financeiro",
        "07. Ficha: Financeiro",
        "08. Hero: Agenda",
        "09. Ficha: Agenda",
        "10. Hero: CRM",
        "11. Ficha: CRM",
        "12. Hero: Equipe",
        "13. Ficha: Equipe",
        "14. Hero: Insumos",
        "15. Ficha: Insumos",
        "16. Encerramento"
      ];

      grid.innerHTML = titles.map((t, idx) => `
        <button onclick="goToPage(${{idx}})" class="p-3 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-left transition-all hover:scale-105">
          <span class="text-[10px] text-[#0066D6] font-mono font-bold block mb-1">PÁG ${{idx + 1}}</span>
          <strong class="text-xs text-white block truncate">${{t}}</strong>
          <span class="text-[9px] text-slate-500">Clique para abrir</span>
        </button>
      `).join('');
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') flipNext();
      if (e.key === 'ArrowLeft') flipPrev();
      if (e.key === 'Escape') {{
        const modal = document.getElementById('modal-thumbnails');
        if (modal) modal.classList.add('hidden');
      }}
    }});

    window.addEventListener('DOMContentLoaded', () => {{
      setTimeout(initFlipbook, 100);
    }});

    window.addEventListener('resize', () => {{
      if (pageFlip) {{
        try {{
          pageFlip.destroy();
          setTimeout(initFlipbook, 150);
        }} catch(e) {{}}
      }}
    }});
  </script>
</body>
</html>
'''

# Escrever frontend/catalogo.html
with open("frontend/catalogo.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("SUCESSO: frontend/catalogo.html atualizado para 16 Páginas Black Edition!")
