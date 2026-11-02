# Sistema 0 — Documentação Oficial & Descritivo do Projeto

> **Visão Geral da Solução:**  
> O **Sistema 0** é uma plataforma universal e modular de gestão empresarial integrada (ERP & CRM Multi-Nicho), desenvolvida para atender empresas e profissionais de **qualquer segmento de mercado** — desde prestadores de serviços, comércio e varejo até clínicas, consultorias, agências, assistências técnicas e distribuidoras. A plataforma une agilidade operacional diária, controle financeiro rigoroso e fidelização de clientes em uma interface visual de alto impacto inspirada no consagrado conceito *Metro/Modern UI*, com suporte nativo a temas Escuro e Claro.

---

## 1. Posicionamento Multi-Nicho & Proposta de Valor Universal

Diferente de ferramentas engessadas ou restritas a segmentos específicos, o **Sistema 0** foi concebido com uma **arquitetura modular e adaptável**, permitindo que qualquer tipo de negócio configure e utilize suas ferramentas com total fluidez:

* **Universalidade de Aplicação:** Atende com a mesma excelência comércios (controle de fornecedores, caixa e DRE), consultorias e agências (acompanhamento de metas e clientes), clínicas e estéticas (agendamentos e anti-falta via WhatsApp) e prestadores de serviços em geral (controle de fila, comissões de equipe e ordens de atendimento).
* **Eliminação de Barreiras:** Substitui a fragmentação de planilhas manuais, anotações descentralizadas e softwares complexos por um ecossistema rápido, unificado e visualmente intuitivo.
* **Interface Produtiva Metro:** Com blocos dinâmicos (*Live Tiles*), o Sistema 0 elimina barreiras de usabilidade para recepcionistas, gestores e operadores, permitindo que a equipe foque no crescimento do negócio enquanto a plataforma automatiza a operação diária.

---

## 2. Arquitetura e Engenharia do Sistema

* **Backend:** FastAPI (Python 3.12+), com arquitetura assíncrona de alto desempenho, documentação automática OpenAPI/Swagger e tipagem estrita com Pydantic.
* **Banco de Dados:** SQLAlchemy ORM com suporte nativo a SQLite e PostgreSQL (totalmente compatível com Supabase e instâncias em nuvem).
* **Frontend:** Aplicação em página única (*Single-Page Application*), estilizada com Tailwind CSS, ícones vetoriais Lucide e visualizações de dados interativas com Chart.js.
* **Segurança e Multitenancy:** Autenticação baseada em JWT (*JSON Web Tokens*), senhas criptografadas com bcrypt e isolamento seguro por organização (*tenant*).
* **Design & Acessibilidade:** Interface adaptativa construída com fontes otimizadas para leitura (*FS Me*, *Lexend*, *Atkinson Hyperlegible*), alto contraste e persistência local de preferências.

---

## 3. Módulos e Funcionalidades

### 3.1. Tela Inicial Executiva (*Metro Start Screen*)
* **Blocos Vivos (*Live Tiles*):** Cartões interativos que alternam faces dinamicamente para exibir métricas-chave em tempo real sem exigir cliques (receitas, despesas, equipe em atendimento, próximos clientes, etc.).
* **Acesso Rápido com Cores Semânticas:** Botões em destaque azul, verde-limão e grafite para navegação instantânea às áreas operacionais e financeiras.
* **Alternância de Tema em 1 Clique:** Suporte integrado a **Modo Escuro** (fundo preto `#000000` e cartões `#1A1D24`) e **Modo Claro** (fundo `#F8FAFC` e cartões brancos `#FFFFFF` em alto contraste).
* **Central de Notificações e Avisos (Sino):** Dropdown flutuante que consolida alertas automáticos de contas a vencer, atendimentos pendentes e avisos prioritários.

---

### 3.2. Dashboard Analítico & Projeções
* **Linha de KPIs Executivos com Sparklines:** Monitoramento de Faturamento Total, Quantidade de Pedidos/Serviços, Ticket Médio e Novos Clientes com indicadores visuais de variação percentual.
* **Faturamento Mensal (Gráfico Spline):** Curvas dinâmicas de Receitas versus Despesas com gradientes visuais.
* **Simulador e Projeção Mês a Mês:** Barra de navegação rápida pelos 12 meses do ano que recalcula dinamicamente a receita prevista, despesa estimada, saldo projetado e percentual da meta atingida.
* **Vendas por Canal (Gráfico Donut):** Distribuição percentual das origens de atendimento (Direto, Redes Sociais, E-mail e Orgânico).
* **Histórico de Pedidos Recentes:** Tabela resumida dos últimos lançamentos e atendimentos finalizados.

---

### 3.3. Agenda Inteligente & Calendário Mensal
* **Visão Panorâmica Mensal:** Grade interativa do mês em curso com indicação em tempo real do dia atual ("Hoje").
* **Badges de Compromissos por Data:** Contadores visuais com quantidade de atendimentos/entregas agendadas e visualização do primeiro cliente diretamente no bloco do calendário.
* **Visão Diária Detalhada:** Programação cronológica por horário, cliente, serviço/demanda, duração, valor e status.
* **Ações Rápidas no Atendimento:**
  * **Confirmar:** Marca o compromisso como confirmado.
  * **Concluir:** Finaliza o atendimento e gera automaticamente a entrada de receita no Financeiro.
  * **Cancelar e Excluir:** Gestão ágil de cancelamentos com confirmação de segurança.
* **Navegação Temporal:** Botões de "Anterior", "Hoje" e "Próximo" para consulta retroativa e planejamento futuro.

---

### 3.4. Gestão Financeira & Fluxo de Caixa
* **Quatro Cartões Estratégicos de Saldo:**
  1. *Total Receitas:* Realizado (pago) e a receber (pendente).
  2. *Total Despesas:* Efetuado (pago) e a pagar (pendente).
  3. *Saldo Realizado:* Dinheiro líquido apurado em caixa.
  4. *Saldo Projetado:* Estimativa de fechamento até o fim do mês considerando previsões.
* **Filtros por Abas:** Alternância em 1 clique entre visualização de *Todos*, apenas *Receitas* ou apenas *Despesas*.
* **Busca em Tempo Real:** Campo de busca instantânea por categoria, método de pagamento ou status.
* **Controle de Status com 1 Clique:** Botão para alternar lançamentos entre *Pagar* (baixa em aberto) e *Marcar Pendente*.
* **Lançamentos Detalhados:** Registro de data de vencimento, forma de pagamento (PIX, Cartão, Boleto, Dinheiro) e categorias customizadas.

---

### 3.5. Central Anti-Falta & Lembretes via WhatsApp
* **Foco em Redução de No-Show e Confirmações:** Listagem automática de clientes e demandas agendadas para o dia e dia seguinte.
* **Disparo com 1 Clique:** Abertura direta do WhatsApp (`wa.me`) com mensagem cordial já preenchida contendo nome do cliente, serviço/pedido, data e horário marcado.
* **Confirmação em Lote:** Opção de disparar confirmações pendentes de forma ágil e registrar o status de confirmação.

---

### 3.6. Fila de Atendimento do Dia (Recepção & Triagem)
* **Controle de Fluxo na Recepção:** Organização por ordem de chegada com registro automático de horário.
* **Gestão de Chamada:** Botão para "Chamar" cliente (mudança de status para *Em atendimento*) e botão para "Concluir".
* **Atribuição de Profissional/Atendente:** Indicação de qual colaborador está responsável pela demanda.
* **Monitor no Iniciar:** O bloco na tela inicial exibe quantos clientes estão aguardando e quem está em atendimento no momento.

---

### 3.7. Equipe & Controle Automático de Comissões / Repasses
* **Cadastro de Colaboradores:** Registro de dados de contato, função/especialidade e percentual de comissão acordado (ex: 40%, 45%, 50%).
* **Cálculo Automático de Repasses:** Multiplicação dos serviços e atendimentos concluídos pela taxa de comissão individual, eliminando o fechamento manual de folhas.
* **Métricas do Módulo:** Contagem de profissionais ativos, atendimentos executados no mês, total de comissões acumuladas a repassar e taxa média da equipe.

---

### 3.8. CRM & Carteira de Clientes
* **Cadastro Completo:** Nome, telefone/WhatsApp, e-mail e campo livre de observações e histórico.
* **Anotações Estratégicas:** Armazenamento de restrições, histórico de compras, preferências e particularidades de cada cliente.
* **Busca Instantânea:** Localização ágil por qualquer termo em segundos.

---

### 3.9. Catálogo de Serviços & Produtos
* **Tabela Comercial Padronizada:** Nome comercial do item/serviço, valor em Reais (R$) e especificações.
* **Controle de Duração:** Tempo estimado em minutos (ex: 45 min, 60 min, 75 min), utilizado na alocação da agenda.

---

### 3.10. Fornecedores & Parceiros Comerciais
* **Gestão de Compras e Insumos:** Registro de fornecedores, parceiros comerciais, categorias e distribuidores.
* **Condições Comerciais:** Armazenamento de contato responsável, telefone e prazos de pagamento acordados (ex: Boleto 30d, PIX à vista, Cartão 2x).

---

### 3.11. Demonstrativo de Resultado (DRE) & Exportação
* **Visão Contábil Gerencial:**
  * (+) Receita Operacional Bruta (Realizada)
  * (-) Despesas Operacionais e Insumos
  * (-) Repasses e Comissões da Equipe
  * (=) **Resultado Líquido do Exercício (Lucro Real)**
* **Margem Líquida Percentual:** Cálculo em tempo real da lucratividade líquida sobre o faturamento.
* **Exportação para CSV:** Geração instantânea de arquivo `.csv` para envio à contabilidade ou conciliação em planilhas externas.

---

## 4. Benefícios Estratégicos & Prós de Implementação

| Benefício | Impacto Direto no Negócio |
| :--- | :--- |
| **Adaptabilidade Multi-Nicho** | Flexibilidade para atender comércios, prestadores de serviços, clínicas, agências e consultorias com o mesmo sistema. |
| **Combate Ativo ao No-Show** | Lembretes de WhatsApp com 1 clique reduzem faltas de clientes em até 60%, recuperando receitas que seriam perdidas. |
| **Visão Financeira Clara (Caixa vs. Projeção)** | O gestor sabe exatamente quanto dinheiro tem hoje e quanto sobrará no último dia do mês antes de tomar decisões. |
| **Zero Erros no Cálculo de Comissões** | Cada serviço concluído alimenta automaticamente a comissão do profissional, eliminando atritos e horas perdidas de cálculo manual. |
| **Agilidade na Recepção e Balcão** | A fila em tempo real e a grade mensal permitem atender os clientes sem demora, com organização profissional. |
| **Interface Moderna Sem Complicação** | O conceito Metro de blocos coloridos e botões intuitivos dispensa semanas de treinamento de equipes. |
| **Performance e Acessibilidade** | Carregamento em frações de segundo, sem travamentos de frameworks pesados, com suporte perfeito a modo claro e escuro. |
| **Soberania e Segurança dos Dados** | Sistema independente, sem mensalidades abusivas por usuário adicional, pronto para hospedagem própria ou em nuvem segura. |
