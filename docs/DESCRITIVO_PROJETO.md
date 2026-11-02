# Sistema 0 — Documentação Oficial & Descritivo do Projeto

> **Visão Geral da Solução:**  
> O **Sistema 0** é uma plataforma integrada de gestão empresarial (ERP & CRM) projetada para negócios de serviços — como estéticas, salões de beleza, barbearias, clínicas e consultorias. O sistema une agilidade operacional diária, controle financeiro rigoroso e fidelização de clientes em uma interface visual de alto impacto inspirada no consagrado conceito *Metro/Modern UI*, com suporte nativo a temas Escuro e Claro.

---

## 1. Arquitetura e Engenharia do Sistema

* **Backend:** FastAPI (Python 3.12+), com arquitetura assíncrona de alto desempenho, documentação automática OpenAPI/Swagger e tipagem estrita com Pydantic.
* **Banco de Dados:** SQLAlchemy ORM com suporte nativo a SQLite e PostgreSQL (totalmente compatível com Supabase e instâncias em nuvem).
* **Frontend:** Aplicação em página única (*Single-Page Application*), estilizada com Tailwind CSS, ícones vetoriais Lucide e visualizações de dados interativas com Chart.js.
* **Segurança e Multitenancy:** Autenticação baseada em JWT (*JSON Web Tokens*), senhas criptografadas com bcrypt e isolamento seguro por organização (*tenant*).
* **Design & Acessibilidade:** Interface adaptativa construída com fontes otimizadas para leitura (*FS Me*, *Lexend*, *Atkinson Hyperlegible*), alto contraste e persistência local de preferências.

---

## 2. Módulos e Funcionalidades

### 2.1. Tela Inicial Executiva (*Metro Start Screen*)
* **Blocos Vivos (*Live Tiles*):** Cartões interativos que alternam faces dinamicamente para exibir métricas-chave em tempo real sem exigir cliques (receitas, despesas, equipe em atendimento, próximos clientes, etc.).
* **Acesso Rápido com Cores Semânticas:** Botões em destaque azul, verde-limão e grafite para navegação instantânea às áreas operacionais e financeiras.
* **Alternância de Tema em 1 Clique:** Suporte integrado a **Modo Escuro** (fundo preto `#000000` e cartões `#1A1D24`) e **Modo Claro** (fundo `#F8FAFC` e cartões brancos `#FFFFFF` em alto contraste).
* **Central de Notificações e Avisos (Sino):** Dropdown flutuante que consolida alertas automáticos de contas a vencer, atendimentos pendentes e avisos prioritários.

---

### 2.2. Dashboard Analítico & Projeções
* **Linha de KPIs Executivos com Sparklines:** Monitoramento de Faturamento Total, Quantidade de Pedidos/Serviços, Ticket Médio e Novos Clientes com indicadores visuais de variação percentual.
* **Faturamento Mensal (Gráfico Spline):** Curvas dinâmicas de Receitas versus Despesas com gradientes visuais.
* **Simulador e Projeção Mês a Mês:** Barra de navegação rápida pelos 12 meses do ano que recalcula dinamicamente a receita prevista, despesa estimada, saldo projetado e percentual da meta atingida.
* **Vendas por Canal (Gráfico Donut):** Distribuição percentual das origens de atendimento (Direto, Redes Sociais, E-mail e Orgânico).
* **Histórico de Pedidos Recentes:** Tabela resumida dos últimos lançamentos e atendimentos finalizados.

---

### 2.3. Agenda Inteligente & Calendário Mensal
* **Visão Panorâmica Mensal:** Grade interativa do mês em curso com indicação em tempo real do dia atual ("Hoje").
* **Badges de Atendimentos por Dia:** Contadores visuais com quantidade de serviços agendados e visualização do primeiro cliente do dia diretamente no bloco do calendário.
* **Visão Diária Detalhada:** Ao clicar em qualquer dia do mês, a tela abre a programação cronológica da data (horário, cliente, serviço, duração, valor e status).
* **Ações Rápidas no Atendimento:**
  * **Confirmar:** Marca o atendimento como confirmado.
  * **Concluir:** Finaliza o atendimento e gera automaticamente a entrada de receita no Financeiro.
  * **Cancelar e Excluir:** Gestão ágil de cancelamentos com confirmação de segurança.
* **Navegação Temporal:** Botões de "Anterior", "Hoje" e "Próximo" para consulta retroativa e planejamento futuro.

---

### 2.4. Gestão Financeira & Fluxo de Caixa
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

### 2.5. Central Anti-Falta via WhatsApp
* **Foco em Redução de No-Show:** Listagem automática de clientes agendados para o dia e dia seguinte.
* **Disparo com 1 Clique:** Abertura direta do WhatsApp (`wa.me`) com mensagem cordial já preenchida contendo nome do cliente, serviço, data e horário marcado.
* **Confirmação em Lote:** Opção de disparar confirmações pendentes de forma ágil e marcar o status de confirmação.

---

### 2.6. Fila de Atendimento do Dia (Recepção)
* **Controle de Fluxo na Recepção:** Organização por ordem de chegada com registro automático de horário.
* **Gestão de Chamada:** Botão para "Chamar" cliente (mudança de status para *Em atendimento*) e botão para "Concluir".
* **Atribuição de Profissional:** Indicação de qual colaborador está responsável pelo atendimento.
* **Monitor no Iniciar:** O bloco na tela inicial exibe quantos clientes estão aguardando e quem está em atendimento no momento.

---

### 2.7. Equipe & Controle Automático de Comissões
* **Cadastro de Colaboradores:** Registro de dados de contato, função/especialidade e percentual de comissão acordado (ex: 40%, 45%, 50%).
* **Cálculo Automático de Repasses:** Multiplicação dos atendimentos concluídos pela taxa de comissão individual, eliminando o fechamento manual de folhas.
* **Métricas do Módulo:** Contagem de profissionais ativos, atendimentos executados no mês, total de comissões acumuladas a repassar e comissão média da equipe.

---

### 2.8. CRM & Carteira de Clientes
* **Cadastro Completo:** Nome, telefone/WhatsApp, e-mail e campo livre de observações e histórico.
* **Anotações Estratégicas:** Armazenamento de restrições (ex: alergias a produtos, preferências de horários e particularidades).
* **Busca Instantânea:** Localização ágil por qualquer termo em segundos.

---

### 2.9. Catálogo de Serviços
* **Tabela de Preços Padronizada:** Nome comercial do procedimento, valor em Reais (R$) e descrição do serviço.
* **Controle de Duração:** Tempo estimado em minutos (ex: 45 min, 60 min, 75 min), utilizado na alocação de horários da agenda.

---

### 2.10. Fornecedores & Parceiros Comerciais
* **Gestão de Insumos:** Registro de distribuidores de cosméticos, descartáveis, equipamentos e material gráfico.
* **Condições Comerciais:** Armazenamento de contato responsável, telefone e prazos de pagamento acordados (ex: Boleto 30d, PIX à vista, Cartão 2x).

---

### 2.11. Demonstrativo de Resultado (DRE) & Exportação
* **Visão Contábil Gerencial:**
  * (+) Receita Operacional Bruta (Realizada)
  * (-) Despesas Operacionais e Insumos
  * (-) Repasses e Comissões da Equipe
  * (=) **Resultado Líquido do Exercício (Lucro Real)**
* **Margem Líquida Percentual:** Cálculo em tempo real da lucratividade líquida sobre o faturamento.
* **Exportação para CSV:** Geração instantânea de arquivo `.csv` para envio à contabilidade ou conciliação em planilhas externas.

---

## 3. Benefícios Estratégicos & Prós de Implementação

| Benefício | Impacto Direto no Negócio |
| :--- | :--- |
| **Combate Ativo ao No-Show** | Lembretes de WhatsApp com 1 clique reduzem faltas de clientes em até 60%, recuperando receitas que seriam perdidas. |
| **Visão Financeira Clara (Caixa vs. Projeção)** | O gestor sabe exatamente quanto dinheiro tem hoje e quanto sobrará no último dia do mês antes de tomar decisões de compras. |
| **Zero Erros no Cálculo de Comissões** | Cada serviço concluído alimenta automaticamente a comissão do profissional, eliminando atritos e horas perdidas de cálculo manual. |
| **Agilidade na Recepção e Atendimento** | A fila em tempo real e a grade mensal permitem atender os clientes sem demora, com organização profissional. |
| **Interface Moderna Sem Complicação** | O conceito Metro de blocos coloridos e botões intuitivos dispensa semanas de treinamento de recepcionistas ou novos colaboradores. |
| **Performance e Acessibilidade** | Carregamento em frações de segundo, sem travamentos de frameworks pesados, com suporte perfeito a modo claro e escuro. |
| **Soberania e Segurança dos Dados** | Sistema independente, sem mensalidades abusivas por usuário adicional, pronto para hospedagem própria ou em nuvem segura. |

