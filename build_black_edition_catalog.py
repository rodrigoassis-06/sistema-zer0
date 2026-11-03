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
        <div class="flex flex-col gap-3">
          <div class="grid grid-cols-3 gap-2.5">
            <div class="rounded-lg p-3 bg-[#0063B1] text-white shadow-xs">
              <div class="text-[10px] uppercase tracking-wider text-white/80 font-medium">Faturamento</div>
              <div class="text-lg sm:text-xl font-bold mt-0.5">R$ 84.500</div>
              <div class="text-[9px] text-emerald-300 font-semibold mt-1">↑ +18,4% no mês</div>
            </div>
            <div class="rounded-lg p-3 bg-slate-50 border border-slate-200">
              <div class="text-[10px] uppercase tracking-wider text-slate-500 font-medium">Ticket Médio</div>
              <div class="text-lg sm:text-xl font-bold text-slate-800 mt-0.5">R$ 212,00</div>
              <div class="text-[9px] text-slate-500 font-medium mt-1">428 atendimentos</div>
            </div>
            <div class="rounded-lg p-3 bg-slate-50 border border-slate-200">
              <div class="text-[10px] uppercase tracking-wider text-slate-500 font-medium">Margem Líquida</div>
              <div class="text-lg sm:text-xl font-bold text-emerald-600 mt-0.5">31,4%</div>
              <div class="text-[9px] text-emerald-600 font-medium mt-1">Meta: 28% (Superada)</div>
            </div>
          </div>
          
          <div class="rounded-lg bg-slate-50 border border-slate-200 p-3.5">
            <div class="flex items-center justify-between text-xs text-slate-600 mb-2 font-medium">
              <span>Evolução do Faturamento Mensal</span>
              <span class="text-[10px] text-[#0063B1] font-bold">Consolidado em Tempo Real</span>
            </div>
            <div class="flex items-end gap-2.5 h-28 pt-2">
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1]/40 rounded-t h-[45%]"></div><span class="text-[9px] text-slate-400 font-mono">Jan</span></div>
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1]/50 rounded-t h-[60%]"></div><span class="text-[9px] text-slate-400 font-mono">Fev</span></div>
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1]/60 rounded-t h-[52%]"></div><span class="text-[9px] text-slate-400 font-mono">Mar</span></div>
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1]/75 rounded-t h-[75%]"></div><span class="text-[9px] text-slate-400 font-mono">Abr</span></div>
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1]/85 rounded-t h-[68%]"></div><span class="text-[9px] text-slate-400 font-mono">Mai</span></div>
              <div class="flex-1 flex flex-col items-center gap-1"><div class="w-full bg-[#0063B1] rounded-t h-[92%] shadow-xs"></div><span class="text-[9px] text-slate-700 font-bold font-mono">Jun</span></div>
            </div>
          </div>
        </div>
        '''

    elif kind == "ledger":
        return f'''
        <div class="flex flex-col gap-3">
          <div class="rounded-lg p-3.5 bg-emerald-50 border border-emerald-200 flex items-center justify-between">
            <div>
              <div class="text-[10px] uppercase tracking-wider text-emerald-800 font-bold">Saldo Conciliado em Caixa</div>
              <div class="text-xl sm:text-2xl font-bold text-emerald-700 mt-0.5">R$ 128.430,00</div>
              <div class="text-[10px] text-emerald-600 font-medium mt-0.5">Projeção a 30 dias: R$ 142.100,00 (+10,6%)</div>
            </div>
            <div class="h-10 w-24">
              <svg viewBox="0 0 100 30" class="h-full w-full">
                <polyline fill="none" stroke="#16A34A" stroke-width="2.5" points="0,25 20,20 40,22 60,12 80,15 100,4" />
              </svg>
            </div>
          </div>
          
          <div class="space-y-1.5 border border-slate-200 rounded-lg p-2.5 bg-slate-50">
            <div class="flex items-center justify-between py-1 px-2 border-b border-slate-200 text-xs">
              <span class="font-medium text-slate-700">Receitas de Vendas (Cartão / PIX)</span>
              <span class="font-bold text-emerald-600">+ R$ 4.280,00</span>
            </div>
            <div class="flex items-center justify-between py-1 px-2 border-b border-slate-200 text-xs">
              <span class="font-medium text-slate-700">Fornecedor Distribuidora Master</span>
              <span class="font-bold text-red-600">- R$ 1.150,00</span>
            </div>
            <div class="flex items-center justify-between py-1 px-2 border-b border-slate-200 text-xs">
              <span class="font-medium text-slate-700">Comissões de Profissionais</span>
              <span class="font-bold text-red-600">- R$ 2.450,00</span>
            </div>
            <div class="flex items-center justify-between py-1 px-2 text-xs">
              <span class="font-medium text-slate-700">Serviço Recorrente Assinatura</span>
              <span class="font-bold text-emerald-600">+ R$ 890,00</span>
            </div>
          </div>
        </div>
        '''

    elif kind == "calendar":
        return f'''
        <div class="flex flex-col gap-2.5">
          <div class="flex items-center justify-between text-xs text-slate-600 font-medium pb-1 border-b border-slate-200">
            <span>Visão Semanal de Atendimentos</span>
            <span class="text-[10px] bg-orange-100 text-orange-800 font-bold px-2 py-0.5 rounded">Taxa de Ocupação: 88%</span>
          </div>
          <div class="grid grid-cols-5 gap-1.5">
            <div class="flex flex-col gap-1.5 rounded bg-slate-50 border border-slate-200 p-2">
              <div class="text-center text-[10px] font-bold text-slate-700 pb-1 border-b border-slate-200">SEG</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">09:00</div>
              <div class="rounded p-1 bg-orange-100 text-orange-800 text-[9px] font-semibold text-center">11:30</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">14:00</div>
            </div>
            <div class="flex flex-col gap-1.5 rounded bg-slate-50 border border-slate-200 p-2">
              <div class="text-center text-[10px] font-bold text-slate-700 pb-1 border-b border-slate-200">TER</div>
              <div class="rounded p-1 bg-orange-100 text-orange-800 text-[9px] font-semibold text-center">10:00</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">13:30</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">16:00</div>
            </div>
            <div class="flex flex-col gap-1.5 rounded bg-slate-50 border border-slate-200 p-2">
              <div class="text-center text-[10px] font-bold text-slate-700 pb-1 border-b border-slate-200">QUA</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">08:30</div>
              <div class="rounded p-1 bg-orange-100 text-orange-800 text-[9px] font-semibold text-center">11:00</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">15:00</div>
            </div>
            <div class="flex flex-col gap-1.5 rounded bg-slate-50 border border-slate-200 p-2">
              <div class="text-center text-[10px] font-bold text-slate-700 pb-1 border-b border-slate-200">QUI</div>
              <div class="rounded p-1 bg-orange-100 text-orange-800 text-[9px] font-semibold text-center">09:30</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">14:00</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">17:30</div>
            </div>
            <div class="flex flex-col gap-1.5 rounded bg-slate-50 border border-slate-200 p-2">
              <div class="text-center text-[10px] font-bold text-slate-700 pb-1 border-b border-slate-200">SEX</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">08:00</div>
              <div class="rounded p-1 bg-orange-600 text-white text-[9px] font-bold text-center">10:30</div>
              <div class="rounded p-1 bg-orange-100 text-orange-800 text-[9px] font-semibold text-center">16:00</div>
            </div>
          </div>
        </div>
        '''

    elif kind == "people":
        return f'''
        <div class="flex gap-3">
          <div class="w-1/3 space-y-1.5 border-r border-slate-200 pr-2">
            <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">Clientes VIP</div>
            <div class="rounded p-2 bg-pink-50 border border-pink-200 text-xs font-bold text-pink-900">Mariana S.</div>
            <div class="rounded p-2 bg-slate-50 border border-slate-200 text-xs font-medium text-slate-700">Carlos E.</div>
            <div class="rounded p-2 bg-slate-50 border border-slate-200 text-xs font-medium text-slate-700">Fernanda M.</div>
            <div class="rounded p-2 bg-slate-50 border border-slate-200 text-xs font-medium text-slate-700">Juliana R.</div>
          </div>
          <div class="flex-1 rounded-lg bg-pink-50 border border-pink-200 p-3">
            <div class="flex items-center gap-2.5 pb-2 border-b border-pink-200">
              <div class="w-8 h-8 rounded-full bg-pink-700 text-white font-bold flex items-center justify-center text-xs">MS</div>
              <div>
                <div class="text-sm font-bold text-slate-800">Mariana Silva</div>
                <div class="text-[10px] text-pink-700 font-semibold">Cliente VIP Ouro · Desde 2021</div>
              </div>
            </div>
            <div class="grid grid-cols-3 gap-2 mt-2.5 text-center">
              <div class="rounded bg-white p-2 border border-pink-100">
                <div class="text-[9px] text-slate-500 uppercase font-semibold">LTV Acumulado</div>
                <div class="text-sm font-bold text-pink-700 mt-0.5">R$ 4.250</div>
              </div>
              <div class="rounded bg-white p-2 border border-pink-100">
                <div class="text-[9px] text-slate-500 uppercase font-semibold">Visitas</div>
                <div class="text-sm font-bold text-slate-800 mt-0.5">38</div>
              </div>
              <div class="rounded bg-white p-2 border border-pink-100">
                <div class="text-[9px] text-slate-500 uppercase font-semibold">Pontos Fidelidade</div>
                <div class="text-sm font-bold text-pink-700 mt-0.5">920 pts</div>
              </div>
            </div>
          </div>
        </div>
        '''

    elif kind == "team":
        return f'''
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs text-slate-600 font-medium pb-1 border-b border-slate-200">
            <span>Ranking da Equipe no Mês</span>
            <span class="text-[10px] bg-teal-100 text-teal-800 font-bold px-2 py-0.5 rounded">Repasse em 1 Clique</span>
          </div>
          <div class="space-y-2 pt-1">
            <div class="flex items-center gap-3 p-1.5 rounded bg-slate-50 border border-slate-200">
              <div class="w-6 h-6 rounded-full bg-teal-700 text-white font-bold text-[10px] flex items-center justify-center">1</div>
              <div class="flex-1">
                <div class="flex justify-between text-xs"><b>Ana Paula</b><span class="text-teal-700 font-bold">92% da Meta</span></div>
                <div class="h-1.5 rounded-full bg-slate-200 mt-1"><div class="h-full rounded-full bg-teal-600" style="width: 92%"></div></div>
              </div>
              <div class="text-xs font-bold text-teal-800">R$ 2.116,00</div>
            </div>
            <div class="flex items-center gap-3 p-1.5 rounded bg-slate-50 border border-slate-200">
              <div class="w-6 h-6 rounded-full bg-slate-400 text-white font-bold text-[10px] flex items-center justify-center">2</div>
              <div class="flex-1">
                <div class="flex justify-between text-xs"><b>Bruno Costa</b><span class="text-teal-700 font-bold">78% da Meta</span></div>
                <div class="h-1.5 rounded-full bg-slate-200 mt-1"><div class="h-full rounded-full bg-teal-600" style="width: 78%"></div></div>
              </div>
              <div class="text-xs font-bold text-teal-800">R$ 1.794,00</div>
            </div>
            <div class="flex items-center gap-3 p-1.5 rounded bg-slate-50 border border-slate-200">
              <div class="w-6 h-6 rounded-full bg-slate-400 text-white font-bold text-[10px] flex items-center justify-center">3</div>
              <div class="flex-1">
                <div class="flex justify-between text-xs"><b>Carla Mendes</b><span class="text-teal-700 font-bold">64% da Meta</span></div>
                <div class="h-1.5 rounded-full bg-slate-200 mt-1"><div class="h-full rounded-full bg-teal-600" style="width: 64%"></div></div>
              </div>
              <div class="text-xs font-bold text-teal-800">R$ 1.472,00</div>
            </div>
          </div>
        </div>
        '''

    elif kind == "stock":
        return f'''
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs text-slate-600 font-medium pb-1 border-b border-slate-200">
            <span>Controle de Estoque & Reposição</span>
            <span class="text-[10px] bg-amber-100 text-amber-900 font-bold px-2 py-0.5 rounded">Baixa Automática</span>
          </div>
          <div class="grid grid-cols-2 gap-2 pt-1">
            <div class="p-2.5 rounded-lg bg-slate-50 border border-slate-200">
              <div class="flex justify-between text-xs font-bold text-slate-800"><span>Insumo Master A</span><span class="text-amber-800">80%</span></div>
              <div class="text-[9px] text-slate-500 mt-0.5">Validade: 12/2027 · Lote #482</div>
              <div class="h-1.5 rounded-full bg-slate-200 mt-1.5"><div class="h-full rounded-full bg-amber-600" style="width: 80%"></div></div>
            </div>
            <div class="p-2.5 rounded-lg bg-red-50 border border-red-200">
              <div class="flex justify-between text-xs font-bold text-red-900"><span>Produto Premium B</span><span class="text-red-700">15%</span></div>
              <div class="text-[9px] text-red-700 font-bold mt-0.5">ALERTA: Compra Sugerida</div>
              <div class="h-1.5 rounded-full bg-red-200 mt-1.5"><div class="h-full rounded-full bg-red-600" style="width: 15%"></div></div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-50 border border-slate-200">
              <div class="flex justify-between text-xs font-bold text-slate-800"><span>Ampola Regenerativa</span><span class="text-amber-800">65%</span></div>
              <div class="text-[9px] text-slate-500 mt-0.5">Validade: 09/2026 · Lote #311</div>
              <div class="h-1.5 rounded-full bg-slate-200 mt-1.5"><div class="h-full rounded-full bg-amber-600" style="width: 65%"></div></div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-50 border border-slate-200">
              <div class="flex justify-between text-xs font-bold text-slate-800"><span>Kit Descartável Multi</span><span class="text-amber-800">95%</span></div>
              <div class="text-[9px] text-slate-500 mt-0.5">Estoque Pleno · 140 un</div>
              <div class="h-1.5 rounded-full bg-slate-200 mt-1.5"><div class="h-full rounded-full bg-amber-600" style="width: 95%"></div></div>
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
      <div class="absolute inset-0 flex flex-col items-center justify-center text-center p-8 sm:p-12">
        <div class="max-w-md mx-auto space-y-3">
          <p class="text-xs font-semibold tracking-[0.25em] text-[#38BDF8] uppercase">PROPÓSITO</p>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-light text-white leading-tight">
            Menos telas.<br />
            Menos planilhas.<br />
            <span class="font-bold">Mais decisão.</span>
          </h2>
        </div>
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
    <div class="page page-left mod-blue bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
      <div class="border-b border-slate-200 pb-3">
        <span class="text-xs font-bold uppercase tracking-[0.25em] text-[#0063B1]">Simplicidade Radical</span>
      </div>

      <div class="my-auto space-y-6">
        <div>
          <h2 class="text-3xl sm:text-4xl font-light text-slate-900 leading-tight">
            Toda a gestão<br />
            <b class="font-bold">em seis módulos.</b>
          </h2>
          <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-light">
            Eliminamos menus labirínticos e burocracia para entregar uma ferramenta veloz, ágil e focada em tomada de decisão em tempo real.
          </p>
        </div>

        <div class="grid grid-cols-2 gap-3 pt-2">
          <div class="rounded-xl p-3.5 bg-[#0063B1] text-white flex flex-col justify-between h-24 shadow-xs">
            <span class="text-[10px] opacity-80 font-light">01</span>
            <div>
              <div class="text-2xl font-bold leading-none">06</div>
              <div class="text-[11px] opacity-90 mt-1 font-light">módulos integrados</div>
            </div>
          </div>
          <div class="rounded-xl p-3.5 bg-slate-50 border border-slate-200 text-slate-900 flex flex-col justify-between h-24">
            <span class="text-[10px] text-slate-400 font-light">02</span>
            <div>
              <div class="text-2xl font-bold leading-none">2</div>
              <div class="text-[11px] text-slate-600 mt-1 font-light">cliques por operação</div>
            </div>
          </div>
          <div class="rounded-xl p-3.5 bg-slate-50 border border-slate-200 text-slate-900 flex flex-col justify-between h-24">
            <span class="text-[10px] text-slate-400 font-light">03</span>
            <div>
              <div class="text-2xl font-bold leading-none">&lt;300ms</div>
              <div class="text-[11px] text-slate-600 mt-1 font-light">tempo de resposta</div>
            </div>
          </div>
          <div class="rounded-xl p-3.5 bg-[#16A34A] text-white flex flex-col justify-between h-24 shadow-xs">
            <span class="text-[10px] opacity-80 font-light">04</span>
            <div>
              <div class="text-2xl font-bold leading-none">AES-256</div>
              <div class="text-[11px] opacity-90 mt-1 font-light">criptografia de ponta</div>
            </div>
          </div>
        </div>
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
        <button onclick="goToFolio({target_folio_click})" class="{m['mod']} group flex items-center gap-3.5 border-b border-slate-200 py-3 text-left w-full cursor-pointer hover:bg-slate-50 px-2 rounded-lg transition-colors">
          <span class="text-lg font-bold text-mod w-7">{m['n']}</span>
          <div class="flex-1">
            <div class="text-sm font-semibold text-slate-800 group-hover:text-mod transition-colors">{' '.join(m['title']).replace('.', '')}</div>
            <div class="text-[10px] text-slate-500 uppercase tracking-wider">{m['area']}</div>
          </div>
          <span class="text-xs font-mono font-medium text-slate-400 group-hover:text-mod transition-colors">{display_num:02d}</span>
        </button>
        '''

    p5 = f'''
    <div class="page page-right mod-blue bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
      <div class="border-b border-slate-200 pb-3 flex justify-between items-center">
        <span class="text-xs font-bold uppercase tracking-[0.25em] text-[#0063B1]">Sumário</span>
        <span class="text-xs font-light text-slate-400">6 Soluções Integradas</span>
      </div>

      <div class="my-auto space-y-1">
        <div class="mb-4">
          <h3 class="text-2xl font-light text-slate-900">Índice dos <b class="font-bold">módulos.</b></h3>
          <p class="text-xs text-slate-500 mt-1 font-light">Clique em qualquer módulo para navegar diretamente para ele.</p>
        </div>
        {buttons_html}
      </div>

      {render_tabs()}
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
        <div class="page page-left {m['mod']} bg-mod text-white relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
          <div class="flex items-center justify-between border-b border-white/20 pb-3">
            <span class="text-xs font-bold uppercase tracking-[0.25em] text-white/90">{m['area']}</span>
            <span class="text-[10px] font-semibold uppercase tracking-wider bg-white/20 px-2.5 py-0.5 rounded-full text-white">{m['badge']}</span>
          </div>

          <div class="my-auto space-y-4">
            <div class="text-7xl sm:text-8xl font-bold tracking-tight text-white leading-none opacity-95">
              {m['n']}
            </div>
            <h2 class="text-3xl sm:text-4xl font-light leading-[1.1] text-white">
              {m['title'][0]}<br />
              <b class="font-bold">{m['title'][1]}</b>
            </h2>
            <p class="text-base sm:text-lg font-medium leading-snug text-white/95 pt-2">
              {m['promise']}
            </p>
            <p class="text-xs sm:text-sm text-white/80 leading-relaxed font-light">
              {m['summary']}
            </p>
          </div>

          <div class="pt-4 border-t border-white/20 grid grid-cols-3 gap-2 text-white">
            <div>
              <div class="text-[9px] uppercase tracking-wider text-white/70">Resposta</div>
              <div class="text-xs font-bold text-white mt-0.5">{m['speed']}</div>
            </div>
            <div>
              <div class="text-[9px] uppercase tracking-wider text-white/70">Operação</div>
              <div class="text-xs font-bold text-white mt-0.5">{m['clicks']}</div>
            </div>
            <div>
              <div class="text-[9px] uppercase tracking-wider text-white/70">Arquitetura</div>
              <div class="text-xs font-bold text-white mt-0.5">{m['architecture']}</div>
            </div>
          </div>

          <div class="absolute bottom-3 left-6 text-xs text-white/50 font-light">{p_hero:02d}</div>
        </div>
        '''
        pages.append(po_left)

        # ---------------------------------------------------------------------
        # PÁGINA DIREITA: ModuleOpening (Mockup da Tela - Fundo Preto)
        # ---------------------------------------------------------------------
        po_right = f'''
        <div class="page page-right {m['mod']} bg-black text-white relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
          <div class="border-b border-white/10 pb-3">
            <span class="text-xs font-bold uppercase tracking-[0.2em] text-mod">Tela Operacional</span>
          </div>

          <div class="rounded-xl border border-white/10 bg-white shadow-2xl overflow-hidden flex flex-col my-auto p-4 sm:p-5">
            {render_screen_mockup(m['screen'], m['color'])}
          </div>

          <div class="pt-3 border-t border-white/10">
            <div class="text-xs font-semibold text-white">{m['funcionalidades'][0]}</div>
            <div class="text-[11px] text-slate-400 font-light mt-0.5">Interface simplificada em 2 cliques, sem menus labirínticos.</div>
          </div>

          {render_tabs(i)}
          <div class="absolute bottom-3 right-6 text-xs text-slate-500 font-light">{p_screen:02d}</div>
        </div>
        '''
        pages.append(po_right)

        # ---------------------------------------------------------------------
        # PÁGINA ESQUERDA: ModuleSheet (Ficha Técnica & Diferenciais)
        # ---------------------------------------------------------------------
        difs_html = "".join([
            f'<div class="flex gap-3 border-b border-slate-100 py-2.5 text-xs sm:text-sm leading-relaxed text-slate-700">'
            f'  <span class="font-bold text-mod shrink-0 text-sm">0{k + 1}</span><span>{d}</span>'
            f'</div>'
            for k, d in enumerate(m['diferenciais'])
        ])

        funcs_html = "".join([
            f'<div class="flex items-center gap-2 border-b border-slate-100 py-1.5 text-xs text-slate-700">'
            f'  <span class="w-1.5 h-1.5 rounded-full bg-mod shrink-0"></span><span>{f}</span>'
            f'</div>'
            for f in m['funcionalidades']
        ])

        stack_html = "".join([
            f'<div class="border-b border-slate-100 py-1.5">'
            f'  <div class="text-[10px] uppercase tracking-wider text-slate-400 font-semibold">{s[0]}</div>'
            f'  <div class="text-xs font-semibold text-slate-800">{s[1]}</div>'
            f'</div>'
            for s in m['stack']
        ])

        ps_left = f'''
        <div class="page page-left {m['mod']} bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-3">
              <span class="text-xs font-bold uppercase tracking-[0.2em] text-mod">{m['n']} · Ficha Técnica</span>
              <span class="text-[10px] text-slate-400 uppercase tracking-widest">{m['area']}</span>
            </div>
            
            <h2 class="text-2xl sm:text-3xl font-light text-slate-900 mt-3 leading-snug">
              {m['title'][0]} <b class="font-bold">{m['title'][1]}</b>
            </h2>

            <div class="mt-4">
              <div class="text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-1">Diferenciais do Módulo</div>
              {difs_html}
            </div>

            <div class="mt-4 grid grid-cols-2 gap-4">
              <div>
                <div class="text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-1">Funcionalidades</div>
                {funcs_html}
              </div>
              <div>
                <div class="text-[10px] font-bold uppercase tracking-widest text-slate-400 mb-1">Arquitetura & Segurança</div>
                {stack_html}
              </div>
            </div>
          </div>

          <div class="absolute bottom-3 left-6 text-xs text-slate-400 font-light">{p_sheet:02d}</div>
        </div>
        '''
        pages.append(ps_left)

        # ---------------------------------------------------------------------
        # PÁGINA DIREITA: ModuleSheet (Indicadores & Recomendação com Balão Corrigido)
        # ---------------------------------------------------------------------
        indics_html = "".join([
            f'<div class="space-y-1">'
            f'  <div class="flex justify-between text-xs sm:text-sm">'
            f'    <span class="text-slate-700 font-medium">{ind[0]}</span><b class="text-mod font-bold">{ind[1]}</b>'
            f'  </div>'
            f'  <div class="h-1.5 rounded-full bg-slate-100 overflow-hidden">'
            f'    <div class="h-full rounded-full bg-mod" style="width: {ind[2]}%"></div>'
            f'  </div>'
            f'</div>'
            for ind in m['indicadores']
        ])

        ps_right = f'''
        <div class="page page-right {m['mod']} bg-white text-slate-900 relative w-full h-full overflow-hidden select-none p-8 sm:p-10 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2.5">
              <span class="text-xs font-bold uppercase tracking-[0.2em] text-mod">Indicadores Operacionais</span>
              <span class="text-[10px] text-slate-400 uppercase tracking-widest font-mono">Métricas Reais</span>
            </div>
            
            <h3 class="text-xl sm:text-2xl font-light text-slate-900 mt-2.5 leading-snug">
              O ganho, <b class="font-bold">visível de relance.</b>
            </h3>

            <div class="mt-4 space-y-2 pr-4">
              {indics_html}
            </div>
          </div>

          <!-- Balão de Recomendação Redimensionado e Proporcional -->
          <div class="rounded-xl py-3 px-3.5 bg-mod-soft border border-mod/20 mt-3 mb-1 pr-4">
            <div class="text-2xl font-serif text-mod leading-none opacity-40 mb-1">“</div>
            <p class="text-xs leading-relaxed text-slate-800 font-light">
              {m['recomendacao'][0]}<b class="font-bold text-slate-900">{m['recomendacao'][1]}</b>{m['recomendacao'][2]}
            </p>
            <div class="mt-2 flex items-center gap-2">
              <div class="h-0.5 w-5 bg-mod"></div>
              <span class="text-[9px] font-bold text-slate-500 uppercase tracking-wider">Recomendação de Uso</span>
            </div>
          </div>

          {render_tabs(i)}
          <div class="absolute bottom-3 right-6 text-xs text-slate-400 font-light">{p_indic:02d}</div>
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
  <header class="h-14 px-6 flex items-center justify-between border-b border-slate-200 bg-white/70 backdrop-blur-md z-30">
    <div class="flex items-center gap-3">
      <a href="/" class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-white hover:bg-slate-100 text-slate-700 text-xs border border-slate-200 transition-colors shadow-2xs">
        <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> <span>Voltar</span>
      </a>
      <div class="h-4 w-[1px] bg-slate-200"></div>
      <span class="font-display font-medium text-xs text-slate-800 tracking-wide uppercase">Catálogo Digital — Sistema 0</span>
    </div>

    <!-- Controles Rápidos -->
    <div class="flex items-center gap-2">
      <span id="page-indicator" class="font-sans text-xs text-slate-500 bg-white border border-slate-200 px-3 py-1 rounded shadow-2xs font-light">
        1 / {total_pages}
      </span>
      <button onclick="goToFolio(4)" class="px-3 py-1 text-xs rounded bg-white hover:bg-slate-100 text-slate-700 flex items-center gap-1.5 transition-colors border border-slate-200 shadow-2xs cursor-pointer">
        <i data-lucide="grid" class="w-3.5 h-3.5"></i> <span>Sumário</span>
      </button>
      <a href="/catalogo.pdf" download class="px-3 py-1 text-xs rounded bg-[#0063B1] hover:bg-blue-700 text-white flex items-center gap-1.5 font-medium transition-colors shadow">
        <i data-lucide="download" class="w-3.5 h-3.5"></i> <span>PDF</span>
      </a>
    </div>
  </header>

  <!-- ================= PALCO CENTRAL (LIVRO DIGITAL) ================= -->
  <main class="flex-1 flex items-center justify-center p-2 sm:p-4 overflow-hidden relative">
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
  <footer class="h-12 px-4 sm:px-6 flex items-center justify-between border-t border-slate-200 bg-white/60 text-slate-500 text-xs">
    <div class="flex items-center gap-2">
      <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
      <span class="text-[11px] font-light">Deslize com o dedo ou use as setas para folhear</span>
    </div>
    <div class="flex items-center gap-3 sm:gap-4">
      <button onclick="goToPage(0)" class="text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Capa</button>
      <button onclick="goToFolio(4)" class="text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Sumário</button>
      <button onclick="goToPage({total_pages - 1})" class="text-[11px] text-slate-600 hover:text-blue-600 font-light cursor-pointer">Contracapa</button>
    </div>
  </footer>

  <!-- SCRIPT DO MOTOR STPAGEFLIP -->
  <script>
    {pageflip_js}
  </script>

  <script>
    let pageFlip = null;
    const totalPages = {total_pages};

    function initBook() {{
      const container = document.getElementById("book-container");
      if (!container) return;

      const vh = window.innerHeight;
      const vw = window.innerWidth;
      
      let width, height;

      if (vw < 768) {{
        // Celular: 1 página por vez, ajustada à largura da tela
        width = Math.min(460, vw - 24);
        height = Math.min(Math.round(width * 1.414), vh - 125);
        width = Math.round(height / 1.414);
      }} else if (vw < 1100) {{
        // Tablet: 2 páginas ajustadas
        width = Math.min(420, (vw - 60) / 2);
        height = Math.round(width * 1.414);
      }} else {{
        // Desktop: 2 páginas editoriais completas
        height = Math.min(780, vh - 150);
        width = Math.round(height / 1.414);
      }}

      pageFlip = new St.PageFlip(container, {{
        width: width,
        height: height,
        size: 'fixed',
        minWidth: 260,
        maxWidth: 600,
        minHeight: 360,
        maxHeight: 850,
        maxShadowOpacity: 0.35,
        showCover: true,
        usePortrait: true,
        mobileScrollSupport: false,
        useMouseEvents: true,
        clickEventForward: true,
        swipeDistance: 25,
        drawShadow: true,
        flippingTime: 380
      }});

      pageFlip.loadFromHTML(document.querySelectorAll(".page"));

      pageFlip.on("flip", (e) => {{
        updateIndicator(e.data);
      }});

      updateIndicator(0);
      setupTouchGestures();
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
      const isPortrait = pageFlip ? pageFlip.getOrientation() === 'portrait' : window.innerWidth < 768;

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
        try {{
          pageFlip.destroy();
          setTimeout(initBook, 150);
        }} catch(e) {{}}
      }}
    }});

    window.addEventListener("DOMContentLoaded", () => {{
      initBook();
      lucide.createIcons();
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
