import json
import base64
import os

# 1. Carregar imagens
cover_4k_path = "frontend/img/cover_4k.jpg"
with open(cover_4k_path, "rb") as f:
    cover_4k_b64 = base64.b64encode(f.read()).decode("utf-8")
cover_4k_uri = f"data:image/jpeg;base64,{cover_4k_b64}"

capa_path = "frontend/img/capa_oficial.png"
with open(capa_path, "rb") as f:
    capa_b64 = base64.b64encode(f.read()).decode("utf-8")
capa_uri = f"data:image/png;base64,{capa_b64}"

contracapa_path = "frontend/img/contracapa_oficial.jpg"
with open(contracapa_path, "rb") as f:
    contracapa_b64 = base64.b64encode(f.read()).decode("utf-8")
contracapa_uri = f"data:image/jpeg;base64,{contracapa_b64}"

logo_dark_path = "frontend/img/logo/habitat_dark.png"
with open(logo_dark_path, "rb") as f:
    logo_dark_b64 = base64.b64encode(f.read()).decode("utf-8")
logo_dark_uri = f"data:image/png;base64,{logo_dark_b64}"

logo_white_path = "frontend/img/logo/habitat_white.png"
with open(logo_white_path, "rb") as f:
    logo_white_b64 = base64.b64encode(f.read()).decode("utf-8")
logo_white_uri = f"data:image/png;base64,{logo_white_b64}"

# 2. Carregar biblioteca StPageFlip
with open("bundle_assets.json", "r", encoding="utf-8") as f:
    assets = json.load(f)
pageflip_js = assets["pageflip"]

# 3. Dados Completos e Detalhados dos 6 Módulos do Sistema 0
modules = [
    {
        "n": "01",
        "mod": "mod-blue",
        "color": "#0063B1",
        "area": "Gestão estratégica",
        "badge": "VISÃO 360°",
        "title": ["Dashboard", "analítico."],
        "screen": "bars",
        "promise": "O cockpit de controle do seu negócio em tempo real.",
        "summary": "Faturamento, ticket médio, margem líquida e produtividade da operação consolidados em uma única tela.",
        "speed": "< 250ms",
        "clicks": "1 clique",
        "architecture": "Edge Cached / Realtime",
        "diferenciais": [
            "Consolidação automática de todos os canais de receita e custos operacionais sem intervenção manual",
            "Gráficos preditivos com alertas antecipados de oscilação de margem e tendências de faturamento",
            "Indicadores de performance individual por profissional e coletiva da equipe em tempo real"
        ],
        "funcionalidades": [
            "Gráficos interativos em tempo real por período customizável",
            "DRE sintético visual com visão consolidada da empresa",
            "Ranking automático de serviços e produtos mais rentáveis",
            "Painel de metas dinâmico com termômetro de atingimento",
            "Visão multi-unidade e multi-empresa nativa da plataforma"
        ],
        "stack": [
            ("Stack Principal", "React 18 + Tailwind + FastAPI"),
            ("Segurança", "Criptografia AES-256 de Ponta"),
            ("Sincronização", "WebSockets em Tempo Real"),
            ("Exportação", "PDF, Excel e CSV em 1 Clique")
        ],
        "indicadores": [
            ("Tempo de consolidação de dados", "Instantâneo (0s)", 100),
            ("Redução do tempo de fechamento", "-85%", 85),
            ("Visibilidade de margem operacional", "100%", 100),
            ("Assertividade de previsibilidade", "98,4%", 98),
            ("Acesso em dispositivos móveis", "100% PWA", 100)
        ],
        "recomendacao": ("Ideal para gestores que tomam ", "decisões diárias", " sem esperar o fechamento contábil.")
    },
    {
        "n": "02",
        "mod": "mod-green",
        "color": "#16A34A",
        "area": "Inteligência financeira",
        "badge": "FLUXO DE CAIXA",
        "title": ["Gestão financeira", "& DRE gerencial."],
        "screen": "ledger",
        "promise": "Controle cirúrgico de cada centavo que entra e sai da empresa.",
        "summary": "Contas a pagar e receber, conciliação bancária, DRE e distribuição de lucro com rastreabilidade total.",
        "speed": "< 300ms",
        "clicks": "2 cliques",
        "architecture": "Audit Log Imutável",
        "diferenciais": [
            "DRE gerencial por regime de caixa e competência sem retrabalho ou digitação dupla",
            "Rastreabilidade total com comprovantes anexos em cada lançamento e histórico auditável",
            "Previsibilidade de inadimplência com régua de cobrança automática e conciliação bancária"
        ],
        "funcionalidades": [
            "Centro de custos e planos de contas totalmente personalizáveis",
            "Importação e conciliação de extratos OFX e Open Finance",
            "Simulador de ponto de equilíbrio e margem de contribuição",
            "Split de pagamentos e rateio automático de despesas fixas",
            "Alerta preventivo de contas a vencer via push e WhatsApp"
        ],
        "stack": [
            ("Stack Principal", "PostgreSQL Transacional"),
            ("Segurança", "Assinatura SHA-256 por Registro"),
            ("Sincronização", "Open Finance API e Webhooks"),
            ("Exportação", "SPED Contábil, OFX e Excel")
        ],
        "indicadores": [
            ("Redução de atrasos e inadimplência", "-42%", 42),
            ("Tempo economizado em conciliação", "12h / mês", 90),
            ("Precisão de projeção de caixa", "96,8%", 97),
            ("Conformidade fiscal e tributária", "100%", 100),
            ("Auditoria de lançamentos retroativos", "100% rastreado", 100)
        ],
        "recomendacao": ("Recomendado para operações que exigem ", "rigor contábil", " e eliminação de furos de caixa.")
    },
    {
        "n": "03",
        "mod": "mod-terra",
        "color": "#C2410C",
        "area": "Fluxo operacional",
        "badge": "AGENDAMENTO MULTI",
        "title": ["Agenda &", "atendimentos."],
        "screen": "calendar",
        "promise": "Zero conflito de horários e ocupação máxima da sua equipe.",
        "summary": "Calendário inteligente, reservas simultâneas, confirmação automática e cobrança de sinal.",
        "speed": "< 200ms",
        "clicks": "2 cliques",
        "architecture": "WebSockets Realtime",
        "diferenciais": [
            "Confirmação e lembretes automáticos por WhatsApp sem custo de API ou retrabalho de recepção",
            "Bloqueio anti-overbooking e gestão de salas, macas ou cadeiras com capacidade simultânea",
            "Histórico completo de comparecimento e cálculo imediato de no-show por cliente e profissional"
        ],
        "funcionalidades": [
            "Visão diária, semanal, mensal e filtro por profissional",
            "Link público de autoagendamento 24h para clientes finais",
            "Reserva com cobrança antecipada de sinal via PIX automático",
            "Encaixes inteligentes com fila de espera automatizada",
            "Sincronização bidirecional com Google Agenda e Apple Calendar"
        ],
        "stack": [
            ("Stack Principal", "FullCalendar + Redis Cache Lock"),
            ("Segurança", "LGPD com Termo de Consentimento"),
            ("Sincronização", "Notificações Push em Tempo Real"),
            ("Exportação", "ICS, iCal e Relatórios de Ocupação")
        ],
        "indicadores": [
            ("Redução de no-show (faltas)", "-70%", 70),
            ("Aumento na taxa de ocupação", "+34%", 34),
            ("Tempo confirmando horários", "-95%", 95),
            ("Tempo para novo atendimento", "8 segundos", 99),
            ("Satisfação com autoagendamento", "4,9 / 5,0", 98)
        ],
        "recomendacao": ("Essencial para ", "clínicas, salões e consultórios", " que trabalham com hora marcada.")
    },
    {
        "n": "04",
        "mod": "mod-wine",
        "color": "#9D174D",
        "area": "Relacionamento & vendas",
        "badge": "LTV & RETENÇÃO",
        "title": ["CRM de clientes", "& retenção."],
        "screen": "people",
        "promise": "Transforme clientes esporádicos em defensores fiéis da sua marca.",
        "summary": "Ficha cadastral, histórico de consumo, LTV, programa de pontos e funil de reativação.",
        "speed": "< 150ms",
        "clicks": "1 clique",
        "architecture": "PostgreSQL Indexado",
        "diferenciais": [
            "Dossiê unificado: compras anteriores, preferências, fotos e notas privadas em tela única",
            "Segmentação inteligente por frequência, ticket médio e última visita (RFM)",
            "Disparo automatizado de campanhas para reativação de clientes inativos"
        ],
        "funcionalidades": [
            "Ficha digital completa com fotos de antes e depois",
            "Cálculo automático do Lifetime Value (LTV) por cliente",
            "Histórico de preferências, restrições e ficha de anamnese",
            "Programa de pontos e fidelidade com resgate imediato",
            "Integração nativa com campanhas de WhatsApp e Meta Ads"
        ],
        "stack": [
            ("Stack Principal", "PostgreSQL com Índices Full-Text"),
            ("Segurança", "Anonimização de Dados Sensíveis"),
            ("Sincronização", "Instantânea com PDV e Financeiro"),
            ("Exportação", "CSV Segmentado e Relatório RFM")
        ],
        "indicadores": [
            ("Aumento de recompra em 90 dias", "+28%", 28),
            ("Taxa de reativação de inativos", "31,5%", 65),
            ("Acesso ao histórico completo", "< 1 seg", 100),
            ("Retenção com fidelidade ativa", "+45%", 45),
            ("NPS médio percebido", "89 pontos", 89)
        ],
        "recomendacao": ("Indicado para empresas que valorizam o ", "relacionamento próximo", " e querem faturar mais por cliente.")
    },
    {
        "n": "05",
        "mod": "mod-teal",
        "color": "#0D9488",
        "area": "Recursos humanos",
        "badge": "GESTÃO DE REPASSES",
        "title": ["Equipe, metas", "& comissões."],
        "screen": "team",
        "promise": "Transparência total que motiva colaboradores e elimina discussões.",
        "summary": "Comissionamento flexível, controle de acessos por cargo, produtividade e fechamento em 1 clique.",
        "speed": "< 200ms",
        "clicks": "1 clique",
        "architecture": "RBAC / Row Security",
        "diferenciais": [
            "Cálculo de comissão por serviço, produto, escala progressiva ou valor fixo",
            "Painel exclusivo do profissional para conferência em tempo real pelo celular",
            "Permissões granulares: cada colaborador visualiza apenas seus dados autorizados"
        ],
        "funcionalidades": [
            "Regras flexíveis de comissão sobre faturamento bruto ou líquido",
            "Controle de ponto digital e registro de jornada",
            "Fechamento de folha de repasse em 1 clique com recibo em PDF",
            "Mural de comunicados internos e alinhamento de metas",
            "Extrato individual de comissões com rastreio de cada comanda"
        ],
        "stack": [
            ("Stack Principal", "RBAC com Autenticação JWT"),
            ("Segurança", "Isolamento Estrito de Dados Financeiros"),
            ("Sincronização", "Cálculo no Momento do Fechamento"),
            ("Exportação", "Holerite de Repasse e Recibos em PDF")
        ],
        "indicadores": [
            ("Tempo calculando comissões no mês", "De 8h para 2min", 99),
            ("Erros em repasses de comissão", "0%", 100),
            ("Aumento no engajamento de metas", "+22%", 22),
            ("Segurança de permissões por cargo", "100% RBAC", 100),
            ("Transparência percebida pela equipe", "97%", 97)
        ],
        "recomendacao": ("Essencial para ", "estéticas, salões e estúdios", " com profissionais comissionados.")
    },
    {
        "n": "06",
        "mod": "mod-mustard",
        "color": "#B45309",
        "area": "Custos & suprimentos",
        "badge": "CONTROLE DE LOTES",
        "title": ["Serviços, insumos", "& fornecedores."],
        "screen": "stock",
        "promise": "Estoque sempre certo, sem falta e sem desperdício.",
        "summary": "Ficha técnica de serviços, consumo fracionado de insumos por atendimento e compras inteligentes.",
        "speed": "< 180ms",
        "clicks": "2 cliques",
        "architecture": "Ledger Imutável",
        "diferenciais": [
            "Baixa automática de insumos fracionados a cada serviço concluído no sistema",
            "Ponto de reposição automático com lista de compras sugerida baseada no histórico",
            "Controle rigoroso de lotes, datas de validade e alertas preventivos de vencimento"
        ],
        "funcionalidades": [
            "Ficha técnica com custo real por procedimento",
            "Entrada por nota fiscal XML com atualização automática de custos",
            "Auditoria de perdas, desperdícios e consumo interno",
            "Comparativo de preços e histórico de pedidos por fornecedor",
            "Inventário rápido com leitura de código de barras pelo celular"
        ],
        "stack": [
            ("Stack Principal", "PostgreSQL + Filas Assíncronas"),
            ("Segurança", "Trilha de Auditoria por Usuário"),
            ("Sincronização", "Baixa em Tempo Real na Comanda"),
            ("Exportação", "Pedidos em PDF e Curva ABC em Excel")
        ],
        "indicadores": [
            ("Redução de perdas por validade", "-60%", 60),
            ("Rupturas de estoque", "-80%", 80),
            ("Custo real por serviço visível", "100%", 100),
            ("Economia média em compras", "+15%", 15),
            ("Tempo de inventário mensal", "-70%", 70)
        ],
        "recomendacao": ("Indicado para quem quer saber o ", "custo real de cada serviço", " e parar de perder material.")
    }
]

# 4. Renderização dos Mockups Visuais das Telas (Design Limpo, Amplo e Legível)
def render_screen_mockup(kind, mod_color):
    if kind == "bars":
        return f'''
        <div class="flex flex-col gap-1 sm:gap-3">
          <div class="grid grid-cols-3 gap-1 sm:gap-2.5">
            <div class="rounded p-1 sm:p-3 bg-[#0063B1] text-white shadow-xs">
              <div class="text-[7px] sm:text-[10px] uppercase tracking-wider text-white/80 font-medium">Faturamento</div>
              <div class="text-[10px] sm:text-xl font-bold mt-0.5">R$ 84.500</div>
              <div class="text-[6px] sm:text-[9px] text-emerald-300 font-semibold mt-0.5">↑ +18,4%</div>
            </div>
            <div class="rounded p-1 sm:p-3 bg-slate-50 border border-slate-200">
              <div class="text-[7px] sm:text-[10px] uppercase tracking-wider text-slate-500 font-medium">Ticket Médio</div>
              <div class="text-[10px] sm:text-xl font-bold text-slate-800 mt-0.5">R$ 212,00</div>
              <div class="text-[6px] sm:text-[9px] text-slate-500 font-medium mt-0.5">428 atend.</div>
            </div>
            <div class="rounded p-1 sm:p-3 bg-slate-50 border border-slate-200">
              <div class="text-[7px] sm:text-[10px] uppercase tracking-wider text-slate-500 font-medium">Margem Líq.</div>
              <div class="text-[10px] sm:text-xl font-bold text-emerald-600 mt-0.5">31,4%</div>
              <div class="text-[6px] sm:text-[9px] text-emerald-600 font-medium mt-0.5">Meta: 28%</div>
            </div>
          </div>
          
          <div class="rounded bg-slate-50 border border-slate-200 p-1 sm:p-3.5">
            <div class="flex items-center justify-between text-[8px] sm:text-xs text-slate-600 mb-1 font-medium">
              <span>Evolução do Faturamento</span>
              <span class="text-[7px] sm:text-[10px] text-[#0063B1] font-bold">Consolidado</span>
            </div>
            <div class="flex items-end gap-1 sm:gap-2.5 h-14 sm:h-28 pt-1">
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1]/40 rounded-t h-[45%]"></div><span class="text-[6px] sm:text-[9px] text-slate-400 font-mono">Jan</span></div>
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1]/50 rounded-t h-[60%]"></div><span class="text-[6px] sm:text-[9px] text-slate-400 font-mono">Fev</span></div>
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1]/60 rounded-t h-[52%]"></div><span class="text-[6px] sm:text-[9px] text-slate-400 font-mono">Mar</span></div>
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1]/75 rounded-t h-[75%]"></div><span class="text-[6px] sm:text-[9px] text-slate-400 font-mono">Abr</span></div>
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1]/85 rounded-t h-[68%]"></div><span class="text-[6px] sm:text-[9px] text-slate-400 font-mono">Mai</span></div>
              <div class="flex-1 flex flex-col items-center gap-0.5"><div class="w-full bg-[#0063B1] rounded-t h-[92%] shadow-xs"></div><span class="text-[6px] sm:text-[9px] text-slate-700 font-bold font-mono">Jun</span></div>
            </div>
          </div>
        </div>
        '''

    elif kind == "ledger":
        return f'''
        <div class="flex flex-col gap-1 sm:gap-3">
          <div class="rounded p-1.5 sm:p-3.5 bg-emerald-50 border border-emerald-200 flex items-center justify-between">
            <div>
              <div class="text-[7px] sm:text-[10px] uppercase tracking-wider text-emerald-800 font-bold">Saldo em Caixa</div>
              <div class="text-xs sm:text-2xl font-bold text-emerald-700 mt-0.5">R$ 128.430,00</div>
              <div class="text-[6px] sm:text-[10px] text-emerald-600 font-medium">Projeção 30d: +10,6%</div>
            </div>
            <div class="h-6 sm:h-10 w-16 sm:w-24">
              <svg viewBox="0 0 100 30" class="h-full w-full">
                <polyline fill="none" stroke="#16A34A" stroke-width="2.5" points="0,25 20,20 40,22 60,12 80,15 100,4" />
              </svg>
            </div>
          </div>
          
          <div class="space-y-0.5 sm:space-y-1 border border-slate-200 rounded p-1 sm:p-2.5 bg-slate-50">
            <div class="flex items-center justify-between py-0.5 sm:py-1 px-1 border-b border-slate-200 text-[7px] sm:text-xs">
              <span class="font-medium text-slate-700">Receitas de Vendas (Cartão / PIX)</span>
              <span class="font-bold text-emerald-600">+ R$ 4.280,00</span>
            </div>
            <div class="flex items-center justify-between py-0.5 sm:py-1 px-1 border-b border-slate-200 text-[7px] sm:text-xs">
              <span class="font-medium text-slate-700">Fornecedor Distribuidora</span>
              <span class="font-bold text-red-600">- R$ 1.150,00</span>
            </div>
            <div class="flex items-center justify-between py-0.5 sm:py-1 px-1 text-[7px] sm:text-xs">
              <span class="font-medium text-slate-700">Comissões de Profissionais</span>
              <span class="font-bold text-red-600">- R$ 2.450,00</span>
            </div>
          </div>
        </div>
        '''

    elif kind == "calendar":
        return f'''
        <div class="flex flex-col gap-1 sm:gap-2.5">
          <div class="flex items-center justify-between text-[7px] sm:text-xs text-slate-600 font-medium pb-0.5 border-b border-slate-200">
            <span>Visão Semanal de Atendimentos</span>
            <span class="text-[6px] sm:text-[10px] bg-orange-100 text-orange-800 font-bold px-1.5 py-0.5 rounded">Ocupação: 88%</span>
          </div>
          <div class="grid grid-cols-5 gap-0.5 sm:gap-1.5">
            <div class="flex flex-col gap-0.5 sm:gap-1.5 rounded bg-slate-50 border border-slate-200 p-0.5 sm:p-2">
              <div class="text-center text-[7px] sm:text-[10px] font-bold text-slate-700 pb-0.5 border-b border-slate-200">SEG</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-600 text-white text-[6px] sm:text-[9px] font-bold text-center">09:00</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-100 text-orange-800 text-[6px] sm:text-[9px] font-semibold text-center">11:30</div>
            </div>
            <div class="flex flex-col gap-0.5 sm:gap-1.5 rounded bg-slate-50 border border-slate-200 p-0.5 sm:p-2">
              <div class="text-center text-[7px] sm:text-[10px] font-bold text-slate-700 pb-0.5 border-b border-slate-200">TER</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-100 text-orange-800 text-[6px] sm:text-[9px] font-semibold text-center">10:00</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-600 text-white text-[6px] sm:text-[9px] font-bold text-center">13:30</div>
            </div>
            <div class="flex flex-col gap-0.5 sm:gap-1.5 rounded bg-slate-50 border border-slate-200 p-0.5 sm:p-2">
              <div class="text-center text-[7px] sm:text-[10px] font-bold text-slate-700 pb-0.5 border-b border-slate-200">QUA</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-600 text-white text-[6px] sm:text-[9px] font-bold text-center">08:30</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-100 text-orange-800 text-[6px] sm:text-[9px] font-semibold text-center">11:00</div>
            </div>
            <div class="flex flex-col gap-0.5 sm:gap-1.5 rounded bg-slate-50 border border-slate-200 p-0.5 sm:p-2">
              <div class="text-center text-[7px] sm:text-[10px] font-bold text-slate-700 pb-0.5 border-b border-slate-200">QUI</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-100 text-orange-800 text-[6px] sm:text-[9px] font-semibold text-center">09:30</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-600 text-white text-[6px] sm:text-[9px] font-bold text-center">14:00</div>
            </div>
            <div class="flex flex-col gap-0.5 sm:gap-1.5 rounded bg-slate-50 border border-slate-200 p-0.5 sm:p-2">
              <div class="text-center text-[7px] sm:text-[10px] font-bold text-slate-700 pb-0.5 border-b border-slate-200">SEX</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-600 text-white text-[6px] sm:text-[9px] font-bold text-center">08:00</div>
              <div class="rounded p-0.5 sm:p-1 bg-orange-100 text-orange-800 text-[6px] sm:text-[9px] font-semibold text-center">10:30</div>
            </div>
          </div>
        </div>
        '''

    elif kind == "people":
        return f'''
        <div class="flex gap-1.5 sm:gap-3">
          <div class="w-1/3 space-y-0.5 sm:space-y-1.5 border-r border-slate-200 pr-1 sm:pr-2">
            <div class="text-[7px] sm:text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-0.5">VIP</div>
            <div class="rounded p-1 sm:p-2 bg-pink-50 border border-pink-200 text-[7px] sm:text-xs font-bold text-pink-900 truncate">Mariana S.</div>
            <div class="rounded p-1 sm:p-2 bg-slate-50 border border-slate-200 text-[7px] sm:text-xs font-medium text-slate-700 truncate">Carlos E.</div>
            <div class="rounded p-1 sm:p-2 bg-slate-50 border border-slate-200 text-[7px] sm:text-xs font-medium text-slate-700 truncate">Fernanda M.</div>
          </div>
          <div class="flex-1 rounded bg-pink-50 border border-pink-200 p-1 sm:p-3">
            <div class="flex items-center gap-1 sm:gap-2.5 pb-1 border-b border-pink-200">
              <div class="w-5 h-5 sm:w-8 sm:h-8 rounded-full bg-pink-700 text-white font-bold flex items-center justify-center text-[8px] sm:text-xs">MS</div>
              <div>
                <div class="text-[8px] sm:text-sm font-bold text-slate-800">Mariana Silva</div>
                <div class="text-[6px] sm:text-[10px] text-pink-700 font-semibold">Cliente VIP Ouro</div>
              </div>
            </div>
            <div class="grid grid-cols-3 gap-1 sm:gap-2 mt-1 sm:mt-2.5 text-center">
              <div class="rounded bg-white p-0.5 sm:p-2 border border-pink-100">
                <div class="text-[6px] sm:text-[9px] text-slate-500 uppercase font-semibold">LTV</div>
                <div class="text-[8px] sm:text-sm font-bold text-pink-700">R$ 4.250</div>
              </div>
              <div class="rounded bg-white p-0.5 sm:p-2 border border-pink-100">
                <div class="text-[6px] sm:text-[9px] text-slate-500 uppercase font-semibold">Visitas</div>
                <div class="text-[8px] sm:text-sm font-bold text-slate-800">38</div>
              </div>
              <div class="rounded bg-white p-0.5 sm:p-2 border border-pink-100">
                <div class="text-[6px] sm:text-[9px] text-slate-500 uppercase font-semibold">Pontos</div>
                <div class="text-[8px] sm:text-sm font-bold text-pink-700">920</div>
              </div>
            </div>
          </div>
        </div>
        '''

    elif kind == "team":
        return f'''
        <div class="space-y-1 sm:space-y-2">
          <div class="flex items-center justify-between text-[7px] sm:text-xs text-slate-600 font-medium pb-0.5 border-b border-slate-200">
            <span>Ranking da Equipe</span>
            <span class="text-[6px] sm:text-[10px] bg-teal-100 text-teal-800 font-bold px-1.5 py-0.5 rounded">Em 1 Clique</span>
          </div>
          <div class="space-y-1 sm:space-y-2 pt-0.5">
            <div class="flex items-center gap-1.5 sm:gap-3 p-1 sm:p-1.5 rounded bg-slate-50 border border-slate-200">
              <div class="w-4 h-4 sm:w-6 sm:h-6 rounded-full bg-teal-700 text-white font-bold text-[7px] sm:text-[10px] flex items-center justify-center">1</div>
              <div class="flex-1 min-w-0">
                <div class="flex justify-between text-[7px] sm:text-xs"><b>Ana Paula</b><span class="text-teal-700 font-bold">92%</span></div>
                <div class="h-1 sm:h-1.5 rounded-full bg-slate-200 mt-0.5"><div class="h-full rounded-full bg-teal-600" style="width: 92%"></div></div>
              </div>
              <div class="text-[7px] sm:text-xs font-bold text-teal-800">R$ 2.116</div>
            </div>
            <div class="flex items-center gap-1.5 sm:gap-3 p-1 sm:p-1.5 rounded bg-slate-50 border border-slate-200">
              <div class="w-4 h-4 sm:w-6 sm:h-6 rounded-full bg-slate-400 text-white font-bold text-[7px] sm:text-[10px] flex items-center justify-center">2</div>
              <div class="flex-1 min-w-0">
                <div class="flex justify-between text-[7px] sm:text-xs"><b>Bruno Costa</b><span class="text-teal-700 font-bold">78%</span></div>
                <div class="h-1 sm:h-1.5 rounded-full bg-slate-200 mt-0.5"><div class="h-full rounded-full bg-teal-600" style="width: 78%"></div></div>
              </div>
              <div class="text-[7px] sm:text-xs font-bold text-teal-800">R$ 1.794</div>
            </div>
          </div>
        </div>
        '''

    elif kind == "stock":
        return f'''
        <div class="space-y-1 sm:space-y-2">
          <div class="flex items-center justify-between text-[7px] sm:text-xs text-slate-600 font-medium pb-0.5 border-b border-slate-200">
            <span>Controle de Estoque & Reposição</span>
            <span class="text-[6px] sm:text-[10px] bg-amber-100 text-amber-900 font-bold px-1.5 py-0.5 rounded">Automático</span>
          </div>
          <div class="grid grid-cols-2 gap-1 sm:gap-2 pt-0.5">
            <div class="p-1 sm:p-2.5 rounded bg-slate-50 border border-slate-200">
              <div class="flex justify-between text-[7px] sm:text-xs font-bold text-slate-800"><span>Insumo A</span><span class="text-amber-800">80%</span></div>
              <div class="h-1 sm:h-1.5 rounded-full bg-slate-200 mt-1"><div class="h-full rounded-full bg-amber-600" style="width: 80%"></div></div>
            </div>
            <div class="p-1 sm:p-2.5 rounded bg-red-50 border border-red-200">
              <div class="flex justify-between text-[7px] sm:text-xs font-bold text-red-900"><span>Produto B</span><span class="text-red-700">15%</span></div>
              <div class="h-1 sm:h-1.5 rounded-full bg-red-200 mt-1"><div class="h-full rounded-full bg-red-600" style="width: 15%"></div></div>
            </div>
          </div>
        </div>
        '''

def render_tabs(active_idx=None):
    tabs_html = ""
    for i, m in enumerate(modules):
        is_active = (i == active_idx)
        w_class = "h-10 w-2.5 opacity-100 shadow-sm" if is_active else "h-6 w-1.5 opacity-30 hover:opacity-60"
        tabs_html += f'<div class="{m["mod"]} rounded-l bg-mod transition-all {w_class}"></div>'
    return f'''
    <div class="pointer-events-none absolute right-0 top-[15%] flex h-[65%] flex-col justify-between z-10">
      {tabs_html}
    </div>
    '''

def build_catalog():
    pages = []

    # =========================================================================
    # PÁGINA 1: CAPA OFICIAL (ANEXO DO USUÁRIO)
    # Lado direito: cursor de clique, Lado esquerdo: tipografia azul Sistema 0
    # =========================================================================
    p1 = f'''
    <div class="page page-right bg-black text-white relative w-full h-full overflow-hidden select-none">
      <img src="{capa_uri}" alt="Capa Sistema 0" class="w-full h-full object-cover select-none" />
    </div>
    '''
    pages.append(p1)

    # =========================================================================
    # PÁGINA 2: COSTAS DA CAPA (PRETO SÓLIDO + PROPÓSITO CENTRALIZADO)
    # =========================================================================
    p2 = f'''
    <div class="page page-left bg-black text-white relative w-full h-full overflow-hidden select-none">
      <div class="absolute inset-0 flex flex-col items-center justify-center text-center p-4 sm:p-8 md:p-12">
        <div class="max-w-md mx-auto space-y-3">
          <p class="text-xs font-semibold tracking-[0.25em] text-[#38BDF8] uppercase">PROPÓSITO</p>
          <h2 class="text-2xl sm:text-4xl lg:text-5xl font-light text-white leading-tight">
            Menos telas.<br />
            Menos planilhas.<br />
            <span class="font-bold">Mais decisão.</span>
          </h2>
        </div>
      </div>
      <div class="absolute bottom-4 left-1/2 -translate-x-1/2 pointer-events-none opacity-30">
        <img src="{logo_white_uri}" alt="Habitat Media" class="h-3.5 sm:h-4 w-auto object-contain select-none" />
      </div>
    </div>
    '''
    pages.append(p2)

    # =========================================================================
    # PÁGINA 3: SEGUNDA CAPA (4K ULTRA HD MASTER - APENAS A FOTOGRAFIA)
    # =========================================================================
    p3 = f'''
    <div class="page page-right bg-black text-white relative w-full h-full overflow-hidden select-none">
      <img src="{cover_4k_uri}" alt="Ambiente Sistema 0" class="w-full h-full object-cover object-center select-none" />
    </div>
    '''
    pages.append(p3)

    # =========================================================================
    # PÁGINAS 4 & 5: SUMÁRIO / ÍNDICE DOS MÓDULOS (DIAGRAMAÇÃO EDITORIAL)
    # =========================================================================
    # Pág 4: Sumário Esquerda
    p4 = f'''
    <div class="page page-left mod-blue bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
      <div class="border-b border-slate-200 pb-1 sm:pb-3">
        <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-[#0063B1]">Simplicidade Radical</span>
      </div>

      <div class="my-auto space-y-1 sm:space-y-4">
        <div>
          <h2 class="text-xs sm:text-3xl font-light text-slate-900 leading-tight">
            Toda a gestão<br />
            <b class="font-bold">em seis módulos.</b>
          </h2>
          <p class="mt-0.5 sm:mt-2 text-[7px] sm:text-sm text-slate-600 leading-snug line-clamp-2 sm:line-clamp-none font-light">
            Eliminamos menus labirínticos e burocracia para entregar uma ferramenta veloz e ágil.
          </p>
        </div>

        <div class="grid grid-cols-2 gap-1 sm:gap-2.5 pt-0.5">
          <div class="rounded p-1 sm:p-3 bg-[#0063B1] text-white flex flex-col justify-between h-10 sm:h-22 shadow-xs">
            <span class="text-[6px] sm:text-[10px] opacity-80 font-light">01</span>
            <div>
              <div class="text-[10px] sm:text-2xl font-bold leading-none">06</div>
              <div class="text-[6px] sm:text-[10px] opacity-90 mt-0.5 font-light">módulos</div>
            </div>
          </div>
          <div class="rounded p-1 sm:p-3 bg-slate-50 border border-slate-200 text-slate-900 flex flex-col justify-between h-10 sm:h-22">
            <span class="text-[6px] sm:text-[10px] text-slate-400 font-light">02</span>
            <div>
              <div class="text-[10px] sm:text-2xl font-bold leading-none">2</div>
              <div class="text-[6px] sm:text-[10px] text-slate-600 mt-0.5 font-light">cliques</div>
            </div>
          </div>
          <div class="rounded p-1 sm:p-3 bg-slate-50 border border-slate-200 text-slate-900 flex flex-col justify-between h-10 sm:h-22">
            <span class="text-[6px] sm:text-[10px] text-slate-400 font-light">03</span>
            <div>
              <div class="text-[10px] sm:text-2xl font-bold leading-none">&lt;300ms</div>
              <div class="text-[6px] sm:text-[10px] text-slate-600 mt-0.5 font-light">resposta</div>
            </div>
          </div>
          <div class="rounded p-1 sm:p-3 bg-[#16A34A] text-white flex flex-col justify-between h-10 sm:h-22 shadow-xs">
            <span class="text-[6px] sm:text-[10px] opacity-80 font-light">04</span>
            <div>
              <div class="text-[10px] sm:text-2xl font-bold leading-none">AES-256</div>
              <div class="text-[6px] sm:text-[10px] opacity-90 mt-0.5 font-light">segurança</div>
            </div>
          </div>
        </div>
      </div>

      <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
        <img src="{logo_dark_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
      </div>
    </div>
    '''
    pages.append(p4)

    # Pág 5: Sumário Direita (Lista dos 6 Módulos interativa)
    buttons_html = ""
    for i, m in enumerate(modules):
        target_folio_click = 6 + i * 4  # Posição física da página no flipbook
        display_num = 1 + i * 4        # Numeração editorial oficial do módulo
        buttons_html += f'''
        <button onclick="goToFolio({target_folio_click})" class="{m['mod']} group flex items-center gap-1 sm:gap-2.5 border-b border-slate-100 py-0.5 sm:py-2 text-left w-full cursor-pointer hover:bg-slate-50 px-1 rounded transition-colors">
          <span class="text-[10px] sm:text-base font-bold text-mod w-4 sm:w-6">{m['n']}</span>
          <div class="flex-1 min-w-0">
            <div class="text-[8px] sm:text-xs font-semibold text-slate-800 group-hover:text-mod transition-colors truncate">{' '.join(m['title']).replace('.', '')}</div>
          </div>
          <span class="text-[7px] sm:text-xs font-mono font-medium text-slate-400 group-hover:text-mod transition-colors">{display_num:02d}</span>
        </button>
        '''

    p5 = f'''
    <div class="page page-right mod-blue bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
      <div class="border-b border-slate-200 pb-1 sm:pb-2.5 flex justify-between items-center">
        <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-[#0063B1]">Sumário</span>
        <span class="text-[7px] sm:text-xs font-light text-slate-400">6 Módulos</span>
      </div>

      <div class="my-auto space-y-0.5">
        <div class="mb-0.5 sm:mb-2">
          <h3 class="text-xs sm:text-xl font-light text-slate-900">Índice dos <b class="font-bold">módulos.</b></h3>
        </div>
        {buttons_html}
      </div>

      {render_tabs()}
      <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
        <img src="{logo_dark_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
      </div>
    </div>
    '''
    pages.append(p5)

    # =========================================================================
    # OS 6 MÓDULOS (4 PÁGINAS POR MÓDULO):
    # SPREAD 1: ModuleOpening (Capa Hero à esquerda + Mockup da Tela à direita)
    # SPREAD 2: ModuleSheet (Diferenciais e Stack à esquerda + Indicadores à direita)
    # =========================================================================
    for i, m in enumerate(modules):
        p_hero = 1 + i * 4
        p_screen = 2 + i * 4
        p_sheet = 3 + i * 4
        p_indic = 4 + i * 4

        # ---------------------------------------------------------------------
        # PÁGINA ESQUERDA: ModuleOpening (Hero do Módulo)
        # ---------------------------------------------------------------------
        po_left = f'''
        <div class="page page-left {m['mod']} bg-mod text-white relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
          <div class="flex items-center justify-between border-b border-white/20 pb-1 sm:pb-3">
            <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-white/90">{m['area']}</span>
            <span class="text-[7px] sm:text-[10px] font-semibold uppercase tracking-wider bg-white/20 px-1.5 sm:px-2.5 py-0.5 rounded-full text-white">{m['badge']}</span>
          </div>

          <div class="my-auto space-y-1 sm:space-y-4">
            <div class="text-3xl sm:text-7xl md:text-8xl font-bold tracking-tight text-white leading-none opacity-95">
              {m['n']}
            </div>
            <h2 class="text-xs sm:text-3xl md:text-4xl font-light leading-[1.1] text-white">
              {m['title'][0]}<br />
              <b class="font-bold">{m['title'][1]}</b>
            </h2>
            <p class="text-[9px] sm:text-base md:text-lg font-medium leading-tight text-white/95 pt-0.5 sm:pt-2">
              {m['promise']}
            </p>
            <p class="text-[8px] sm:text-xs md:text-sm text-white/80 leading-snug line-clamp-2 sm:line-clamp-none font-light">
              {m['summary']}
            </p>
          </div>

          <div class="pt-1 sm:pt-4 border-t border-white/20 grid grid-cols-3 gap-1 sm:gap-2 text-white">
            <div>
              <div class="text-[6px] sm:text-[9px] uppercase tracking-wider text-white/70">Resposta</div>
              <div class="text-[8px] sm:text-xs font-bold text-white mt-0.5">{m['speed']}</div>
            </div>
            <div>
              <div class="text-[6px] sm:text-[9px] uppercase tracking-wider text-white/70">Operação</div>
              <div class="text-[8px] sm:text-xs font-bold text-white mt-0.5">{m['clicks']}</div>
            </div>
            <div>
              <div class="text-[6px] sm:text-[9px] uppercase tracking-wider text-white/70">Arquitetura</div>
              <div class="text-[8px] sm:text-xs font-bold text-white mt-0.5">{m['architecture']}</div>
            </div>
          </div>

          <div class="absolute bottom-1.5 left-3 sm:left-5 text-[8px] sm:text-xs text-white/50 font-light">{p_hero:02d}</div>
          <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
            <img src="{logo_white_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
          </div>
        </div>
        '''
        pages.append(po_left)

        # ---------------------------------------------------------------------
        # PÁGINA DIREITA: ModuleOpening (Mockup da Tela - Fundo Preto)
        # ---------------------------------------------------------------------
        po_right = f'''
        <div class="page page-right {m['mod']} bg-black text-white relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
          <div class="border-b border-white/10 pb-1 sm:pb-3 flex justify-between items-center">
            <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-mod">Tela Operacional</span>
            <span class="text-[7px] sm:text-[10px] text-white/40 uppercase">2 Cliques</span>
          </div>

          <div class="rounded-lg sm:rounded-xl border border-white/10 bg-white shadow-2xl overflow-hidden flex flex-col my-auto p-1.5 sm:p-4">
            {render_screen_mockup(m['screen'], m['color'])}
          </div>

          <div class="pt-1 sm:pt-3 border-t border-white/10">
            <div class="text-[8px] sm:text-sm font-semibold text-white truncate">{m['funcionalidades'][0]}</div>
          </div>

          {render_tabs(i)}
          <div class="absolute bottom-1.5 right-3 sm:right-5 text-[8px] sm:text-xs text-slate-500 font-light">{p_screen:02d}</div>
          <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
            <img src="{logo_white_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
          </div>
        </div>
        '''
        pages.append(po_right)

        # ---------------------------------------------------------------------
        # PÁGINA ESQUERDA: ModuleSheet (Ficha Técnica & Diferenciais)
        # ---------------------------------------------------------------------
        difs_html = "".join([
            f'<div class="flex gap-1.5 sm:gap-3 border-b border-slate-100 py-0.5 sm:py-2 text-[8px] sm:text-sm leading-tight text-slate-700">'
            f'  <span class="font-bold text-mod shrink-0 text-[8px] sm:text-sm">0{k + 1}</span><span>{d}</span>'
            f'</div>'
            for k, d in enumerate(m['diferenciais'])
        ])

        funcs_html = "".join([
            f'<div class="flex items-center gap-1 sm:gap-2 border-b border-slate-100 py-0.5 sm:py-1.5 text-[7px] sm:text-xs text-slate-700">'
            f'  <span class="w-1 h-1 sm:w-1.5 sm:h-1.5 rounded-full bg-mod shrink-0"></span><span class="truncate">{f}</span>'
            f'</div>'
            for f in m['funcionalidades']
        ])

        stack_html = "".join([
            f'<div class="border-b border-slate-100 py-0.5 sm:py-1.5">'
            f'  <div class="text-[6px] sm:text-[10px] uppercase tracking-wider text-slate-400 font-semibold">{s[0]}</div>'
            f'  <div class="text-[7px] sm:text-xs font-semibold text-slate-800 truncate">{s[1]}</div>'
            f'</div>'
            for s in m['stack']
        ])

        ps_left = f'''
        <div class="page page-left {m['mod']} bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-1 sm:pb-3">
              <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-mod">{m['n']} · Ficha Técnica</span>
              <span class="text-[7px] sm:text-[10px] text-slate-400 uppercase tracking-widest">{m['area']}</span>
            </div>
            
            <h2 class="text-xs sm:text-2xl md:text-3xl font-light text-slate-900 mt-1 sm:mt-3 leading-snug">
              {m['title'][0]} <b class="font-bold">{m['title'][1]}</b>
            </h2>

            <div class="mt-1 sm:mt-4">
              <div class="text-[7px] sm:text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-0.5 sm:mb-1">Diferenciais do Módulo</div>
              {difs_html}
            </div>

            <div class="mt-1 sm:mt-4 grid grid-cols-2 gap-1.5 sm:gap-4">
              <div>
                <div class="text-[7px] sm:text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-0.5 sm:mb-1">Funcionalidades</div>
                {funcs_html}
              </div>
              <div>
                <div class="text-[7px] sm:text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-0.5 sm:mb-1">Arquitetura & Segurança</div>
                {stack_html}
              </div>
            </div>
          </div>

          <div class="absolute bottom-1.5 left-3 sm:left-5 text-[8px] sm:text-xs text-slate-400 font-light">{p_sheet:02d}</div>
          <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
            <img src="{logo_dark_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
          </div>
        </div>
        '''
        pages.append(ps_left)

        # ---------------------------------------------------------------------
        # PÁGINA DIREITA: ModuleSheet (Indicadores & Recomendação com Balão Corrigido)
        # ---------------------------------------------------------------------
        indics_html = "".join([
            f'<div class="space-y-0.5 sm:space-y-1">'
            f'  <div class="flex justify-between text-[8px] sm:text-sm">'
            f'    <span class="text-slate-700 font-medium truncate">{ind[0]}</span><b class="text-mod font-bold ml-1">{ind[1]}</b>'
            f'  </div>'
            f'  <div class="h-1 sm:h-1.5 rounded-full bg-slate-100 overflow-hidden">'
            f'    <div class="h-full rounded-full bg-mod" style="width: {ind[2]}%"></div>'
            f'  </div>'
            f'</div>'
            for ind in m['indicadores']
        ])

        ps_right = f'''
        <div class="page page-right {m['mod']} bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-2 sm:p-7 md:p-10 pb-3 sm:pb-8 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-1 sm:pb-2.5">
              <span class="text-[8px] sm:text-xs font-bold uppercase tracking-[0.2em] text-mod">Indicadores Operacionais</span>
              <span class="text-[7px] sm:text-[10px] text-slate-400 uppercase tracking-widest font-mono">Métricas</span>
            </div>
            
            <h3 class="text-xs sm:text-xl md:text-2xl font-light text-slate-900 mt-1 sm:mt-2.5 leading-snug">
              O ganho, <b class="font-bold">visível de relance.</b>
            </h3>

            <div class="mt-1 sm:mt-4 space-y-0.5 sm:space-y-2 pr-1 sm:pr-4">
              {indics_html}
            </div>
          </div>

          <!-- Balão de Recomendação Redimensionado e Proporcional -->
          <div class="rounded-lg py-1 px-1.5 sm:py-3 sm:px-3.5 bg-mod-soft border border-mod/20 mt-1 sm:mt-3 mb-0.5 pr-1 sm:pr-4">
            <div class="text-sm sm:text-2xl font-serif text-mod leading-none opacity-40 mb-0.5">“</div>
            <p class="text-[7px] sm:text-xs leading-tight text-slate-800 font-light">
              {m['recomendacao'][0]}<b class="font-bold text-slate-900">{m['recomendacao'][1]}</b>{m['recomendacao'][2]}
            </p>
            <div class="mt-0.5 sm:mt-2 flex items-center gap-1 sm:gap-2">
              <div class="h-0.5 w-3 sm:w-5 bg-mod"></div>
              <span class="text-[6px] sm:text-[9px] font-bold text-slate-500 uppercase tracking-wider">Recomendação</span>
            </div>
          </div>

          {render_tabs(i)}
          <div class="absolute bottom-1.5 right-3 sm:right-5 text-[8px] sm:text-xs text-slate-400 font-light">{p_indic:02d}</div>
          <div class="absolute bottom-1 sm:bottom-2 left-1/2 -translate-x-1/2 pointer-events-none opacity-20">
            <img src="{logo_dark_uri}" alt="Habitat Media" class="h-2 sm:h-3 w-auto object-contain select-none" />
          </div>
        </div>
        '''
        pages.append(ps_right)

    # =========================================================================
    # PÁGINA FINAL: CONTRACAPA OFICIAL (IMAGEM OFICIAL ENVIADA PELO USUÁRIO)
    # =========================================================================
    p_cover_end = f'''
    <div class="page page-left bg-[#0063B1] text-white relative w-full h-full overflow-hidden select-none">
      <img src="{contracapa_uri}" alt="Contracapa Sistema 0" class="w-full h-full object-cover select-none" />
    </div>
    '''
    pages.append(p_cover_end)

    return pages

# 5. Gerar o HTML Completo com o Flipbook Interativo 3D
def generate_html():
    catalog_pages = build_catalog()
    pages_html = "\n".join(catalog_pages)
    total_pages = len(catalog_pages)

    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Catálogo Digital — Sistema 0</title>

  <!-- Fontes Oficiais do Sistema (Lexend & Atkinson) -->
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
            sans: ['"Lexend"', '"Atkinson Hyperlegible"', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Definições de Cores e Tokens do Lovable */
    :root {{
      --mod-blue: #0063B1;
      --mod-blue-soft: #EBF3FC;

      --mod-green: #16A34A;
      --mod-green-soft: #F0FDF4;

      --mod-terra: #C2410C;
      --mod-terra-soft: #FFF7ED;

      --mod-wine: #9D174D;
      --mod-wine-soft: #FDF2F8;

      --mod-teal: #0D9488;
      --mod-teal-soft: #F0FDFA;

      --mod-mustard: #B45309;
      --mod-mustard-soft: #FFFBEB;

      --mod-ink: #0F172A;
      --mod-ink-soft: #F8FAFC;
    }}

    .mod-blue {{ --mod: var(--mod-blue); --mod-soft: var(--mod-blue-soft); }}
    .mod-green {{ --mod: var(--mod-green); --mod-soft: var(--mod-green-soft); }}
    .mod-terra {{ --mod: var(--mod-terra); --mod-soft: var(--mod-terra-soft); }}
    .mod-wine {{ --mod: var(--mod-wine); --mod-soft: var(--mod-wine-soft); }}
    .mod-teal {{ --mod: var(--mod-teal); --mod-soft: var(--mod-teal-soft); }}
    .mod-mustard {{ --mod: var(--mod-mustard); --mod-soft: var(--mod-mustard-soft); }}
    .mod-ink {{ --mod: var(--mod-ink); --mod-soft: var(--mod-ink-soft); }}

    .bg-mod {{ background-color: var(--mod); }}
    .text-mod {{ color: var(--mod); }}
    .bg-mod-soft {{ background-color: var(--mod-soft); }}

    body {{
      font-family: 'Lexend', 'Atkinson Hyperlegible', sans-serif;
      background-color: #F1F4F9; /* Branco Gelo Sólido Editorial */
      color: #0F172A;
      overflow: hidden;
      user-select: none;
    }}

    .flip-book {{
      box-shadow: 0 25px 60px -15px rgba(15, 23, 42, 0.25), 0 0 1px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      border-radius: 4px;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.98);
      transition: opacity 0.35s ease-out, transform 0.35s ease-out;
    }}

    .flip-book.ready {{
      opacity: 1;
      visibility: visible;
      transform: scale(1);
    }}

    .page {{
      overflow: hidden;
      position: relative;
    }}

    .page-left {{
      box-shadow: inset -12px 0 16px -6px rgba(0, 0, 0, 0.10);
      border-right: 1px solid rgba(0, 0, 0, 0.05);
    }}

    .page-right {{
      box-shadow: inset 12px 0 16px -6px rgba(0, 0, 0, 0.10);
      border-left: 1px solid rgba(0, 0, 0, 0.05);
    }}
  </style>
</head>
<body class="h-screen w-screen flex flex-col justify-between bg-[#F1F4F9]">

  <!-- ================= TOP HEADER LIMPO EM BRANCO GELO ================= -->
  <header class="h-12 sm:h-14 px-3 sm:px-6 flex items-center justify-between border-b border-slate-200 bg-white/80 backdrop-blur-md z-30 shrink-0">
    <div class="flex items-center gap-1.5 sm:gap-3 min-w-0">
      <a href="/" class="flex items-center gap-1 px-2 py-1 rounded bg-white hover:bg-slate-100 text-slate-700 text-xs border border-slate-200 transition-colors shadow-2xs shrink-0" title="Voltar ao início">
        <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> <span class="hidden sm:inline">Voltar</span>
      </a>
      <span class="font-display font-semibold text-xs text-slate-800 tracking-wide uppercase truncate">Sistema 0</span>
    </div>

    <!-- Controles Rápidos -->
    <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
      <span id="page-indicator" class="font-sans text-[11px] sm:text-xs text-slate-600 bg-white border border-slate-200 px-2 sm:px-3 py-0.5 sm:py-1 rounded shadow-2xs font-medium whitespace-nowrap">
        Capa / {total_pages}
      </span>
      <button onclick="goToFolio(4)" class="hidden sm:flex px-2.5 sm:px-3 py-1 text-xs rounded bg-white hover:bg-slate-100 text-slate-700 items-center gap-1 transition-colors border border-slate-200 shadow-2xs cursor-pointer" title="Ir para o Sumário">
        <i data-lucide="grid" class="w-3.5 h-3.5"></i> <span>Sumário</span>
      </button>
      <a href="/catalogo.pdf" download class="px-2.5 sm:px-3 py-1 text-xs rounded bg-[#0063B1] hover:bg-blue-700 text-white flex items-center gap-1 font-medium transition-colors shadow">
        <i data-lucide="download" class="w-3.5 h-3.5"></i> <span>PDF</span>
      </a>
    </div>
  </header>

  <!-- ================= PALCO CENTRAL (LIVRO DIGITAL) ================= -->
  <main class="flex-1 flex items-center justify-center p-1 sm:p-3 md:p-4 overflow-hidden relative">
    <!-- Loader elegante de inicialização (elimina qualquer flash de tela) -->
    <div id="book-loader" class="absolute inset-0 flex flex-col items-center justify-center bg-[#F1F4F9] z-20 transition-opacity duration-300 pointer-events-none">
      <div class="w-8 h-8 rounded-full border-2 border-slate-300 border-t-[#0063B1] animate-spin mb-3"></div>
      <p class="text-[11px] font-medium text-slate-500 tracking-widest uppercase">Carregando catálogo...</p>
    </div>

    <button onclick="flipPrev()" class="hidden md:flex absolute left-4 lg:left-6 z-20 w-11 h-11 rounded-full bg-white/80 hover:bg-white border border-slate-200 text-slate-700 items-center justify-center transition-all hover:scale-105 shadow-md cursor-pointer">
      <i data-lucide="chevron-left" class="w-5 h-5"></i>
    </button>

    <div id="book-container" class="flip-book">
      {pages_html}
    </div>

    <button onclick="flipNext()" class="hidden md:flex absolute right-4 lg:right-6 z-20 w-11 h-11 rounded-full bg-white/80 hover:bg-white border border-slate-200 text-slate-700 items-center justify-center transition-all hover:scale-105 shadow-md cursor-pointer">
      <i data-lucide="chevron-right" class="w-5 h-5"></i>
    </button>
  </main>

  <!-- ================= BARRA INFERIOR (LEITURA EDITORIAL) ================= -->
  <footer class="h-10 sm:h-12 px-3 sm:px-6 flex items-center justify-between border-t border-slate-200 bg-white/60 text-slate-500 text-xs shrink-0">
    <div class="flex items-center gap-1.5 sm:gap-2">
      <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
      <span class="text-[10px] sm:text-[11px] font-light">Deslize com o dedo ou use as setas</span>
    </div>
    <div class="flex items-center gap-2 sm:gap-4">
      <button onclick="goToPage(0)" class="text-[10px] sm:text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Capa</button>
      <button onclick="goToFolio(4)" class="text-[10px] sm:text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Sumário</button>
      <button onclick="goToPage({total_pages - 1})" class="text-[10px] sm:text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Contracapa</button>
    </div>
  </footer>

  <!-- SCRIPT DO MOTOR STPAGEFLIP -->
  <script>
    {pageflip_js}
  </script>

  <script>
    let pageFlip = null;
    const totalPages = {total_pages};

    function initBook(startPage = 0) {{
      const container = document.getElementById("book-container");
      if (!container) return;

      if (window.lucide && typeof lucide.createIcons === 'function') {{
        lucide.createIcons();
      }}

      const vh = window.innerHeight;
      const vw = window.innerWidth;
      const isMobile = vw < 768;

      let width, height;

      // Sempre exibe as 2 Páginas Lado a Lado (Spread Duplo Completo de Revista):
      const availW = isMobile ? (vw - 8) : Math.min(vw - 60, 1400);
      const availH = isMobile ? (vh - 90) : (vh - 120);

      let singleW = Math.floor(availW / 2);
      let calcH = Math.floor(singleW * 1.414);

      if (calcH > availH) {{
        calcH = availH;
        singleW = Math.floor(calcH / 1.414);
      }}

      width = Math.max(150, singleW);
      height = Math.max(212, calcH);

      pageFlip = new St.PageFlip(container, {{
        width: width,
        height: height,
        size: 'fixed',
        minWidth: 150,
        maxWidth: 750,
        minHeight: 200,
        maxHeight: 1000,
        maxShadowOpacity: 0.35,
        showCover: true,
        usePortrait: false,
        mobileScrollSupport: false,
        useMouseEvents: true,
        clickEventForward: true,
        swipeDistance: 20,
        drawShadow: true,
        flippingTime: 380,
        startPage: startPage
      }});

      pageFlip.loadFromHTML(document.querySelectorAll(".page"));

      pageFlip.on("flip", (e) => {{
        updateIndicator(e.data);
      }});

      updateIndicator(startPage);
      setupTouchGestures();

      // Suaviza a entrada do livro montado, eliminando qualquer flash de tela (FOUC)
      requestAnimationFrame(() => {{
        container.classList.add("ready");
        const loader = document.getElementById("book-loader");
        if (loader) {{
          loader.style.opacity = "0";
          setTimeout(() => {{ if (loader) loader.remove(); }}, 320);
        }}
      }});
    }}

    function setupTouchGestures() {{
      let touchStartX = 0;
      let touchStartY = 0;
      let touchStartTime = 0;

      const mainArea = document.querySelector("main") || document.body;

      mainArea.addEventListener("touchstart", (e) => {{
        if (e.touches.length === 1) {{
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
          touchStartTime = Date.now();
        }}
      }}, {{ passive: true }});

      mainArea.addEventListener("touchend", (e) => {{
        if (e.changedTouches.length === 1) {{
          const deltaX = e.changedTouches[0].clientX - touchStartX;
          const deltaY = e.changedTouches[0].clientY - touchStartY;
          const elapsed = Date.now() - touchStartTime;

          // Se deslizou mais de 35px horizontalmente com predomínio sobre o vertical em até 800ms
          if (Math.abs(deltaX) > 35 && Math.abs(deltaX) > Math.abs(deltaY) * 1.1 && elapsed < 800) {{
            if (deltaX < 0) {{
              flipNext();
            }} else {{
              flipPrev();
            }}
          }}
        }}
      }}, {{ passive: true }});
    }}

    function updateIndicator(pageNum) {{
      const ind = document.getElementById("page-indicator");
      if (!ind) return;
      const isPortrait = pageFlip ? pageFlip.getOrientation() === 'portrait' : false;

      if (pageNum === 0) {{
        ind.innerText = "Capa / " + totalPages;
      }} else if (pageNum >= totalPages - 1) {{
        ind.innerText = "Contracapa / " + totalPages;
      }} else if (isPortrait) {{
        if (pageNum === 1) ind.innerText = "Verso Capa";
        else if (pageNum === 2) ind.innerText = "Segunda Capa";
        else if (pageNum === 3 || pageNum === 4) ind.innerText = "Sumário";
        else {{
          const p = pageNum - 4;
          ind.innerText = `Pág. ${{String(p).padStart(2, '0')}} / 24`;
        }}
      }} else {{
        if (pageNum < 5) {{
          if (pageNum === 1) ind.innerText = "Segunda Capa";
          else ind.innerText = "Sumário";
        }} else {{
          const p1 = pageNum - 4;
          const p2 = Math.min(pageNum - 3, 24);
          ind.innerText = `Pág. ${{String(p1).padStart(2, '0')}}–${{String(p2).padStart(2, '0')}}`;
        }}
      }}
    }}

    function flipPrev() {{
      if (pageFlip) pageFlip.flipPrev();
    }}

    function flipNext() {{
      if (pageFlip) pageFlip.flipNext();
    }}

    function goToPage(n) {{
      if (pageFlip) pageFlip.flip(n);
    }}

    function goToFolio(f) {{
      const pageIndex = Math.max(0, Math.min(totalPages - 1, f - 1));
      if (pageFlip) pageFlip.flip(pageIndex);
    }}

    document.addEventListener("keydown", (e) => {{
      if (e.key === "ArrowLeft") flipPrev();
      if (e.key === "ArrowRight") flipNext();
    }});

    window.addEventListener("resize", () => {{
      if (pageFlip) {{
        const cur = pageFlip.getCurrentPageIndex();
        try {{
          pageFlip.destroy();
          setTimeout(() => initBook(cur), 120);
        }} catch(e) {{}}
      }}
    }});

    window.addEventListener("DOMContentLoaded", () => {{
      initBook();
    }});
  </script>
</body>
</html>
'''
    return html_content

if __name__ == "__main__":
    html = generate_html()
    with open("frontend/catalogo.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("CATÁLOGO RECOMPILADO COM DESIGN EDITORIAL E INFORMAÇÕES COMPLETAS!")
