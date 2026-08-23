# Notas de versão do DocBits — 29 de julho – 12 de agosto de 2026

_O que mudou na atualização de produção do DocBits implementada a 10–12 de
agosto de 2026, cobrindo tudo desde a versão de 29 de julho. Cada serviço
indica a versão que entrou em produção e, de seguida, as novidades ou correções
em linguagem simples. Os serviços não listados (Auto Accounting `1.21.1`,
Ideas `0.3.1`, OCR `1.10.3`, Operator `1.42.1`, PO Match `1.59.3`, FTP
`1.32.4`) não tiveram alterações visíveis para o cliente._

---

## Destaques

- **Suporte de FacturaE.** As faturas eletrónicas espanholas FacturaE 3.1 são
  classificadas e extraídas de origem, com mapeamentos de campos completos. Na
  mesma vaga, os mapeamentos de ebInterface (Áustria) tornaram-se fiéis à
  versão, as predefinições de Factur-X e ZUGFeRD ganharam o caminho do nome da
  empresa, e foram corrigidos vários mapeamentos predefinidos errados para
  descontos, IVA e preços unitários.
- **Pesquisa e ordenação do dashboard reparadas.** A ordenação deixou de
  depender das colunas que estão visíveis, um filtro OR combinado com um
  intervalo ou uma igualdade já não apaga as expressões de pesquisa, os nomes
  de fornecedores voltam a aparecer na pesquisa rápida e as datas em formato
  ISO são lidas corretamente.
- **A extração por IA corrige-se a si própria.** Uma troca comprovável entre o
  valor líquido e o total feita pela IA é anulada automaticamente, os campos
  lidos pela IA já não regressam errados após um reinício do documento, e a
  extração de tabelas por IA processa os documentos em lotes de páginas, para
  que as tabelas longas cheguem completas.
- **Os fluxos de trabalho sobrevivem a uma falha de autenticação.** Um serviço
  de autenticação momentaneamente inacessível é tentado de novo em vez de
  fazer falhar a execução, e um acionador de fluxo de trabalho que não
  consegue autenticar-se comunica o erro em vez de deixar o documento preso.
- **Os PDFs difíceis de ler voltam a ser extraídos.** Quando o descodificador
  de texto PDF padrão não consegue ler uma página (frequente em ficheiros
  produzidos pelo Ghostscript), a extração recorre a um segundo motor em vez
  de não devolver nada.
- **A MFA funciona entre regiões.** Os dados de inscrição na autenticação de
  dois fatores são replicados entre as regiões UE e EUA, pelo que um segundo
  fator configurado numa região é aceite na outra.

---

## Web App — `10.49.4`

### Início de sessão e contas

- Terminar sessão num separador do navegador termina também a sessão nos
  outros separadores, sem os avisos de erro que costumavam aparecer quando os
  separadores discordavam sobre a sessão.
- Alterar a sua própria palavra-passe no perfil passa pelo endpoint de
  self-service dedicado, pelo que funciona sem permissões de administrador.
- O início de sessão com chave de acesso a partir da região que não é a de
  origem mostra mensagens de erro traduzidas, e o respetivo botão de submissão
  está visível.

### Ecrã de validação

- O separador "Extracted table" já não fica a carregar indefinidamente quando
  já existe uma tabela de IA.
- Os documentos sem dados de código de barras já não fazem falhar a vista de
  atribuição de códigos de barras.
- As linhas multi-imposto do M3 oferecem o código de imposto como lista
  pendente alimentada pela lista de valores, em vez de um campo de texto
  livre.
- Abrir faturas de fornecedor de grande dimensão é visivelmente mais rápido.

### Tarefas

- As colunas do Kanban são paginadas à medida que percorre a lista, pelo que
  os quadros com muitas tarefas carregam depressa.
- O contador de tarefas abertas na barra lateral conta as tarefas no contexto
  da sua suborganização, e não no contexto do documento que estiver aberto.

### Workflow Builder

- A lista de fluxos de trabalho mantém a pesquisa, a ordenação, a página e o
  tamanho da página quando abre um fluxo de trabalho e regressa, inclusive
  através do breadcrumb, e a página abre por predefinição no separador List.

### Definições e administração

- A página de Master Data já não surge em branco devido a uma condição de
  corrida na ordenação, e ordenar por badges já não faz a página falhar.
- Uma subscrição no estado "a cancelar" pode ser retomada.
- A página de detalhe de XSLT comunica os erros de carregamento em vez de não
  mostrar nada, e as definições de notificações por e-mail usam toda a largura
  da página, com um painel de registos funcional.
- O seletor de organizações para utilizadores com várias organizações tem o
  layout de linhas, o dimensionamento e as cores de tema corretos, desloca-se
  corretamente e oferece um filtro para contas com muitas organizações.
- Analytics: um pedido de métricas falhado mostra um estado de erro em vez de
  apresentar zeros, e os widgets de utilização indicam honestamente quando não
  existem dados de medição disponíveis.
- Foram removidas opções de cache obsoletas da página de gestão de cache, e as
  páginas de Utilizadores e Grupos perderam as barras de deslocamento duplas
  aninhadas.
- "Use Default Template" no gestor de layouts já não falha nem fica sem
  reação; também deixou de afirmar que não existe um layout predefinido.
- As regras de seleção mantêm os operadores de correspondência de texto,
  presença e regex quando uma regra é reaberta.
- Os Tipos de Documento suportam regras de transformação por tipo, e a
  interface da lista de regras ganhou uma ação de valor fixo.
- Os badges de estado das ordens de compra mapeiam corretamente os valores de
  estado com a capitalização do ERP.
- Os ecrãs do DocNet (AI Workforce), incluindo o Agent Wizard, estão
  traduzidos, e a caixa de diálogo de criar/editar ideia desloca-se
  horizontalmente.
- Cotações do portal de fornecedores: as unidades de medida geridas aparecem
  na tabela de linhas, o estilo de aprovação aplica-se apenas às cotações de
  contrato, e a linha de comparação já não aparece quando ambos os valores são
  idênticos.
- A alternativa JSON da página de erro é legível no modo escuro, e os
  relatórios usam uma etiqueta adequada de "últimos 7 dias" em vez de um "7"
  solto.

## API Service — `12.74.0`

### Dashboard e pesquisa

- A ordenação funciona independentemente das colunas visíveis, e uma
  palavra-chave que a pesquisa delega no texto integral já não deixa para trás
  um fragmento SQL inválido.
- Os nomes de fornecedores voltam a aparecer na pesquisa rápida para
  organizações sem indexação de texto integral.
- As datas em formato ISO (2026-08-12) já não são mal interpretadas pelo
  normalizador de datas que assume o dia primeiro.
- As exportações do dashboard encaminham os valores de texto simples, como os
  números de fatura, para a coluna certa.

### Faturas eletrónicas

- FacturaE 3.1 (Espanha): regra de classificação e mapeamentos de campos
  completos.
- As regras de classificação de XRechnung estão ancoradas à sua família de
  sintaxe, pelo que um documento UBL já não é correspondido por regras CII e
  vice-versa.
- A versão aceite "3.0" cobre toda a sua família de patches (3.0.1, 3.0.2).
- As faturas CII assumem o nome legal do fornecedor, usando o nome comercial
  apenas como alternativa.
- Os mapeamentos de ebInterface (Áustria) são fiéis à versão, com um catch-all
  corrigido e fixtures reconstruídas.
- As predefinições de Factur-X e ZUGFeRD ganharam o caminho de extração do
  nome da empresa, e foram corrigidas as transformações de cabeçalho
  predefinidas para taxa de imposto, tipo de fatura e campos de nível 3, bem
  como a semântica de descontos, IVA e preços unitários em toda a família.
- Os códigos de categoria de imposto de origem já não são mapeados cegamente
  para os códigos do seu ERP.
- Os documentos que mencionam tanto "fatura" como "nota de crédito" preferem a
  classificação de nota de crédito.

### Documentos e extração

- Quando o descodificador PDF padrão não consegue ler o texto incorporado de
  uma página, a extração recorre a um segundo motor, pelo que os PDFs afetados
  são extraídos em vez de regressarem vazios.
- O interruptor principal dos códigos de barras é agora `BARCODE_EXTRACTION`;
  a antiga definição de códigos QR continua a funcionar como alias.
- Foi tapada uma fuga de memória no agendador de segundo plano; degradava
  lentamente o processamento ao longo de dias de atividade.
- Os fornecedores importados sem país ficam em branco em vez de assumirem a
  Alemanha por predefinição.

### Exportação e dados mestre

- Save Rules comunica a falha quando não escreve nada, em vez de afirmar
  sucesso.
- As linhas de montante zero já não são descartadas das exportações de
  contabilidade automática, e foi corrigido um filtro que correspondia a todos
  os buckets.
- As exportações M3 suportam post-hooks de informação adicional.
- Uma única sonda de conjunto de dados falhada já não deixa em branco todo o
  ecrã de Master Data.
- As caches de PO são invalidadas quando o ERP atualiza o estado de uma ordem
  de compra, pelo que o dashboard deixa de mostrar o estado obsoleto.

### Administração

- Cada preferência mostra o utilizador que a alterou pela última vez.
- As regras de extração podem ser eliminadas por fornecedor e clonadas através
  de novos endpoints.
- Os destinatários dos e-mails de alerta de estado são comparados de forma
  segura face a NULL, o que corrige uma falha na entrega de notificações.

## Auth Service — `1.75.9`

- Uma chave de API de organização usada contra uma organização não relacionada
  é rejeitada.
- Criar uma organização devolvia um erro apesar de gravar efetivamente a
  linha; agora responde corretamente.
- Iniciar sessão com uma chave de acesso quando nenhuma está inscrita devolve
  o seu próprio código de erro, para que o ecrã de início de sessão possa
  dizer o que se passa.

## Auth Bridge Service — `0.4.2`

- As tabelas de inscrição na autenticação de dois fatores são replicadas entre
  as regiões UE e EUA, e as linhas são identificadas pela sua verdadeira chave
  primária.

## Docflow Service — `2.8.7`

- Um acionador de fluxo de trabalho que não consegue autenticar-se comunica a
  falha em vez de deixar o documento preso, e um serviço de autenticação
  momentaneamente inacessível é tentado de novo em vez de ser tratado como um
  token inválido.
- Cartões de comparação de cotações: os números de artigo só são comparados
  nas linhas descritas pela matriz de preços de artigos; as linhas sem unidade
  de medida ou sem preço são ignoradas em vez de fazerem falhar a comparação.
- O cartão de comparação de preços contratados ganhou uma opção de operador
  any/all, e as caches dos cartões são invalidadas corretamente após migrações
  e atualizações de código.
- As ligações SSL interrompidas são tratadas como transitórias e tentadas de
  novo em vez de fazerem falhar a execução.

## Docnet Service — `1.56.4`

- Os endpoints de estado e de versão já não bloqueiam em verificações em
  direto, o que costumava fazer a caixa de diálogo Service Versions ficar
  pendurada.

## Email Service — `1.40.6`

- Quando um e-mail recebido é ignorado, o motivo é mostrado na linha do evento
  de importação em vez de ficar em silêncio.
- Os ficheiros contentores `.eml` anexados já não são importados como
  documentos.
- Um início de sessão falhado no Microsoft Office produz uma mensagem de erro
  legível, e um erro de transporte do serviço de IA conta como "indeterminado"
  em vez de uma rejeição.

## Extraction Service — `1.53.8`

- Uma troca comprovável entre o valor líquido e o total feita pela IA é
  anulada após a extração de campos, e as falhas das salvaguardas são
  registadas em vez de passarem em silêncio.
- Os campos lidos pela IA já não regressam errados após um reinício do
  documento.
- A extração de tabelas por IA processa por lotes de páginas e acumula todos
  os lotes, pelo que as tabelas longas chegam completas.
- Os documentos que mencionam tanto "fatura" como "nota de crédito" preferem a
  classificação de nota de crédito.
- A limpeza repetida de cabeçalhos e rodapés é colocada em cache, o que
  acelera a extração em documentos com várias páginas.

## Fulltext Service — `1.41.7`

- Um filtro OR combinado com uma condição de intervalo ou de igualdade já não
  apaga as expressões de pesquisa.
- A ordenação usa os caminhos de índice corretos e revela o motivo real quando
  o backend de pesquisa rejeita uma consulta; uma regressão de ordenação que
  quebrava por completo a pesquisa por consulta em bruto foi corrigida na
  mesma semana em que surgiu.
- As consultas de documentos funcionam em índices mais antigos mapeados como
  texto.
- A cache de tokens está limitada ao par token/organização, pelo que mudar de
  organização não pode servir resultados no contexto anterior.
