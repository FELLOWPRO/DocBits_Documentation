# Notas de versão DocBits — 26–30 de junho de 2026

_O que esta atualização de produção trouxe, em linguagem simples. Cada serviço
mostra a versão agora em produção. Os serviços não listados não tiveram alterações
visíveis para o cliente nesta janela._

---

## Destaques

- **Uma única ligação para assistentes de IA ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Um gateway único e
  unificado serve agora todas as ferramentas do DocBits — incluindo o DocFlow —
  através da API principal, para que os assistentes de IA (Claude, Gemini CLI,
  Codex) se liguem através de um único endpoint fiável em vez de vários.
- **Pesquisa multilingue mais inteligente no dashboard.** Os conectores de pesquisa
  (**AND / OR**) aparecem agora no seu idioma com realce a cores, os subtipos de
  fatura oferecem um menu suspenso de valores, e as mensagens de sintaxe de pesquisa
  estão localizadas — com um manuseamento do teclado mais fluido em toda a parte.
- **Aprovações e permissões mais fluidas.** A aprovação já não é acionada quando a
  unidade de embalagem de uma confirmação de encomenda está vazia, os utilizadores
  normais podem voltar a aprovar elementos de custo após a migração do controlo de
  acesso, e as permissões ao nível do documento aplicam-se corretamente mesmo quando
  uma coluna de tabela já existe.
- **A aplicação atualiza-se sozinha.** Quando é lançada uma nova versão, o DocBits
  atualiza-se agora automaticamente em vez de o interromper com um popup "Refresh
  Now".
- **Correspondência de ordens de compra mais robusta.** As transformações de valores
  de colunas, as proteções contra falhas para linhas sem preço ou quantidade e a
  repetição automática em ligações de base de dados interrompidas tornam a
  correspondência mais estável.
- **Menos erros em toda a linha.** Muitos erros raros de servidor em dashboards,
  faturas de fornecedor, registos de PO e tarefas de OCR foram identificados e
  corrigidos.

---

## Web App — em produção: `10.34.4`

- **Pesquisa rápida no dashboard:** conectores **AND / OR** localizados (de/fr) com
  realce de sintaxe a cores; menu suspenso de valores para subtipos de fatura;
  mensagens de erro de sintaxe de pesquisa localizadas; experiência de teclado mais
  fluida; o aviso "full-text required" é agora apresentado em linha para que o
  layout já não salte.
- **Aprovações e permissões:** corrigida a aprovação acionada erradamente quando a
  unidade de embalagem de uma confirmação de encomenda está vazia; os utilizadores
  normais podem voltar a aprovar elementos de custo após a migração do controlo de
  acesso; as permissões ao nível do documento aplicam-se agora quando uma coluna de
  tabela já existe.
- **Atualização automática:** a aplicação atualiza-se automaticamente numa nova
  versão em vez de mostrar um popup "Refresh Now"; removido o antigo diálogo de
  informação de versão.
- **Definições de e-mail de entrada:** nova opção e campo de destinatários das
  notificações de falha; o registo de importação mostra agora a atividade de saída e
  o motivo da falha; o endereço de entrada é copiado de forma fiável.
- **Divisão de documentos:** o ecrã Document Split permite agora deslocamento
  (scroll).
- **Modo escuro:** correções para a extração de tabelas, o contador de tarefas e os
  marcadores de documentos fechados no dashboard.
- **Usabilidade e estabilidade:** correções na UI de exportação do dashboard; os
  cabeçalhos de tabela fixos já não transparecem através dos diálogos; o dashboard
  DocNet já não falha num pedido de estatísticas com erro; os scripts de campo já
  não revertem campos esvaziados para os seus valores antigos; correções nas caixas
  de verificação e no layout das definições de PO; correções na apresentação da
  classify-list.
- **Fornecedores:** as organizações de fornecedores podem agora registar-se através
  de magic link.

## API Service — em produção: `12.46.8`

- **Gateway DocBits MCP:** um gateway unificado faz agora proxy das ferramentas do
  DocFlow através da API principal, para que os assistentes de IA alcancem todas as
  ferramentas do DocBits através de um único endpoint; o endpoint MCP é servido sem
  um redirecionamento que poderia quebrar as ligações.
- **Contabilidade:** adicionada validação de centro de custo para o ID de
  contabilidade.
- **Encaminhamento de OCR:** os documentos são enviados para um re-OCR completo
  quando o e-text do fornecedor está desativado, para que o texto se mantenha
  fiável.
- **Infor ERP / SAP:** os encargos adicionais são encaminhados corretamente quando o
  ERP já detém o encargo com um montante zero.
- **Fiabilidade (menos erros de servidor):** reforçadas as consultas de dashboard,
  fatura de fornecedor, registo de PO e gestor de tarefas para que já não devolvam
  erros 500 raros; sincronização de cache de organização e limpeza de ficheiros
  armazenados mais resilientes.
- **Filtros de dashboard mais limpos:** removido o campo de filtro de número de
  fatura redundante; corrigida a quantidade correspondida por PO.
- **Documentação da API para programadores:** a interface Swagger oferece agora um
  menu suspenso de especificações (OpenAPI 3.0 mais a vista Infor Swagger 2.0) com a
  marca DocBits.

## Auth Service — em produção: `1.68.0`

- **Fim de sessão / revogação de token mais rápidos:** a revogação de tokens em
  massa já não demora minutos nem interrompe a ligação.
- **Corrigidos os e-mails de definição de palavra-passe** para que sejam
  apresentados corretamente.
- **Fornecedores:** as organizações de fornecedores podem registar-se com um magic
  link.
- **Estabilidade do início de sessão:** um membro já não fica bloqueado numa falha
  transitória de pesquisa de organização, e um id de organização inválido devolve
  agora uma mensagem limpa em vez de um erro.

## Docflow Service — em produção: `2.4.1`

- **Gateway de IA fiável:** corrigidos bloqueios e timeouts no endpoint MCP do
  DocFlow (handshake, desconexões de cliente, respostas duplicadas) — o lado
  DocFlow do gateway DocBits MCP unificado.

## OCR Service — em produção: `1.7.1`

- **Processamento de OCR mais estável:** as filas de resposta em segundo plano
  expiram automaticamente e as falhas de ligação transitórias são repetidas, para
  que menos tarefas de OCR fiquem presas.

## PO Match Service — em produção: `1.55.7`

- **As transformações de valores** são agora aplicadas nas colunas de item-id,
  unit-code e static-value durante a correspondência por regras.
- **Proteções contra falhas:** uma linha sem preço ou quantidade, uma combinação
  incomum de chave ponderada, ou uma divisão impossível já não fazem a
  correspondência falhar.
- **Fiabilidade:** as escritas na base de dados são repetidas automaticamente em
  ligações interrompidas ou fechadas por SSL.
- **Infor ERP / SAP:** os encargos adicionais são encaminhados corretamente quando o
  ERP detém o encargo com um montante zero.

## Fulltext Service — em produção: `1.35.6`

- **Reindexação mais rápida:** todas as fases de sincronização se distribuem agora
  em paralelo para que o autoscaling entre em ação, corrigindo a lenta reindexação
  em série e um widget de progresso preso em 0%.
- **Estatísticas mais estáveis:** os pedidos de estatísticas de documentos
  entre regiões são limitados para que já não sofram timeout.

---

## Sem alterações visíveis para o cliente nesta janela

Estáveis, sem alterações de produto notáveis entre 26–30 de junho: Auto Accounting
(`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction
(`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting e FTP receberam
apenas manutenção interna.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
