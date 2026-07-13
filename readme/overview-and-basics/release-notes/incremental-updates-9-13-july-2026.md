# Notas de versão DocBits — 9–13 de julho de 2026

_Um resumo do que muda para si com esta versão do DocBits. Cada serviço abaixo
mostra a versão agora em produção, seguida das novidades ou correções explicadas
em linguagem simples — sem números de ticket nem jargão técnico. Os serviços não
listados não tiveram alterações visíveis para o cliente nesta janela._

---

## Destaques

- **Início de sessão multiorganização.** Os utilizadores que pertencem a várias
  organizações passam a ter um verdadeiro seletor de organização no início de
  sessão, um comutador de organização no cabeçalho e uma definição de
  organização predefinida. As sessões ficam associadas de forma segura a uma
  organização de cada vez, e a aplicação acompanha automaticamente a região da
  organização ativa. Iniciar sessão na região errada passa a repetir
  automaticamente na região correta em vez de falhar.
- **Canais de lançamento (frozen / latest).** As organizações podem agora ser
  fixadas numa versão estável ("frozen") enquanto outras recebem as
  atualizações mais recentes — permitindo lançamentos controlados. A janela de
  Versões dos Serviços mostra uma nova coluna *Release*, e os administradores
  gerem o canal a partir das Informações da Empresa. Vários serviços
  apresentam saltos de versão maiores nesta janela apenas devido à nova
  numeração de versões por canal — esses saltos não trazem qualquer alteração
  funcional.
- **Motores de regras configuráveis.** Chegam três novos sistemas de regras à
  API (todos desativados por predefinição, ativáveis por organização):
  **regras de validação** que verificam os valores extraídos e assinalam as
  falhas diretamente no documento, **regras de transformação** que limpam ou
  reescrevem automaticamente os valores extraídos de campos e tabelas, e
  **seleção de layout baseada em regras** que escolhe o layout de documento
  certo através de regras, em vez de depender da origem do documento.
- **Transparência na importação de e-mails.** O registo de importação de
  e-mails mostra agora uma linha expansível por anexo, indica que documentos
  foram criados (com botões que levam diretamente a eles no dashboard),
  assinala itens ignorados e divididos, e permite descarregar o e-mail
  original como ficheiro `.eml`.
- **Extração de tabelas com IA.** Um novo modo de extração estruturada por IA
  para tabelas, com uma caixa de seleção "Use AI" por tabela e por coluna nas
  definições do Tipo de Documento.
- **Estabilidade da Web App.** Corrigido um ciclo infinito de recarregamentos
  após uma sessão expirada, corrigido o Layout Builder que estava avariado, e
  as tabelas de extração passam a ter um redimensionador de altura
  arrastável.
- **Novo: Auth Bridge Service.** Um novo serviço mantém os dados de início de
  sessão continuamente sincronizados entre as regiões da UE e dos EUA, com
  autorreparação e monitorização integradas.

---

## API Service — em produção: `12.57.8`

- **Regras de validação (novo, por organização):** um motor de regras
  configurável pelo administrador verifica os valores extraídos (totais,
  campos obrigatórios e mais) e marca as falhas diretamente no documento,
  incluindo qual a regra que foi acionada. As regras podem ser testadas em
  modo de simulação antes de serem ativadas, podem ser ligadas por tipo de
  documento e incluem um catálogo inicial de regras predefinidas (todas
  desativadas até optar por ativá-las).
- **Regras de transformação (novo, por organização):** limpam ou reescrevem
  automaticamente os valores extraídos de campos e tabelas durante o
  processamento — configuráveis por tipo de documento ou para toda a
  organização.
- **Seleção de layout baseada em regras (novo):** os layouts de documento
  podem agora ser escolhidos por regras configuráveis, em vez de estarem
  ligados à origem do documento. O comportamento existente baseado na origem
  é migrado automaticamente, os modelos de layout podem ser renomeados e os
  títulos de layout duplicados são impedidos.
- **Exportações do dashboard mais rápidas:** as exportações acionadas a partir
  do dashboard são agora enviadas para um worker dedicado em vez de esperarem
  por um ciclo de polling, pelo que arrancam prontamente.
- **Corrigido o bloco de exportação da Deteção de Duplicados:** o bloco de
  exportação para duplicados suspeitos volta a funcionar.
- **Definições que não eram guardadas:** corrigidas preferências guardadas que
  ocasionalmente não persistiam quando existia uma cópia antiga eliminada da
  mesma definição.
- **Documentos com carateres invulgares:** corrigidos erros ao guardar
  causados por carateres NUL invisíveis nos dados extraídos.
- **"Atualizado por" correto:** os documentos carregados automaticamente como
  documentos eletrónicos deixam de mostrar um utilizador de sistema como
  último editor — o campo permanece vazio até que uma pessoa edite de facto.
- **PDFs digitalizados com uma boa camada de texto:** uma nova opção permite
  ao DocBits confiar no texto já incorporado numa página digitalizada em vez
  de voltar a executar o OCR — mais rápido e, muitas vezes, mais preciso.
- **Faturas eletrónicas:** deteção mais robusta de XML incorporado quando o
  ficheiro original precisa de ser verificado novamente.
- **Tarefas:** novo interruptor de organização que permite aos
  não administradores usar o filtro "Todos" na lista de tarefas.
- **Correspondência de linhas de item:** o comportamento de correspondência
  aproximada (fuzzy) é agora configurável por linha.
- **Estabilidade:** as ligações WebSocket fecham de forma limpa em caso de
  erro em vez de lançarem exceções no servidor; a sincronização da cache de
  permissões verifica-se e repara-se a si própria; a versão do serviço passa a
  estar visível no endpoint de estado (health).

## Auth Service — em produção: `1.71.1`

- **Início de sessão multiorganização:** o início de sessão pergunta agora em
  que organização entrar quando um utilizador pertence a várias, as sessões
  ficam associadas a essa organização, e novos endpoints suportam selecionar,
  mudar e definir uma organização predefinida. As adesões a organizações
  duplicadas ou em conflito foram limpas e passam a ser impedidas ao nível da
  base de dados, com consultas de adesão mais rápidas.
- **Correções da organização predefinida:** o início de sessão seleciona
  automaticamente a sua organização predefinida (e não uma arbitrária), e a
  alteração da predefinição tem efeito imediato em vez de mostrar dados de
  perfil desatualizados.
- **Fim de sessão corrigido:** resolvido um erro de servidor (HTTP 500) ao
  terminar sessão e reposto o endpoint de revogação de tokens.
- **Segurança dos tokens:** a verificação e a cache de tokens respeitam agora
  a organização para a qual o token foi emitido, e a revogação de tokens está
  centralizada.
- **Canais de lançamento:** o canal de lançamento da organização é armazenado
  aqui, gerível pelos administradores da organização e exposto à aplicação e à
  camada de encaminhamento.

## Auth Bridge Service — em produção: `0.2.4.2` _(novo serviço)_

- **O que é:** um novo serviço que replica continuamente os dados de
  autenticação entre as regiões da UE e dos EUA, para que as contas e os
  inícios de sessão se mantenham consistentes entre regiões.
- **Autorreparação:** deteta e repara desvios de dados entre regiões —
  incluindo garantir que as eliminações são propagadas — e recupera
  automaticamente de perdas de ligação em vez de perder dados.
- **Segurança e monitorização:** um anterior ciclo de replicação bidirecional
  foi interrompido e é agora ativamente detetado e bloqueado; o registo de
  erros e os alertas estão integrados; e o serviço comunica a sua versão na
  janela de Versões dos Serviços.

## Docflow Service — em produção: `2.6.1`

- **Cartões de workflow aceitam valores vazios:** os cartões de caixa de
  seleção e de parceiro deixam de falhar quando um campo está legitimamente
  vazio; as verificações de tipo de cartão são mais rigorosas e previsíveis.
- **Workflows voltam a executar-se em alterações reais:** o lock de workflow
  volta a respeitar o estado do documento proveniente do acionador e passa
  também a acompanhar a versão do documento — assim, um documento cujos dados
  mudaram genuinamente pode voltar a passar pelo workflow mesmo com o mesmo
  estado, enquanto os verdadeiros duplicados continuam bloqueados.
- **Workflows avançados maiores:** o limite de nós de workflow foi aumentado e
  é agora configurável por ambiente.
- **Exportação alternativa:** as exportações alternativas acionadas por
  workflow passam a ser identificadas como tal, para que os sistemas a jusante
  as consigam distinguir.
- **Resiliência:** o serviço volta a ligar-se automaticamente quando uma
  ligação à base de dados cai a meio da utilização, tolera um message broker
  mais lento em vez de falhar, e os pedidos de API falhados são agora
  registados com contexto completo e IDs de execução rastreáveis.

## Email Service — em produção: `1.38.4`

- **Registo de importação reconstruído para rastreabilidade:** cada e-mail
  importado regista agora que documentos foram criados a partir dele, com
  linhas de detalhe por anexo.
- **Descarregar o e-mail original:** a mensagem original pode ser descarregada
  como ficheiro `.eml` diretamente a partir do registo de importação.
- **Recuperação de anexos:** o mecanismo de recuperação de corrupção passa a
  tratar também mensagens de texto simples, pelo que mais e-mails recebidos
  danificados são recuperados em vez de ignorados.

## Extraction Service — em produção: `1.51.6`

- **Imposto/líquido já não são trocados:** corrigido um caso em documentos dos
  EUA em que o valor do imposto podia ser atribuído como superior ao valor
  líquido quando eram encontrados vários pares candidatos.
- **Várias taxas de imposto por fornecedor:** a extração passa a lidar com
  fornecedores cujas faturas apresentam taxas de imposto diferentes no mesmo
  documento.
- **Extração de tabelas com IA (novo, opcional):** endpoints de extração
  estruturada por IA para tabelas, ativados por organização através de uma
  feature flag.
- **Chamadas de IA mais rápidas:** afinada a configuração do modelo de IA
  usado durante a extração para evitar tempo de processamento desnecessário.
- **Correção de falha:** resolvido um erro em documentos que produziam uma
  lista de candidatos vazia durante a extração.

## Fulltext Service — em produção: `1.37.2`

- **Migrações do índice de pesquisa reparadas:** repostas definições de
  migração que tinham divergido, mantendo fiáveis as atualizações do índice de
  pesquisa.
- Trabalho interno de encaminhamento para a nova infraestrutura de canais de
  lançamento.

## PO Match Service — em produção: `1.58.2`

- **Correspondência mais tolerante:** a correspondência de Ordens de Compra
  deixa de falhar com dados invulgares — números de item não textuais,
  quantidades em falta e valores de montante não textuais são agora tratados
  de forma robusta em vez de gerarem erros.

## Web App — em produção: `10.41.8`

- **Experiência multiorganização:** nova página de seleção de organização no
  início de sessão, um ícone dedicado de mudança de organização no cabeçalho,
  definições de organização predefinida, e a aplicação acompanha a região da
  sua organização ativa. Iniciar sessão na região errada repete
  silenciosamente na região correta e encaminha-o para o seletor de
  organização quando necessário.
- **Fim dos recarregamentos infinitos:** corrigido um ciclo infinito de
  recarregamentos que podia ocorrer quando o servidor rejeitava um token de
  sessão armazenado — a aplicação força agora uma verdadeira renovação do
  token em vez de recarregar indefinidamente.
- **Layout Builder corrigido:** o Layout Builder volta a funcionar, e a
  seleção de layout está desacoplada da origem do documento (em linha com a
  nova seleção baseada em regras na API).
- **Tabelas de extração:** as tabelas de linhas de item têm agora uma pega de
  redimensionamento arrastável, para poder dar mais espaço à tabela durante a
  validação.
- **Registo de importação de e-mails:** novo estado de ignorado e emblemas de
  divisão, linhas expansíveis por anexo, descarregamento do e-mail original e
  botões de ID de documento que levam diretamente ao dashboard filtrado para
  esse documento.
- **Pesquisa no dashboard:** a lista pendente de valores de consulta mostra
  agora a etiqueta localizada para campos de lista de valores, e os exemplos
  de ajuda da pesquisa foram reformulados.
- **Fiabilidade das definições:** as preferências do utilizador carregam agora
  de forma fiável ao iniciar sessão via SSO, e a confirmação de gravação só é
  mostrada quando a gravação foi de facto bem-sucedida.
- **Tarefas:** o filtro "Todos" pode ser reposto para não administradores
  através de um novo interruptor de organização.
- **Registos do Watchdog:** deixam de estar limitados a 10 000 entradas, além
  de melhorias gerais de usabilidade.
- **Pedidos de suporte:** o formulário de suporte preenche previamente o seu
  endereço de e-mail a partir do seu perfil.
- **Definições do Tipo de Documento:** nova caixa de seleção "Use AI" em
  tabelas e colunas para controlar a extração de tabelas assistida por IA.
- **Janela de Versões dos Serviços:** nova coluna *Release* que mostra o canal
  de cada serviço (frozen/latest), encaminhada de forma a manter-se rápida
  para organizações fixadas.
- **Field Validation:** corrigido um erro ao regressar ao Field Validation a
  partir de outro ecrã, e o botão "Scripts" deixa de encaminhar para uma
  página 404.

---

## Apenas renumeração de versões (sem alterações funcionais)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) e **Ideas Service** (`0.3.1`) foram renumerados no âmbito da nova
infraestrutura de canais de lançamento. Os seus saltos de versão aparentemente
maiores não trazem alterações de funcionalidades nem de comportamento nesta
janela. O **Docnet Service** (`1.54.6`) está inalterado desde 19 de junho.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..13)
     version-bump commits supplied by the user, per service). -->
