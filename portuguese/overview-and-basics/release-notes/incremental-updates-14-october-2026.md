# Notas de versão do DocBits — 14 de outubro de 2026

_O que muda no hotfix de produção do DocBits a 14 de outubro de 2026 (versão
R1.0.15), cobrindo tudo desde o [hotfix de 15 de setembro](incremental-updates-15-september-2026.md).
Cada serviço indica a versão em implementação e, de seguida, as novidades ou
correções em linguagem simples. Os serviços não listados não tiveram
alterações visíveis para o cliente._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/pt.mp4" %}

---

## Destaques

- **O Settings Assistant.** Uma barra de chat em todas as páginas de definições
  responde a perguntas sobre a configuração da sua organização, no seu idioma
  e com base na documentação do DocBits. Lê o estado atual das suas definições
  e explica-as (permissões de grupo, canais de importação, interruptores de
  ordens de compra, contabilidade). Quando lhe pede para ativar ou desativar
  algo, mostra primeiro uma pré-visualização, aguarda a sua confirmação e
  oferece a opção de anular. "Open setting" salta diretamente para a
  definição, mesmo dentro de uma secção recolhida, e realça-a. Os
  administradores da organização ativam ou desativam o assistente em
  Informações da empresa. Só responde a perguntas sobre o DocBits e nunca
  altera nada sem confirmação.
- **Novos níveis de IA.** Os níveis Fast e Full passam a funcionar com novos
  modelos. Um novo nível Auto escolhe Fast ou Full por documento, e o Nexus
  Flash junta-se ao Nexus. Um modo de visão (híbrido ou automático) decide
  quando a imagem da página é enviada em conjunto. As preferências de modelo
  de IA guardadas passam por si para os novos níveis, e os ecrãs mostram
  apenas nomes de níveis. "Use AI" é uma lista pendente (Standard, Yes, No) com
  uma pré-visualização do que a extração estruturada vai pedir.
- **Verificação dos campos de cabeçalho.** O ecrã de validação tem um botão
  "Header field check" junto a Guardar. O seu relatório lista cada campo de
  cabeçalho com a origem do valor (IA, regra, script ou dados mestre), numa
  tabela compacta com filtro de origem, pesquisa e ordenação, e com as mesmas
  etiquetas de campo do ecrã de validação. O popup de origem mostra a origem
  de cada valor numa única faixa.
- **Segurança de início de sessão e da organização.** Um desafio MFA só pode
  ser usado uma vez em todos os caminhos de início de sessão, e registar um
  autenticador exige o código enviado por e-mail. As organizações possuem uma
  lista de domínios de e-mail verificados; um início de sessão social (por
  exemplo, Microsoft) junta-se à organização que lista o domínio e nunca cria
  por si só uma organização, um utilizador ou uma subscrição. Apenas os
  administradores da organização alteram as preferências da organização e
  escrevem ou aprovam regras de correspondência de ordens de compra. As
  respostas em cache deixam de poder passar entre organizações.
- **Correspondência de ordens de compra e encargos.** Os encargos que a ordem
  de compra prevê como zero recebem um limite mínimo absoluto, a tolerância de
  encargos aplica-se também aos encargos que a ordem não orça, e um campo pode
  listar vários elementos de custo cujos montantes são repartidos
  proporcionalmente à ordem de compra. Uma coluna de correspondência pode ter
  uma flag "allow mismatch". Os cartões de fluxo de trabalho comparam os
  encargos por lista, e o limite de execução de fluxos de trabalho sobe de 30
  para 50.
- **Menos números errados.** Os montantes são apresentados no formato pessoal
  de cada utilizador (Suíça e Eslovénia incluídas), os valores só com data
  mantêm o seu dia de calendário em todos os fusos horários, a equação do
  total dos EUA tem em conta os montantes adicionais e as faturas com vários
  impostos, e os documentos com montantes de cabeçalho de 0.00 deixam de cair
  na passagem de candidatos errada.

---

## Corrigido também nesta versão

- O dashboard deixa de ficar vazio quando uma condição de corrida define o
  filtro de suborganização com o ID da organização e, assim, exclui todos os
  documentos.
- Os valores de dimensão voltam a poder ser selecionados por todos os
  utilizadores.
- Foi corrigido um erro de carregamento reportado por um cliente.
- "Match on total" funciona para fornecedores cuja fatura tem uma única linha,
  e para as configurações de fornecedor que o reportaram.
- Documentos eletrónicos SPS: os encargos do 810 são ajustados, o layout dos
  encargos do 855 é atualizado e o logótipo do cliente na pré-visualização do
  documento eletrónico é corrigido.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Uma gaveta de chat do lado direito, com um interruptor, está presente em
  todas as páginas de definições. A conversa sobrevive à mudança de página, é
  limitada a 20 mensagens e mostra as alterações que aplicou, com opção de
  anular.
- Cumprimenta com perguntas adequadas à página de definições atual e mostra
  cartões de definição com um interruptor de ativar/desativar. Esc fecha
  primeiro os menus, Stop interrompe uma resposta em curso, e as capturas de
  ecrã nas respostas abrem numa lightbox.
- Aplicar uma alteração abre uma caixa de diálogo com pré-visualização,
  confirmação e anulação.
- Todas as definições são pesquisáveis a partir da barra lateral, e a
  definição encontrada é realçada com outra cor. "Open setting" desloca-se até
  ao destino dentro de um acordeão recolhido.
- Um interruptor de administrador da organização para o assistente encontra-se
  em Informações da empresa.
- Os conselhos de IA são atribuídos ao Nova, e só aparecem nomes de níveis,
  nunca ids de modelos.

**Ecrã de validação e tratamento de documentos**
- Novo botão "Header field check" com relatório, origem por campo e página de
  ajuda (ver Destaques). As etiquetas de origem e os chips de estado ficam
  dentro das suas células.
- Os emblemas de texto "from master data" junto às etiquetas de campo
  desapareceram; o popup de origem transmite essa informação.
- Corre em todo o lado uma única validação de campos partilhada, o que elimina
  o erro genérico "One or more fields need validation" depois do Auto
  Accounting.
- As dicas nos botões do popup de campo (Delete, Clear, Confirm) indicam o que
  cada um faz antes de clicar.
- Uma linha otimista mostra agora o que foi guardado, não o que foi escrito.
  Um remapeamento de colunas só pede confirmação quando uma coluna visível
  perde o seu mapeamento.
- As páginas além do limite de páginas do OCR são só de leitura e ficam
  marcadas, também no visualizador do Auto Accounting. O antigo painel de
  restrição de páginas da importação foi retirado.
- Aparece uma tabela de PO para cada número de ordem de compra num campo de
  cabeçalho com várias PO, e o Layout Builder identifica os separadores de PO
  a partir da chave da tabela de PO e deixa de reportar o módulo como
  desativado quando a tabela de PO está ativa.
- O cartão de proposta mostra a tolerância em vez de `[object Object]`, e o
  ecrã de comparação da aprovação deixa de arredondar as colunas de comparação
  configuradas (números de artigo).

**Contas, definições e erros**
- Cada notificação de erro e cada erro de início de sessão mostra o trace id
  do pedido falhado, para que o suporte o possa encontrar. Os erros do
  WebSocket do dashboard rejeitam exatamente o pedido que nomeiam.
- Informações da empresa lista os domínios de e-mail da organização.
- Os administradores podem reenviar o e-mail "Set your password" a partir da
  página do utilizador.
- Os administradores globais definem o início do contrato na tabela de
  subscrições.
- Os administradores da organização veem o separador Executive Dashboard e os
  botões de adicionar e eliminar XSLT. Os membros guardam layouts como
  preferência própria.
- Uma sessão sem organização recebe um erro claro e o seletor de organização
  em vez de um dashboard vazio.
- Os montantes seguem o formato numérico pessoal do utilizador, e os valores
  só com data mantêm o seu dia em todos os fusos horários.
- Os dados mestre enviam ids de suborganização apenas quando diferem do ID da
  organização, e os cabeçalhos personalizados de dados mestre seguem como
  cabeçalhos.
- A máscara de Tabelas deixa de cortar a lista pendente "Use AI", o texto de
  ajuda da IA deixa de cobrir a linha de treino, e a tabela de IA mantém o
  seu botão Apply direto, com uma verificação de cabeçalho só com ícone e uma
  mensagem de licença.
- Os ícones da extração de tabelas voltam a ser apresentados depois de o
  antigo tipo de letra de ícones ter sido removido.

**Quadro de tarefas**
- O quadro carrega a primeira página com menos pedidos duplicados, Enter
  executa a pesquisa de imediato, as respostas tardias são associadas à
  pesquisa certa, o rodapé mostra o número real de resultados em vez da
  capacidade da página, e uma eliminação iniciada numa organização é cancelada
  antes de ser enviada quando muda de organização.

---

## API Service — `12.83.293`

**Settings Assistant e MCP**
- Endpoint de chat com salvaguardas: apenas perguntas sobre o DocBits,
  nenhuma alteração sem confirmação, perguntas pouco claras ou meta recebem
  ajuda em vez de uma recusa, e as respostas transmitem primeiro os cartões e
  depois o texto.
- Blocos de construção só de leitura para cada área de definições (permissões
  de grupo, canais de importação, correspondência de PO, contabilidade,
  domínios de e-mail), um catálogo de ligações diretas com uma ferramenta de
  pesquisa de definições, e pesquisa na documentação com imagens da
  documentação do DocBits.
- Fluxo de aplicação da vaga 1: pré-visualização, confirmação e anulação para
  as definições suportadas, uma única regra de âmbito para as três, protegido
  contra dupla confirmação e expiração.
- As ferramentas MCP nunca leem ficheiros do servidor em modo remoto, e as
  ferramentas de fixtures e de laboratório só correm em dev.

**IA**
- Novos modelos por trás dos níveis Fast e Full, do nível Auto, do Nexus Flash
  e da preferência do modo de visão. As preferências `AI_MODEL` guardadas são
  movidas para os novos níveis.
- "Use AI" documenta o que a extração estruturada pede.

**Segurança e isolamento**
- Apenas os administradores da organização alteram as preferências da
  organização.
- A chamada `/accounting/rebuild` treina apenas a organização de quem chama,
  falha de forma segura se a consulta da organização falhar e responde 400 a
  um id inválido.
- A renderização de XSLT, XML e PDF nega o acesso a ficheiros e à rede, não
  resolve includes externos, e os bytes da fatura são saneados antes de
  chegarem ao transformador. As pré-visualizações PDF renderizadas só admitem
  anfitriões de imagens de confiança.
- As chaves de cache incluem a organização e o mesmo identificador dá sempre a
  mesma chave, pelo que o id de uma organização alheia deixa de poder ler
  dados em cache. Acabaram-se as limpezas da cache do dashboard à escala da
  organização a cada alteração de documento.
- A lista de domínios de e-mail da organização é transmitida ao Auth.

**Correspondência de ordens de compra e exportação**
- Um campo pode listar vários elementos de custo cujos montantes são
  repartidos proporcionalmente à PO.
- Os substitutos de aprovação ligam-se ao pedido de aprovação ativo, as
  gravações de aprovações reparadas deixam de bloquear, e um documento com
  aprovação pendente é recusado para exportação.
- A anotação PDF/A mantém o catálogo e o XML incorporado, pelo que as
  e-faturas conservam o seu XML após a anotação. As faturas UBL com o
  CustomizationID EN 16931 simples são classificadas (rede de e-faturas).
- O GRPR arredonda para as 6 casas decimais que o M3 aceita. Os fatores de
  conversão da unidade de medida base são adicionados à linha congelada.
- Os treinos e regras de formatação eliminados de forma lógica (soft delete)
  são respeitados, e o `update_document_fields` do MCP deixa de confirmar uma
  gravação que perdeu. `get_table_rules` responde com uma falha tipificada, e
  um payload de traduções vazio usa o seu valor de recurso.
- Os montantes eslovenos usam `sl_SI` e as preferências guardadas são
  migradas. Os rótulos de classificação personalizados enviados como ids UUID
  são resolvidos. Os dashboards partilhados mantêm `created_by` e a lista de
  partilha na atualização.
- As tramas de erro do dashboard transportam o `request_id` do pedido, e cada
  resposta JSON falhada transporta um trace id.
- O sistema reinicia apenas os workers com problemas em vez de toda a frota da
  API e verifica corretamente a lista de tarefas registadas. A fila do
  monitor de bloqueios volta a ser consumida.

---

## Auth Service — `1.78.49`

- Um desafio de autenticação multifator só pode ser usado uma vez em todos os
  caminhos de início de sessão, e não apenas no fluxo MCP. O registo exige o
  código de e-mail, não é emitido nenhum token de registo após um início de
  sessão com palavra-passe partilhada, e os utilizadores são notificados
  quando um fator é registado.
- As organizações possuem uma lista de domínios de e-mail, cada um atribuível
  uma só vez. Um início de sessão social junta-se à organização que lista o
  domínio verificado, nunca inventa uma organização, um utilizador ou uma
  subscrição, e recusa sem nomear ninguém, enquanto os administradores são
  informados. Os domínios que a Microsoft devolve são tratados.
- Cada início de sessão recusado transporta um trace id. Os administradores
  podem reenviar o e-mail "Set your password". O saldo do contrato tem sinal e
  o início do contrato é auditado.

## Auth Bridge — `0.5.7`

- A replicação de contas UE e EUA mantém a ligação alimentada durante a
  reconciliação, volta a anexar por si só um slot de replicação perdido, usa
  memória limitada e trata uma origem de replicação existente como sucesso. O
  início de sessão entre regiões é mais fiável.

## Docflow Service — `2.10.22`

- O cartão separado de preço unitário lê as definições de campo predefinidas
  da organização para os encargos e compara todos os elementos de custo que um
  campo lista.
- O limite de execução de fluxos de trabalho sobe de 30 para 50, e as
  pesquisas nos registos de fluxos de trabalho rejeitam um id que não seja um
  UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` reporta todas as colunas de tabela configuradas,
  incluindo as que estão vazias.

## Extraction Service — `1.56.0.1`

- Níveis: novos modelos por trás de Fast e Full, Auto, Nexus Flash e um modo
  de visão. Os pedidos de visão ao anfitrião de inferência ficam abaixo do
  seu limite de tamanho.
- A extração de tabelas com o Nexus agrupa páginas em lotes (duas por lote),
  executa os lotes em paralelo com um timeout medido, repete os erros
  transitórios e divide um lote que excedeu o tempo. Os campos de cabeçalho
  são lidos a partir de todos os lotes.
- Totais dos EUA: os montantes adicionais fazem parte da equação do total, o
  par 1 conta na salvaguarda do par 2, os candidatos de baixa pontuação são
  ignorados quando os impostos não são zero, e "above" e "below" correspondem
  a etiquetas de várias palavras.
- Os campos de identificador reparam caracteres que realmente ocorrem, e os
  caracteres invisíveis são tratados pelo que significam, pelo que um "O"
  deixa de se transformar num carácter estranho.

## Fulltext Service — `1.42.41`

- Novo índice para a documentação do DocBits, com endpoints de ingestão e de
  pesquisa, imagens nas respostas e um prazo para toda a pesquisa. Alimenta o
  Settings Assistant.

## PO Match Service — `1.59.48`

- Limite mínimo absoluto para os encargos que a ordem de compra prevê como
  zero, e tolerância de encargos para os encargos que a ordem não orça.
- Uma coluna pode ter uma flag "allow mismatch". Vários elementos de custo
  por campo são repartidos proporcionalmente.
- Apenas os administradores da organização escrevem ou aprovam regras de
  correspondência, e as condições das regras aceitam apenas uma gramática de
  expressões em lista de permissões.
- As alterações às regras podem ser simuladas contra um conjunto de regras de
  substituição sem gravar, para as propostas de alteração do Touchless. As
  colunas extra de PO a corresponder são lidas a partir do atributo do tipo de
  documento, com uma migração da preferência antiga.

---

_Não afetados nesta versão: Auto Accounting, Barcode, E-Mail, FTP, Ideas,
OCR, Operator. FTP e Operator incluem apenas manutenção interna._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
