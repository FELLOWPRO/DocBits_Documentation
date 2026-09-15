# Notas de versão do DocBits — 15 de setembro de 2026

_O que muda no hotfix de produção do DocBits a 15 de setembro de 2026 (versão
R1.0.13), cobrindo tudo desde a versão de 1 de setembro. Cada serviço indica a
versão em implementação e, de seguida, as novidades ou correções em linguagem
simples. Os serviços não listados não tiveram alterações visíveis para o
cliente._

---

## Destaques

- **Um único conjunto de regras para a pesquisa do dashboard.** `field=value` é
  agora exatamente este valor em todos os motores de pesquisa, `field:value`
  significa "contém" (com `value*` e `*value` para "começa por" e "termina em"),
  e `field!=value` devolve também os documentos que não têm valor nenhum. Uma
  pesquisa sem chip é uma pesquisa por substring em todos os campos,
  identificadores de negócio incluídos. A contagem de resultados e a lista de
  resultados descrevem o mesmo conjunto de documentos, e uma pesquisa que
  atingiu a janela de resultados ou correu sem o índice de texto integral
  indica-o em vez de reportar "complete". A ligação de pesquisa própria do
  dashboard (WebSocket) nunca chegava ao índice de texto integral; agora chega.
- **Os fornecedores são reconhecidos mais vezes.** Quando um campo de pesquisa
  (número de identificação fiscal, IBAN, número de fornecedor) corresponde a
  exatamente um fornecedor, esse fornecedor é usado mesmo que um campo lato,
  como o nome, corresponda a vários. Os documentos XRechnung CII e Facturae
  voltam a transportar os seus campos de fornecedor. Quando os dados mestre
  substituíram um valor extraído, o ecrã de validação indica-o e permite
  restaurar o original.
- **A correspondência de ordens de compra explica-se a si própria.** O ecrã
  indica porque não há correspondência e porque uma correspondência não foi
  mantida, o histórico de correspondência lista as regras de transformação que
  correram, e os preços unitários da PO são derivados do valor líquido. As
  correspondências manuais voltam a funcionar para organizações sem regra de
  fallback, e uma tarefa de correspondência terminada à força marca o documento
  como falhado em vez de o deixar estacionado em "Queue" para sempre.
- **Documentos presos e falsos erros.** As organizações que carregam
  continuamente tinham documentos despromovidos para uma prioridade de fila que
  nunca era servida durante o horário de expediente (866 documentos presos em
  "new" num cliente). Um processo de novas tentativas podia sobrescrever um
  documento exportado com sucesso com "error" horas depois e disparar o e-mail
  de erro de exportação correspondente. Esse caminho está fechado.
- **Touchless Intelligence.** O separador de Analytics que mede quantos
  documentos passam pelo DocBits sem intervenção humana recebe a sua primeira
  versão completa: clusters de problemas com conselhos de IA, análise em massa,
  propostas de alteração com pré-visualização, aplicação e anulação, um
  diagnóstico de IA por fornecedor e um diagrama do fluxo do pipeline por
  documento.
- **Mais rápido onde os dados são grandes.** A lista pendente de contabilidade
  funciona para organizações com mais de 2.000 contas, a página de regras de
  E-Documents pagina as suas 1.600 regras no servidor em vez de congelar o
  browser, e Refresh no dashboard de ordens de compra devolve dados atuais em
  vez de uma lista em cache.
- **Segurança.** Os source maps do frontend deixam de ser enviados com cada
  implementação, os filtros de pesquisa de dados mestre são ligados como
  parâmetros SQL em vez de interpolados, um token expirado é rejeitado mesmo
  num acerto de cache, e a proteção de organização no token de processamento é
  aplicada independentemente da camada à sua frente.

---

## Web App — `10.66.3`

### Início de sessão e contas

- A sobreposição "Updating DocBits v10.59.3.1 → v10.59.3.1" que recarregava
  indefinidamente no sandbox foi corrigida. Um recarregamento para a mesma
  versão já não mostra a sobreposição, o ciclo é limitado por separador, e uma
  faixa oferece recuperação manual se voltar a acontecer.
- A caixa de seleção System Admin pode ser marcada num utilizador existente.
  Criar um administrador de sistema a partir do frontend passa a ter efeito; um
  trabalho de sincronização repunha a flag em cada execução.

### Dashboard e pesquisa

- Novas regras de operadores, também descritas no popup de ajuda da pesquisa:
  `=` é exatamente este valor (sem distinção entre maiúsculas e minúsculas),
  `:` é "contém", `: value*` é "começa por", `: *value` é "termina em", `!=` é
  tudo o que não é exatamente este valor, incluindo documentos sem valor. As
  aspas servem apenas para agrupar um valor com espaços.
- Uma expressão entre aspas, como `"Johnson and Johnson"`, é pesquisada como
  uma única expressão. "and" e "or" dentro de aspas já não são lidos como
  conectores.
- Quando uma pesquisa simples não encontra nada, o dashboard explica a regra e
  oferece chips de um clique (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Uma pesquisa com zero resultados repõe a paginação. Antes, a paginação
  mantinha a contagem da pesquisa anterior.
- Os números de requisição e os requisitantes são encontrados por uma pesquisa
  simples, sem chip.

### Ecrã de validação

- Os valores que os dados mestre substituíram são assinalados. Um distintivo
  âmbar mostra o valor original e o valor atual, o conjunto de dados e como
  correspondeu, e um botão restaura o valor extraído. Os valores confirmados
  pelos dados mestre ou preenchidos a partir da ordem de compra recebem as suas
  próprias etiquetas. Antes, todos eles transportavam o distintivo "Extracted
  using saved rules".
- O carimbo de aprovação é guardado mesmo quando a página já transporta outra
  anotação. Os documentos anotados descarregados não tinham o carimbo nesse
  caso.
- "Hide non mapped columns" mantém as colunas que treinou manualmente (por
  exemplo, Item Number e Purchase Order).
- Guardar regras de extração funciona depois de escrever um número de página e
  depois desenhar uma caixa para um campo. Essa sequência fazia falhar a
  gravação.
- O Train Model corre em segundo plano. O ecrã mostra "training started",
  consulta o resultado e reporta sucesso ou falha. As organizações grandes
  recebiam um erro de gateway enquanto o treino continuava no servidor.
- Modo escuro: o cursor de tesoura no ecrã de divisão e o interruptor de modo
  no ecrã de Auto Accounting voltam a ser legíveis.

### Correspondência de ordens de compra

As alterações anunciadas em [Hotfixes 8 de setembro de 2026](incremental-updates-8-september-2026.md)
chegam à produção com esta versão: a correspondência sobrevive à gravação, a
correspondência corre de novo quando o número da PO é corrigido, o ecrã indica
porque não há correspondência e porque uma correspondência não foi mantida, o
histórico de correspondência mostra as regras de transformação, e o preço
unitário da PO é calculado a partir do valor líquido. Além disso:

- O botão Auto Match também exporta o documento quando "PO Auto Match and
  Export" está ativo. Antes, a exportação só acontecia quando o documento era
  aberto a partir do dashboard através de "PO Match".
- O popup de tolerância de quantidade/preço unitário mantém-se aberto quando o
  servidor rejeita a gravação, para que os valores introduzidos não se percam.
- O botão Refresh do dashboard de ordens de compra limpa a cache do servidor
  antes de recarregar. Uma ordem de compra importada do ERP só aparecia passados
  sete a oito minutos.

### Contabilidade automática

- As organizações com mais de 2.000 contas pesquisam a lista de contas no
  servidor. A lista pendente estava vazia no sandbox para essas organizações, e
  o carregamento da página demorava cinco segundos.
- As contas referenciadas por um documento são resolvidas em lotes: um
  documento de 100 linhas com duas divisões por linha precisa de 4 pedidos em
  vez de 403.
- Os cabeçalhos das tabelas de Auto Accounting e de PO seguem a etiqueta
  definida no construtor de layouts em vez de um texto fixo.

### Definições

- Definições → E-Documents → Rules pagina, pesquisa e ordena o catálogo de
  1.600 regras no servidor. O separador apresentava todas as regras de uma vez
  e congelava o browser. "Reset all" é uma única chamada em vez de uma por
  regra.
- As Definições avançadas do tipo de documento mostram o estado guardado de
  cada interruptor. Um `false` guardado, uma tolerância `0` ou uma seleção
  vazia estavam a ser substituídos pelo valor predefinido, e mudar de tipo de
  documento deixava ficar os valores do tipo anterior.
- Regras de transformação: uma ação "Set value" é guardada. O editor enviava-a
  com um nome que o servidor rejeita.
- A ligação para os subtipos de documento é mostrada nos tipos de documento
  padrão.
- O mapeamento JPL da exportação SMB é descarregado como `.properties`, pelo
  que o ficheiro pode voltar a ser carregado. Tinha o nome `.xml` e era
  rejeitado no carregamento.

### Fluxos de trabalho

- Mudar o nome de um fluxo de trabalho mantém as alterações aos cartões feitas
  na mesma sessão. Os novos fluxos de trabalho são criados num único pedido de
  gravação, e as mudanças de nome de modelos são persistidas.
- Um ficheiro de fluxo de trabalho exportado contém o envelope de exportação
  completo (versão, nome, descrição). Os fluxos de trabalho avançados podem
  voltar a ser importados; antes, o ficheiro perdia a versão e era lido como um
  fluxo de trabalho padrão e rejeitado.
- Os filtros de coluna na lista de fluxos de trabalho combinam-se com AND. Com
  um filtro de nome e um filtro de data ativos, as linhas que correspondiam
  apenas ao nome entravam no resultado.
- Os prazos das tarefas usam o formato de data das suas definições de
  utilizador na lista, no quadro e na vista de detalhe.

### Analytics: Touchless Intelligence

O separador Touchless (Analytics → Touchless) mede quantos documentos passam
pelo DocBits sem que uma pessoa lhes toque, e porque é que os outros não
passaram. Esta versão completa-o:

- **Clusters de problemas com evidências.** Os documentos que precisaram de
  intervenção são agrupados por causa. Cada cartão de cluster indica os campos,
  os códigos de validação e as mensagens de erro em que falha, e o seu
  fornecedor, ou diz que não há nenhum. Os clusters que o DocBits pode corrigir
  (uma regra, uma definição de campo) são separados daqueles que só o
  fornecedor pode corrigir, e o orçamento de análise por IA vai primeiro para
  os corrigíveis.
- **Análise por IA, identificada como tal.** Um cartão de cluster diz se o
  conselho foi escrito por um modelo de linguagem ou por uma regra, o que a
  análise contou e quando deixou de ser verdade, e se um clique irá reutilizar
  uma análise em cache. Se o consultor de IA não puder correr neste ambiente,
  o separador explica porquê.
- **Análise em massa.** Analise muitos clusters numa só execução, veja cluster
  a cluster o que a execução está a fazer, e encontre os resultados depois. A
  lista de resultados sobrevive à navegação e ao recarregamento, e a execução
  já não fica pendurada em "Running · 0/6 done" numa vista de suborganização.
- **Propostas de alteração.** Uma recomendação torna-se algo sobre o qual pode
  agir: uma proposta que visa o campo que bloqueia os documentos, uma
  pré-visualização que mostra o que faria (nada é guardado), aplicação, efeito
  medido e anulação. Os agentes chegam aos mesmos passos através de ferramentas
  MCP. Os passos de correção ligam diretamente à página de definições que
  nomeiam, pré-filtrada por tipo de documento, campo ou regra.
- **Diagnóstico de fornecedores.** A página de fornecedores explica um estado
  vazio em vez de mostrar zeros, e oferece um diagnóstico de IA por fornecedor.
  Podem ser escolhidos até cinco fornecedores e comparados lado a lado.
- **Fluxo do pipeline.** Um diagrama por documento e por cluster mostra o
  percurso através da receção, classificação, verificação de documento
  eletrónico, fornecedor, OCR, extração, validação, correspondência de PO,
  aprovação e exportação, com a fase que o parou.
- **Razões da correspondência de ordens de compra.** A decisão de
  correspondência é rastreada por documento (fase, passagem, regra, coluna) e
  condensada no resultado Touchless. Os códigos de razão distinguem "ordem de
  compra não encontrada" de "divergência de linha" e "campo obrigatório em
  falta", e as propostas de tolerância do consultor visam o motor de regras que
  decide.
- **Números corretos.** Os mosaicos de KPI respeitam o filtro de suborganização
  e contam apenas os documentos que a vista de detalhe consegue listar.

### DocNet

- O feed de Atividades, o widget de Atividade recente e a cronologia de missões
  estão traduzidos. Os resumos de auditoria estavam em inglês nos 22 idiomas.
- Os agentes veem os campos que o tipo de documento define mas que a extração
  deixou vazios. Concluíam que esses campos não existiam e saltavam atualizações
  obrigatórias sem tentar escrever.

### Segurança

- Os source maps do frontend são removidos de todas as implementações. Todos
  os ambientes os serviam, produção incluída.

---

## API Service — `12.83.156`

### Reconhecimento de fornecedores e dados mestre

- Um fornecedor é identificado quando um campo de pesquisa é único. Com vários
  campos pesquisáveis, os resultados eram combinados como uma união, pelo que
  uma correspondência lata de nome com quatro fornecedores abafava um número de
  identificação fiscal que correspondia a exatamente um. Os campos que não
  correspondem a nada já não vetam os campos que corresponderam. Consulte
  [Definições de dados mestre](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  para saber como os campos funcionam em conjunto.
- As substituições por dados mestre são registadas com a sua origem: conjunto
  de dados, configuração, campo de origem, operador e tipo de correspondência.
  O ecrã de validação mostra isto e pode restaurar o valor extraído.
- O Cash Discount Term é importado do BOD de fornecedor; os fornecedores
  sincronizados a partir do ERP tinham-no vazio. Um Discount Term Overwrite
  introduzido como código completo ("143", "012", "X08") é aplicado; antes só
  o prefixo de percentagem era consultado.
- As pesquisas de dados mestre estão limitadas a 1.000 linhas por página e
  fazem o pivot em SQL. Uma pesquisa de 19.000 registos demorava cinco segundos
  por chamada e bloqueava a API.
- Os nomes de propriedades e os tipos de dados dos filtros na pesquisa de dados
  mestre são ligados como parâmetros SQL. Eram interpolados na consulta.

### Processamento de documentos

- Os documentos de uma organização que carrega continuamente eram despromovidos
  para a prioridade 9, que a fila só serve quando todas as prioridades
  superiores estão vazias. A despromoção está agora limitada a 3. O
  reconciliador que devia voltar a colocar em fila os documentos presos não
  tinha credenciais válidas em produção; agora tem.
- Um documento terminado e exportado nunca é sobrescrito com "error". Uma flag
  de fluxo de trabalho que nunca era limpa fazia com que o processo de novas
  tentativas apanhasse um documento exportado com sucesso uma vez por minuto
  até o limite de tentativas o marcar como "error" e disparar o e-mail de erro
  de exportação do cliente, 2 h 17 min depois da exportação.
- A fusão e a anexação aceitam ficheiros `.PDF` e `.Pdf`. A saída de scanners
  com o nome `SCAN0001.PDF` era rejeitada com "Only PDF files are allowed."
- A invalidação da cache percorre o espaço de chaves uma vez em vez de duas e
  limpa apenas os tipos de dados de pesquisa que um BOD alterou. Cada BOD
  apagava toda a cache de pesquisa da organização, bloqueando a API enquanto
  percorria as chaves de toda a gente.
- O retreino de modelos corre como tarefa em segundo plano e devolve
  imediatamente um estado que a UI consulta.
- Um token de processamento de outra organização é rejeitado independentemente
  da verificação de pertença à suborganização que o antecede.
- A sincronização de utilizadores deixa a flag de utilizador de sistema
  intacta em vez de a repor em cada execução.

### Exportação

- As linhas de receção do M3 emparelham o preço unitário exportado com a base
  de preço da própria linha da fatura. O preço viajava com o divisor da linha
  da PO e o ERP reavaliava a linha a 1.000 vezes o valor faturado.
- Uma exportação de tabela sobrevive a uma linha cuja ordem de compra foi
  removida; a linha é exportada sem base de preço.

### Documentos eletrónicos

- As faturas XRechnung CII cujo montante a pagar é 0,00 porque um montante
  pré-pago compensa o total mostram o total geral (BT-112) como montante total.
  O cliente via "total amount 0,00".
- Os documentos XRechnung CII e Facturae voltam a entregar os seus campos de
  fornecedor. Substituições obsoletas ao nível da organização estavam a
  sobrepor-se ao mapeamento predefinido correto, pelo que o reconhecimento de
  fornecedores nunca conseguia corresponder.
- O catálogo de regras de validação é paginado, pesquisado e ordenado no
  servidor, com facetas para a barra de filtros.

### Classificação

- Os documentos suíços são classificados como `de_CH`, `fr_CH` ou `it_CH` a
  partir do seu conteúdo (montantes em CHF, números de IVA CHE, IBAN CH). A
  configuração regional era tirada da predefinição da organização e os
  documentos suíços recebiam `de_DE`.

### Pesquisa do dashboard

- Uma única semântica de operadores no Postgres e no ClickHouse: `=` exato, `:`
  contém com wildcards nas extremidades, `!=` complemento incluindo valores
  vazios. No Postgres, `=` era uma correspondência por prefixo, pelo que
  `invoice_id=911892112` devolvia também 911892112333.
- Uma pesquisa simples é uma pesquisa por substring em todos os campos,
  identificadores de negócio incluídos. Um identificador com hífen, como
  `2026-003`, é um único literal, e o tipo de cláusula já não muda depois do
  quinto caráter.
- O chip de número de fatura é exato no Postgres, como já era no índice. Os
  zeros à esquerda, as formas decimais e as maiúsculas/minúsculas são tratados
  da mesma forma no texto livre e nos chips.
- A pesquisa WebSocket do dashboard transporta a credencial de quem faz a
  chamada para o serviço de texto integral. Todas as delegações eram recusadas
  antes, pelo que o dashboard pesquisava silenciosamente apenas no Postgres e
  apresentava a resposta como completa.
- A contagem de resultados e a lista de resultados correm sobre um único
  conjunto de predicados. A contagem era uma aproximação do Postgres enquanto a
  lista vinha do índice.
- A pesquisa vetorial está limitada à janela de resultados real e reporta o
  limite em vez de mostrar "(50)" como total exato.
- Uma pesquisa que correu sem o índice de texto integral (índice minutos
  atrasado, consulta de capacidades falhada, resolução de campos degradada)
  reporta o estado da sua janela em vez de "complete".
- Os scripts de documentos que chamam a pesquisa de texto integral
  autenticam-se corretamente e expõem as falhas em vez de devolverem um
  resultado vazio.

### Correspondência de ordens de compra (matcher em processo)

Para as organizações que fazem a correspondência na API e não no PO Match
Service: um número de PO corrigido é correspondido na gravação que o corrige.

### Analytics

- Touchless: todas as alterações de backend por trás da secção Web App acima,
  incluindo as evidências de fase registadas por cada fase do pipeline, o
  rastreio da correspondência de PO, as propostas de alteração com
  pré-visualização, aplicação e reversão, e o estado das execuções em massa
  numa única chamada por ciclo.

---

## PO Match Service — `1.59.34`

- O preço unitário de uma linha de PO é derivado do seu valor líquido, e não
  do seu total com imposto, e o snapshot de PO de um documento volta a derivar
  os seus preços unitários no momento da correspondência.
- O serviço regista de onde veio cada candidato a número de PO e que números
  uma execução consultou. O próprio número de fatura de um documento nunca é
  candidato a PO. Uma correspondência descartada deixa a sua razão no documento
  para o ecrã.
- A correspondência manual funciona para organizações cujas regras não têm a
  flag `is_fallback`. Os utilizadores escolhiam linhas, carregavam em
  corresponder, e nada voltava.
- Acabaram-se os documentos órfãos em "Queue": os timeouts de instruções da
  base de dados, os keepalives e um handler explícito de soft time limit
  marcam a tarefa como falhada em vez de dependerem de um kill que não deixava
  rasto.
- As alterações de tolerância são lidas por pedido de correspondência, pelo
  que uma tolerância guardada há um instante é usada pela correspondência
  seguinte.
- O rastreio de decisão em cinco fases é persistido por documento para o
  Touchless.

---

## Auth Service — `1.78.27`

- A expiração do token é aplicada nos acertos de cache. Uma entrada em cache
  podia autenticar até nove horas depois de o token expirar.
- A verificação do token deixa de escrever um `org_id` inalterado na linha do
  utilizador em cada pedido, o que produzia um UPDATE por chamada.
- Foi corrigida uma fuga de memória que levava o autoscaler ao máximo de
  réplicas, e o serviço voltou a dois workers.
- A flag de utilizador de sistema pode ser alterada num utilizador existente
  quando nenhum outro membro a tem.

---

## Auth Bridge Service — `0.5.7`

- Quando o fluxo de replicação UE ↔ EUA morre, o slot de replicação é
  reanexado no local em vez de reconstruir a ponte e voltar a executar a
  reconciliação completa de arranque, durante a qual o slot ficava inativo.

---

## Extraction Service — `1.55.33`

- Extração de tabelas por IA: as colunas de montante são tipificadas como
  números com uma descrição, e os valores não numéricos fabricados nas colunas
  de montante (um "St." copiado da célula vizinha para o preço unitário por)
  são descartados em vez de guardados.
- Faturas dos EUA: o ruído de vírgula flutuante abaixo do cêntimo já não decide
  entre pares candidatos de líquido/imposto (268.28 + 22.13 estava a perder
  para líquido = total, imposto = 0).

---

## Fulltext Service — `1.42.35`

- A cache de resultados de pesquisa está ativa em todos os ambientes;
  produção, sandbox e stage estavam a correr sem ela desde que os ficheiros de
  ambiente ativos foram criados. O carregamento e a eliminação invalidam-na,
  pelo que uma pesquisa depois de um carregamento vê o novo documento.
- Uma pesquisa simples por um número de fatura isolado devolve a fatura com
  correspondência exata. Os valores monetários escritos, os mapeamentos
  booleanos antigos, as datas e as flags de imposto sobrevivem à reconstrução
  do índice slim, e as entradas do índice sem campos são detetadas e
  recuperadas a partir da extração.
- O `=` exato num campo de texto dinâmico compara apenas o valor inteiro. Um
  wildcard no caminho analisado fazia com que `note_field=53173`
  correspondesse a "PO 53173 / 2024".
- Um identificador com hífen isolado, como `2026-003`, é um único literal, e
  não um saco de tokens.
- Os caminhos de leitura deixam de criar o índice que leem, e cada resposta
  com zero resultados transporta um estado de janela e uma razão.
- O limite de 50 do lado do serviço na pesquisa vetorial desapareceu.

---

## Docflow Service — `2.10.11`

- As importações de fluxos de trabalho avançados dependem do licenciamento da
  organização, e um lote é verificado antes de qualquer escrita. Uma
  organização sem o módulo avançado podia importar um fluxo de trabalho
  avançado que depois não tinha forma de abrir.
- A mudança de nome de um fluxo de trabalho segue com a gravação, e as mudanças
  de nome de modelos são persistidas.

---

## Docnet Service — `1.56.12`

- A descoberta de campos devolve todos os campos de cabeçalho que o layout
  define, preenchidos ou não, e coincide com o que a proteção de escrita
  verifica. Os agentes saltavam atualizações de campos obrigatórias porque os
  campos vazios pareciam ausentes.
- As identidades são colocadas em cache sob a mesma chave com âmbito de
  organização que a API usa, pelo que a fronteira de chave de API da
  organização mantém-se em ambos os serviços.

---

## Email Service — `1.41.6`

- As caixas de correio partilhadas do Office 365 com mais de dez subpastas
  resolvem todas as pastas. O Microsoft Graph pagina as pastas dez de cada
  vez; a 11.ª configuração e seguintes falhavam em todas as sondagens com
  "unable to find the selected Folder".

---

## FTP Service — `1.32.18`

- O agendador SFTP arranca em cada processo worker em vez de antes do fork. As
  importações SFTP periódicas estavam a falhar silenciosamente com um estado de
  agendador corrompido, enquanto um processo novo funcionava bem.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Apenas alterações de build e implementação (atualização da imagem base,
credenciais de CI). Sem alteração de comportamento.

<!-- Release R1.0.13. Announced: tickets with Jira "Release No." = R1.0.13 and a
     status on sandbox or beyond, plus DOCB-14454, DOCB-14450, DOCB-14415,
     DOCB-14419, DOCB-14431, DOCB-14045/46 (no Release No., on sandbox).
     Held back (Release No. R1.1): DRFS-778, DRFS-712, MEF-165, MEF-166, DOCB-14389.
     Labelled R1.0.12 but code ships now: DRFS-746/748/749/750/751, DOCB-14282. -->
