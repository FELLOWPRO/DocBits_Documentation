# Notas de versão DocBits — 14–29 de julho de 2026

_O que mudou na atualização de produção do DocBits a 29 de julho de 2026 (a
atualização do canal Nova), cobrindo tudo desde a versão de 14 de julho. Cada
serviço indica a versão agora em produção e, de seguida, as novidades ou
correções em linguagem simples. Os serviços não listados não tiveram alterações
visíveis para o cliente._

---

## Destaques

- **Autenticação de dois fatores.** As contas DocBits podem agora ser
  protegidas com um segundo fator: uma aplicação de autenticação (TOTP), um
  código único por e-mail ou uma chave de acesso através de Touch ID, Windows
  Hello, YubiKey e semelhantes. Os códigos de backup cobrem o caso de perda do
  dispositivo, e um dispositivo fiável pode dispensar o segundo fator durante
  algum tempo. Todos os utilizadores podem ativá-la para si próprios; os
  administradores podem torná-la obrigatória para toda a organização. Consulte
  o [guia de Autenticação de Dois Fatores](../two-factor-authentication.md).
- **Tickets de suporte a partir do ecrã de erro.** Quando algo corre mal, pode
  agora abrir um ticket de suporte diretamente a partir do registo de erro. O
  ticket já inclui o contexto técnico, por isso não precisa de o descrever.
- **E-mail de entrada na região correta.** As organizações dos EUA passam a
  ter endereços de importação na sua própria região, e as caixas de correio
  Microsoft 365 em tenants de nuvens nacionais (GCC, 21Vianet e semelhantes)
  podem agora ser configuradas com uma seleção de Cloud Instance.
- **Estado de correspondência de PO mais claro.** As faturas cuja tabela de
  linhas não pôde ser mapeada eram rotuladas como "ordem de compra não
  encontrada", o que levava as pessoas a procurar o problema errado. Passam a
  ter o seu próprio estado "tabela incompleta", com detalhe ao nível da coluna
  sobre o que não foi mapeado.
- **Mapeamento de códigos de imposto para documentos eletrónicos.** Uma nova
  página de definições mapeia os códigos de imposto do seu ERP para documentos
  eletrónicos, e as exportações verificam o mapeamento à partida, em vez de
  falharem no ERP.
- **Nível de IA Turbo descontinuado.** O modelo Turbo chegou ao fim de vida.
  Quem o tinha selecionado foi movido automaticamente para o Fast; não é
  necessária qualquer ação.

---

## Web App — em produção: `10.46.2`

### Início de sessão

- **Autenticação de dois fatores:** configure uma aplicação de autenticação,
  códigos por e-mail ou uma chave de acesso no seu perfil, imprima os códigos
  de backup e marque um dispositivo como fiável para que a verificação não lhe
  seja pedida de todas as vezes. Os utilizadores com chave de acesso podem
  iniciar sessão sem qualquer palavra-passe. Os administradores da organização
  dispõem de um interruptor para tornar a 2FA obrigatória e de uma vista de
  adesão que mostra quem já a ativou.
- **Contas eliminadas:** iniciar sessão com uma conta eliminada passa a
  indicá-lo, em vez de falhar com um erro genérico.
- **SSO:** corrigido um erro ao iniciar sessão com uma região diferente
  selecionada. As sessões SSO expiram agora quando o fornecedor de identidade
  o determina, e não ao fim de um temporizador local fixo.

### Trabalhar com documentos

- **Documentos eliminados:** abrir um documento entretanto eliminado mostra
  uma mensagem adequada em vez de erros de script.
- **Field Validation:** o campo do número de página é mais largo e salta para
  a página ao premir Enter. Um campo tornado só de leitura por um script
  continua a mostrar a sua ligação de campo. Um aviso que apresentava
  JavaScript em bruto passa a mostrar a mensagem real, e o ecrã já não bloqueia
  em documentos com tabelas de linhas de documentos eletrónicos extensas.
- **Extração de tabelas:** eliminar uma coluna liberta o respetivo nome para
  reutilização, e os cabeçalhos eliminados já não reaparecem na tabela
  guardada.
- **Aprovações:** abrir um documento que acabou de ficar pendente leva ao ecrã
  de aprovação correto. Os utilizadores já não conseguem aprovar um passo de
  Sales Tax para o qual o seu grupo não tem permissão, e o histórico de
  aprovações volta a mostrar todas as entradas. O histórico indica também a
  pessoa que realmente aprovou, incluindo as aprovações feitas por um
  administrador em nome do responsável atribuído.
- **Fornecedores:** a página Accounting já não mostra um falso aviso de
  "fornecedor em falta", e eliminar um fornecedor que só existe a partir da
  extração já não deixa a janela bloqueada.
- **Dados mestre:** as tabelas na página de dados mestre voltam a ter scroll.
- **Tarefas e notificações:** eliminar uma tarefa deixou de estar reservado
  aos administradores. A possibilidade de os utilizadores sem direitos de
  administrador eliminarem as suas próprias tarefas passa a ser uma definição
  da organização, e os utilizadores com uma tarefa num documento que não
  conseguem abrir obtêm uma vista apenas da tarefa, em vez de um erro.

### Dashboard e pesquisa

- **Exportação:** as exportações usam o dashboard que tem selecionado, e a
  aplicação avisa antes de exportar um dashboard com alterações por guardar.
- **Pesquisa:** Invoice Type está disponível como campo de pesquisa, com a
  respetiva lista de valores. Quando um conjunto de resultados é maior do que
  a janela que o dashboard consegue mostrar, o contador passa a indicá-lo, em
  vez de truncar a lista silenciosamente.
- **Registo de importação:** os documentos divididos podem ser encontrados
  através do documento principal, e a coluna Failed Filenames lista apenas os
  ficheiros que realmente falharam ou foram ignorados.

### Definições e administração

- **Tickets de suporte:** crie um ticket diretamente a partir de um registo de
  erro. Os tickets incluem o ambiente e o canal de lançamento, e a captura de
  ecrã já não fica bloqueada.
- **Grupos e permissões:** os documentos não classificados podem ser
  concedidos como permissão, tal como qualquer outro tipo de documento.
- **Workflow Builder:** cartões recém-criados ou renomeados, modelos de
  e-mail e outros itens de listas pendentes aparecem imediatamente, sem
  recarregar a página.
- **Árvores de Decisão:** as etiquetas dos campos de documento no editor
  seguem o idioma da interface, em vez de mostrarem sempre o nome em inglês.
- **Tipos de Documento:** nova definição Structured Extraction na secção de
  extração.
- **Códigos de imposto E-Doc:** nova página de definições para mapear os
  códigos de imposto do seu ERP para documentos eletrónicos (ver Destaques).
- **Auto Accounting:** as dimensões aparecem de forma fiável, em vez de
  intermitente.
- **Seleção de modelo de IA:** o nível Turbo descontinuado desapareceu da
  lista; as seleções existentes mostram Fast.
- **Janela Versões dos Serviços:** passou a ter scroll, inclui o Auth Bridge
  Service e mostra os nomes dos canais de lançamento Vesta e Nova.
- **Página de importação:** já não falha em organizações com uma entrada de
  subscrição vazia.

### Correções menores

As notificações vazias são suprimidas, a janela de criar/editar ideia tem
scroll, as caixas de seleção desalinhadas nas definições de campos voltaram a
estar alinhadas, as eliminações de documentos bloqueadas explicam porquê, e as
definições de E-Document lidam corretamente com a mudança de Default para
Custom.

## API Service — em produção: `12.68.1`

- **Autenticação de dois fatores:** todos os caminhos de início de sessão
  baseados em palavra-passe passam pela verificação do segundo fator, pelo que
  nenhuma rota de integração a contorna.
- **Códigos de imposto E-Doc:** mapeamento dos códigos de imposto do ERP para
  documentos eletrónicos, com uma verificação central antes da exportação,
  para que os códigos em falta sejam detetados cedo.
- **Controlo de acessos:** os administradores podem conceder a utilizadores
  sem direitos de administrador visibilidade sobre documentos não
  classificados.
- **Registo de auditoria de eliminações:** os documentos registam quem os
  eliminou e quando.
- **Dashboards pessoais:** corrigidas as definições de partilha que não eram
  guardadas.
- **Pesquisa no dashboard:** Invoice Type junta-se aos campos de pesquisa
  alargada, e os documentos criados por uma divisão por código de barras ou
  QR são encontrados através do documento principal.
- **Atualidade do dashboard:** atualizar uma tabela ou reprocessar um
  documento limpa a cache do dashboard, pelo que a lista deixa de mostrar os
  valores anteriores à alteração.
- **Carregamentos:** carregamentos repetidos do mesmo ficheiro durante uma
  nova tentativa de rede já não criam documentos duplicados.
- **Consulta de fornecedores:** os resultados chegam assim que os dados estão
  prontos, em vez de após uma espera fixa.
- **Exportação Infor:** os preços unitários mantêm quatro casas decimais. As
  exportações M3 podem incluir encargos de linha com valor zero, e as linhas
  de custo LN negativas são enviadas como créditos positivos. A exportação
  aguarda também que um fluxo de trabalho pendente termine, em vez de decorrer
  a meio do fluxo.
- **Aprovações:** uma aprovação só é associada a um pedido de aprovação
  quando o aprovador é o responsável atribuído a esse pedido. As alterações
  que um fluxo de trabalho faz por sua própria iniciativa são atribuídas ao
  utilizador Sistema e não à última pessoa que mexeu no documento.
- **Estabilidade do início de sessão:** uma falha temporária na validação de
  tokens já não termina a sessão dos utilizadores; a aplicação tenta
  novamente. Os documentos recebem o mesmo tratamento e já não falham de
  imediato perante uma breve intermitência da autenticação.
- **Classificação:** as regras de origem comparam agora com todos os campos
  de origem do documento, e não com posições fixas.
- **Estabilidade da validação:** um campo sem nome já não faz falhar a
  validação de documentos.
- **Modelos de IA:** o nível Turbo (descontinuado) é remapeado para Fast em
  todo o lado, incluindo as variantes afinadas, com uma salvaguarda para que
  um modelo descontinuado nunca possa ser executado.
- **Tarefas em segundo plano:** um agendador bloqueado é detetado e
  reiniciado, para que as tarefas recorrentes não possam parar
  silenciosamente.

## Auth Service — em produção: `1.75.3`

- **Autenticação de dois fatores:** o backend por trás da entrada nos
  Destaques. Aplicações de autenticação, códigos únicos por e-mail, chaves de
  acesso e dispositivos fiáveis, além de códigos de backup, imposição ao nível
  da organização e início de sessão sem palavra-passe com chave de acesso.
  Ativar a 2FA termina as suas restantes sessões, alterar a palavra-passe
  revoga os dispositivos fiáveis, e os endpoints de verificação têm limite de
  tentativas, bloqueio e uma proteção contra a reutilização de códigos.
- **Histórico de inícios de sessão:** os inícios de sessão via SSO/SAML
  passam a aparecer no histórico, e a data e hora do último início de sessão
  é registada de forma fiável para todos os tipos de início de sessão.
  Consultar o histórico de outro utilizador requer o nível de administrador
  adequado.
- **Contas antigas:** eliminar uma conta de utilizador antiga (legacy) volta
  a funcionar, em vez de não fazer nada silenciosamente.
- **Administração de utilizadores em massa:** adicione utilizadores
  existentes a suborganizações e grupos em massa via CSV, com correspondência
  pelo endereço de e-mail. Corrigidos também um bloqueio com linhas de CSV
  preenchidas de forma desigual e um erro de servidor ao adicionar dois ou
  mais utilizadores novos de uma vez.
- **Listas de membros:** os utilizadores eliminados já não aparecem nas
  listas de membros das suborganizações.
- **Single sign-on:** uma série de correções de robustez. Os tokens expirados
  devolvem agora uma resposta clara de "expirado", as organizações sem
  configuração SAML recebem uma resposta adequada de "não encontrado" em vez
  de um fluxo de início de sessão errado, o fim de sessão conclui sempre,
  mesmo quando o pedido de saída não pode ser verificado, e desapareceram
  várias falhas relacionadas com configuração de fornecedor de identidade em
  falta. O tempo de vida do token devolvido pelo fornecedor é transmitido à
  aplicação.
- **Tokens de sessão:** corrigidos os tokens de sessão de curta duração que
  eram rejeitados como inválidos mesmo sem estarem expirados.
- **Ferramentas de gestão:** a região da organização é visível na API de
  gestão, o utilizador de sistema de uma organização pode ser reatribuído, e
  a administração de planos e de utilização ganhou endpoints dedicados. Estas
  alterações afetam as ferramentas internas da equipa DocBits, não a
  aplicação do cliente.

## Email Service — em produção: `1.40.2`

- **Importação na região correta:** os domínios de e-mail de entrada existem
  por região, e os e-mails que chegam à região errada são reencaminhados para
  a certa. As organizações dos EUA já não dependem do caminho de entrada da
  UE.
- **Microsoft 365:** os tenants de nuvens nacionais configuram-se através de
  uma seleção de Cloud Instance, o que corrige as importações O365 para
  clientes dos EUA. Um tenant inválido produz agora um erro de início de
  sessão claro em vez de um erro de servidor, e credenciais de tenant
  incompletas falham de imediato com uma mensagem, em vez de silenciosamente.
- **Teste de ligação:** testar uma caixa de correio IMAP que não responde
  falha com uma mensagem de tempo limite ao fim de alguns segundos, em vez de
  esbarrar num tempo limite do gateway.
- **Higiene da caixa de entrada:** os e-mails sem anexos são movidos para
  fora da caixa de entrada em vez de se acumularem.
- **Sem duplicados em novas tentativas:** os carregamentos para a API de
  documentos incluem uma chave de idempotência, pelo que uma entrega repetida
  não pode criar o mesmo documento duas vezes.
- **Nomes das origens:** as origens O365 com uma pasta configurada incluem o
  e-mail da conta no nome, para que origens semelhantes sejam distinguíveis. O
  endereço da caixa de correio é lido a partir da conta autenticada, e não de
  um campo preenchido manualmente.
- **Limpeza do registo de importação:** as entradas do registo de importação
  são mantidas durante 90 dias e depois eliminadas automaticamente.

## PO Match Service — em produção: `1.59.3`

- **Estado "tabela incompleta":** as faturas cuja tabela de linhas não pôde
  ser mapeada recebem o seu próprio estado, em vez do enganador "ordem de
  compra não encontrada" (ver Destaques). O dashboard mostra-o com o ícone de
  não correspondido.
- **Melhor detalhe dos erros:** as falhas de mapeamento de tabelas indicam a
  coluna específica que não foi mapeada.
- **Mais rápido em faturas grandes:** a correspondência baseada em regras
  agrupa os candidatos por número de artigo e lê as definições de tolerância
  uma vez por organização, em vez de uma vez por linha.
- **Comportamento da API mais limpo:** os pedidos de regras de PO
  inexistentes devolvem uma resposta adequada de "não encontrado", e as
  entradas de cache corrompidas são descartadas em vez de causarem erros
  repetidos.
- **Correspondência pelo total:** corrigido um erro na correspondência com o
  total da ordem de compra.

## Fulltext Service — em produção: `1.39.1`

- **Formatos numéricos europeus:** os montantes escritos com vírgula decimal
  (`1.234,56`) são normalizados antes da indexação, pelo que as pesquisas e
  os filtros por montante funcionam independentemente do formato numérico.
- **Contagens de resultados honestas:** quando uma pesquisa encontra mais
  documentos do que a janela do dashboard devolve, a resposta indica-o, em
  vez de apresentar uma lista truncada como se estivesse completa.
- **Contagens ERP:** corrigido um erro de token que podia interromper o fluxo
  de contagem em direto no dashboard.
- **Resiliência da indexação:** a indexação resiste agora a falhas
  temporárias da base de dados e do serviço de autenticação (repetição
  automática, recurso à base de dados principal) e descarta mensagens de fila
  malformadas em vez de as repetir indefinidamente.

## OCR Service — em produção: `1.10.3`

- **Ordem de leitura estável:** o texto é lido por uma ordem determinística,
  pelo que o mesmo documento é extraído sempre da mesma forma.
- **Documentos grandes:** o tempo disponível para o OCR escala com o tamanho
  do documento, pelo que ficheiros muito grandes já não falham por limite de
  tempo.
- **Caracteres invulgares:** um sanitizador limpa os caracteres que o motor
  de OCR não consegue representar, corrigindo falhas em documentos com
  símbolos exóticos.
- **Menos falhas transitórias:** os erros temporários de ligação ao
  armazenamento são repetidos automaticamente, e um processo parado é
  detetado pelo facto de estar, ou não, a consumir trabalho.

## Extraction Service — em produção: `1.53.3`

- **Faturas dos EUA com imposto zero:** corrigido um caso em que o par
  correto de valores líquido/imposto era descartado quando o valor do imposto
  é zero.
- **Extração de tabelas:** as tabelas continuam editáveis quando o mapeamento
  configurado espera mais colunas do que as que o documento fornece, e foi
  corrigida uma falha com dados de linha invulgares.
- **Ordem de leitura estável:** espelha a alteração do OCR acima, para que a
  extração veja a mesma ordem de tokens que o OCR produziu.
- **Modelos de IA:** descontinuação do nível Turbo, replicada do API Service.

## Docflow Service — em produção: `2.7.3`

- **Correspondência de PO em fluxos de trabalho:** os valores de comparação
  em falta são tratados como dados em falta e não como uma divergência.
- **Cartões de confirmação de encomenda:** o comprador e a pessoa responsável
  são determinados de forma fiável.
- **Cartões de cotação:** o registo passa a indicar quando existe um preço
  cotado, mas fora do intervalo de datas permitido, situação que antes
  parecia dados em falta.
- **Custos de transporte:** quando nenhuma das partes tem encargos, o caso é
  resolvido pelo cartão do operador em vez de ficar parado.
- **Segurança:** os tokens de API de fluxos de trabalho são validados face à
  organização a que pertencem.
- **Ativação mais rápida:** a verificação de fluxos de trabalho ativos é
  guardada em cache, e os processos de segundo plano reiniciam de forma
  limpa, em vez de deixarem processos parados para trás.

## Barcode Service — em produção: `1.18.1`

- **Divisões demoradas:** a ligação à fila de tarefas é mantida ativa durante
  trabalhos longos de códigos de barras, pelo que a divisão de lotes grandes
  já não fica parada perto do fim.

## FTP Service — em produção: `1.31.2`

- **Limpeza do registo de importação:** a mesma retenção de 90 dias e limpeza
  automática do Email Service.

## Auth Bridge Service — em produção: `0.4.1`

- **Alertas de replicação precisos:** a ponte de replicação de contas UE/EUA
  mede uma paragem a partir do último progresso real, e não a partir do
  primeiro erro, e conta apenas movimento de replicação genuíno como
  progresso. Desapareceram os falsos alertas noturnos de paragem da ponte.
  Nada muda na aplicação.

## Operator Service — em produção: `1.42.1`

- **Estabilidade dos processos:** um processo parado é detetado pelo facto de
  estar, ou não, a consumir trabalho, e a comunicação inativa entre processos
  foi desligada.

---

## Sem alterações nesta versão

O **Auto Accounting** (`1.21.1`) foi reconstruído sem alterações visíveis para
o cliente. O **Docnet** (`1.55.1`) e o **Ideas** (`0.3.1`) não têm alterações
nesta janela.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
