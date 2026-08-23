# Notas de versão do DocBits — 12–25 de agosto de 2026

_O que muda na atualização de produção do DocBits a 25 de agosto de 2026,
cobrindo tudo desde a versão de 12 de agosto. Cada serviço indica a versão em
implementação e, de seguida, as novidades ou correções em linguagem simples. Os
serviços não listados não tiveram alterações visíveis para o cliente._

---

## Destaques

- **Isolamento mais rigoroso entre organizações.** Uma revisão de segurança
  fechou vários pontos onde dados de uma organização podiam ser lidos ou
  escritos a partir de outra: os scripts de documentos, as listas de
  utilizadores de suborganizações, as pertenças a grupos e o token de
  processamento que um documento transporta ao longo do pipeline são agora
  todos verificados face à organização de quem faz a chamada. As aprovações
  também aplicam corretamente o princípio dos quatro olhos: o segundo aprovador
  tem de ser uma pessoa diferente da primeira.
- **Os documentos deixam de ficar presos.** Foram corrigidas quatro causas
  distintas de documentos pendurados indefinidamente: exportações que
  permaneciam em "Exporting" depois de recusadas, reinícios que congelavam
  quando um passo de processamento falhava, divisões por código de barras que
  nunca davam resposta e o ecrã de contabilidade preso em "Preparing…". Em
  todos os casos, o documento agora ou termina ou mostra um erro real sobre o
  qual pode agir.
- **As notas de crédito são reconhecidas como notas de crédito.** As notas de
  crédito XRechnung 3.0, 3.0.1 e 3.0.2 em sintaxe CII, as notas de crédito CII
  puras e os documentos ZUGFeRD 2.4 / Factur-X 1.08 passam a ser todos
  classificados corretamente, com o total lido do campo certo. Nos documentos
  digitalizados que mencionam tanto "fatura" como "nota de crédito", a decisão
  é tomada pela palavra-chave que está mais próxima do tipo de documento, e os
  montantes voltam a ficar positivos quando reclassifica uma nota de crédito de
  volta para fatura.
- **A correspondência de PO faz contas em que pode confiar.** As tolerâncias
  são comparadas como decimais exatos em vez de valores de vírgula flutuante,
  baseiam-se no valor da ordem de compra, e as faturas que referenciam várias
  ordens de compra são correspondidas contra todas elas. As colunas que nunca
  mapeou deixam de distorcer a verificação do montante das linhas e, quando
  faltam colunas obrigatórias, o erro indica quais são.
- **As execuções de fluxos de trabalho preservam o seu trabalho.** Um fluxo de
  trabalho que escreve o valor de um campo passa a gravá-lo no documento de
  forma que uma exportação posterior não o possa reverter silenciosamente. Os
  acionadores repetidos já não descartam o que a execução já tinha feito, e
  dois acionadores que atinjam o mesmo documento entram em fila em vez de
  roubarem o bloqueio um ao outro.
- **Os e-mails de reposição da palavra-passe voltam a ser enviados.** Estavam
  silenciosamente a nunca sair do servidor. O formulário de reposição também
  passa a mostrar feedback real depois de submeter, e a resposta já não revela
  se uma conta existe.

---

## Web App — `10.55.0`

### Início de sessão e contas

- A reposição da palavra-passe volta a funcionar de ponta a ponta: o e-mail
  chega, o formulário confirma a submissão e a resposta é a mesma quer o
  endereço tenha ou não uma conta.
- Terminar sessão num separador do navegador termina também a sessão nos
  outros separadores, sem os avisos de erro que costumavam aparecer quando os
  separadores discordavam sobre a sessão.
- Se a sua organização exigir a adesão à autenticação de dois fatores, o ecrã
  de início de sessão passa a indicá-lo em vez de falhar sem mensagem. O
  início de sessão com chave de acesso entre regiões mostra mensagens de erro
  traduzidas, e o respetivo botão de submissão está visível.
- Os administradores já não conseguem ativar a obrigatoriedade de MFA em toda
  a organização antes de a adesão no início de sessão estar disponível, o que
  anteriormente podia deixar pessoas sem acesso.

### Ecrã de validação

- O controlo de zoom chega agora aos 150% (antes parava nos 80%), e ampliar
  uma tabela funciona para além da largura do contentor em vez de não fazer
  nada.
- Os campos de montante vazios contam como 0 em vez de dispararem um aviso de
  erro, e um duplo clique na imagem do documento é ignorado quando nenhum
  campo está selecionado.
- A faixa mostrada quando outra sessão detém o bloqueio do documento não tinha
  texto; agora explica-se. Etiquetar uma tabela já não dispara um falso aviso
  de "documento modificado externamente" sobre a sua própria alteração.
- Na tabela de IA, um remapeamento de coluna que iria desmapear outra coluna
  pede primeiro confirmação, e os valores que não são números são assinalados
  nas colunas AMOUNT e NUMBER.
- O separador "Extracted table" volta a ligar ao treino manual de tabelas
  quando está vazio, e já não fica a carregar indefinidamente quando já existe
  uma tabela de IA.
- Os números de artigo na tabela de linhas do Compare são mostrados como
  identificadores, e não arredondados como montantes.
- Os campos de aprovador resolvem os ids de utilizadores e grupos para nomes,
  pelo que nunca mostram um id em bruto nem ficam vazios. Os prazos das
  tarefas são convertidos por um único caminho com suporte de UTC, para que
  todos os visualizadores vejam a mesma data.
- Os documentos devolvidos à validação mostram um indicador de carregamento em
  vez de um ecrã morto enquanto são preparados.
- Abrir faturas de fornecedor de grande dimensão é visivelmente mais rápido.

### Contabilidade

- As linhas divididas mantêm o sinal % depois de premir Enter, e 0 % é aceite
  como valor.
- No filtro de contas, Enter confirma a primeira conta correspondente em vez
  de não fazer nada.
- Os carateres de flexdimension são mapeados pelo id da dimensão, pelo que as
  dimensões caem na coluna certa mesmo quando a ordem difere.
- Uma preparação de contabilidade falhada recupera com uma mensagem de erro em
  vez de ficar presa em "Preparing…" para sempre, e reabrir um documento já
  não apresenta dados obsoletos do documento anterior.

### Correspondência de PO

- Volta a ser possível abrir o PO Matching sem todas as colunas obrigatórias
  mapeadas; quando falta algo necessário, a mensagem indica as colunas exatas.
- As colunas que não estão mapeadas para nada são ocultadas quando o ecrã
  abre, depois de perguntar uma vez, e deixam de entrar no cálculo do montante
  das linhas.
- A quantidade correspondida é atualizada depois de guardar, e o aviso de
  colunas em falta encaminha-o para a Field Validation, onde pode corrigir o
  problema.

### Dashboard e pesquisa

- As colunas baseadas em listas (tipo de fatura, estado e semelhantes) mostram
  a sua etiqueta no idioma da interface em vez do valor armazenado em bruto.
- A pesquisa de texto livre aceita parênteses como texto simples; antes
  rejeitava a consulta. O operador de filtro "diferente de" mantém-se
  selecionado, e editar um filtro manualmente já não corrompe o nome do campo.
- Selecionar uma suborganização na pesquisa rápida insere o respetivo nome, e
  não o uuid, e a lista de sugestões de suborganizações já não mostra
  duplicados.
- O dashboard pode agora obter até 10.000 documentos por janela de pesquisa,
  pelo que os conjuntos de resultados grandes são paginados corretamente.
- O painel de documentos duplicados mostra as mesmas colunas resolvidas da
  lista principal, e os valores de filtro de fornecedor com várias palavras
  sobrevivem ao premir Enter.
- O contador de tarefas abertas na barra lateral conta as tarefas no contexto
  da sua suborganização, e não no contexto do documento que estiver aberto.

### Tarefas

- As colunas do Kanban são paginadas à medida que percorre a lista, pelo que
  os quadros com muitas tarefas carregam depressa.
- O e-mail de atribuição é enviado quando uma tarefa é atribuída, uma única
  vez. Editar uma tarefa ou marcá-la como concluída já não o reenvia, e a data
  de "atribuída em" mantém-se a data da atribuição. Os e-mails de tarefas
  também são apresentados corretamente no Outlook.

### Workflow Builder

- A lista de fluxos de trabalho mantém a pesquisa, a ordenação, a página e o
  tamanho da página quando abre um fluxo de trabalho e regressa, inclusive
  através do breadcrumb. A página abre por predefinição no separador List.
- O interruptor "executar fluxo de trabalho ao alterar" no construtor de
  layouts passa a controlar de facto a execução, e ativá-lo exige a escolha de
  um fluxo de trabalho.

### Definições e administração

- A ligação de download do WatchDog e o comando de configuração apontam para o
  ambiente em que está, e não sempre para produção.
- Árvores de decisão: o campo de documento selecionado mantém-se realçado
  quando o seletor reabre, as etiquetas truncadas ganham uma tooltip, e são
  mostrados nomes de utilizadores (e não ids em bruto) ao adicionar uma linha.
- A caixa de seleção System Admin é editável ao editar um utilizador.
- A página de Master Data já não surge em branco devido a uma condição de
  corrida na ordenação, e ordenar por badges já não faz a página falhar.
- Uma subscrição no estado "a cancelar" pode ser retomada.
- A página de detalhe de XSLT comunica os erros de carregamento em vez de não
  mostrar nada, e as definições de notificações por e-mail usam toda a largura
  da página, com um painel de registos funcional.
- O seletor de organizações para utilizadores com várias organizações tem o
  layout de linhas, o dimensionamento e as cores de tema corretos.
- Analytics: os Core Web Vitals são apresentados a partir dos dados de medição
  reais, a vista do serviço de registos funciona, e um pedido de métricas
  falhado mostra um estado de erro em vez de apresentar zeros.
- "Use Default Template" no gestor de layouts copia o layout predefinido como
  pretendido; antes falhava ou afirmava que não existia predefinição.
- As etiquetas de campos personalizados deixam de sobrepor-se às traduções
  incluídas dos campos padrão, e os ecrãs do DocNet (AI Workforce), incluindo
  o Agent Wizard, estão traduzidos.
- Cotações do portal de fornecedores: submeter uma cotação com um valor REF1
  fora da lista permitida é bloqueado, as unidades de medida geridas aparecem
  na tabela de linhas, e o estilo de aprovação aplica-se apenas às cotações de
  contrato.
- O MediOrder ganha deteção de documentos duplicados no seu ecrã de validação.

## API Service — `12.82.3`

### Segurança e isolamento entre organizações

- Mudar a organização ativa é validado face à sua pertença real e falha de
  forma segura, e foi encerrado um endpoint interno de teste que podia ser
  usado de forma abusiva para atravessar organizações.
- Os scripts de documentos já não podem ser lidos ou substituídos entre
  organizações, nem através da chamada de aplicação ao documento, nem através
  de um id de versão alheio ao guardar.
- As listas de utilizadores de suborganizações e as listas de membros de
  grupos só devolvem pessoas da organização de quem faz a chamada, e adicionar
  vários utilizadores a um grupo de uma só vez já não descarta todos exceto o
  primeiro.
- Uma credencial da organização errada é recusada antes de poder tornar-se o
  token de processamento de um documento, e as consultas de pesquisa de texto
  integral correm como o utilizador que faz a chamada, e não como uma
  identidade de serviço.
- A aprovação a quatro olhos é aplicada: o segundo aprovador tem de ser
  diferente da pessoa que aprovou primeiro.
- A lista do PO Dashboard em direto está limitada às suborganizações do
  utilizador.

### Pipeline de documentos

- Os documentos cuja exportação foi recusada já não ficam em "Exporting" para
  sempre, e os erros de exportação transportam sempre uma mensagem, em vez de
  uma mensagem vazia.
- Quando um passo de processamento falha, o documento passa a um estado de
  erro em vez de ficar preso em "reinício em curso" sem saída.
- Uma divisão por código de barras que falha ou excede o tempo marca o
  documento como Error em vez de mostrar silenciosamente "Running", e uma
  divisão que não produz filhos mantém o documento principal e assinala-o, em
  vez de eliminar tudo.
- Uma nova tentativa falhada já não pode substituir um documento que,
  entretanto, terminou o processamento.
- Os documentos reiniciados sem interação do utilizador e os filhos de
  divisões correm agora com um token de organização duradouro, para que o
  processamento prolongado não morra com uma sessão expirada.
- Uma resposta vazia de modelos de layout já não é colocada em cache durante
  seis horas, o que fazia os layouts desaparecer até a cache expirar.

### Extração e documentos eletrónicos

- Os montantes escritos com o sinal de menos no fim ("100,00-") são
  interpretados como negativos em vez de serem descartados.
- Os documentos suíços são detetados como suíços (CHF, números de IVA CHE,
  IBAN CH) em vez de assumirem as convenções alemãs, e as datas escritas com
  travessões tipográficos são interpretadas corretamente.
- As notas de crédito XRechnung 3.0, 3.0.1 e 3.0.2 em sintaxe CII são
  classificadas como notas de crédito, com o total lido do campo de total
  geral; o mesmo vale para as notas de crédito CII puras. Uma versão ZUGFeRD
  2.4 / Factur-X 1.08 declarada prevalece sobre o identificador genérico de
  perfil, e os tipos XRechnung sem sintaxe resolvem para o seu equivalente UBL
  ou CII em vez de falharem.
- Os campos de lista de valores (dropdown), como Tax Country e Tax Code,
  mantêm o valor ao longo da transformação de campos; estavam a ser
  esvaziados.
- Extração de tabelas: uma falha numa coluna apenas numérica fica confinada a
  essa coluna em vez de destruir a tabela inteira, a extração de tabelas por
  IA ganha um tempo limite que sobrevive a execuções em vários lotes, e foram
  corrigidas duas falhas em formas de tabela invulgares (linhas sem posições
  de página, contagens de colunas irregulares).
- Os padrões das regras de origem correspondem sem distinção entre maiúsculas
  e minúsculas.

### Exportação

- Uma verificação de impostos que falha durante a pré-visualização da
  exportação devolve um erro legível em vez de um erro de servidor, em ambos
  os endpoints de pré-visualização.
- A exportação SFTP pode enviar o documento original juntamente com o
  convertido.
- Quando existem configurações de exportação em vários níveis, a mais
  específica prevalece de forma consistente.
- As exportações BOD podem transportar atributos de tipo de coluna através do
  mapeamento.

### Importação e dados mestre

- O registo de importação de e-mail está completo: os e-mails recebidos
  rejeitados ou falhados têm sempre uma linha de registo com um motivo exato.
  Acabaram-se as perdas silenciosas.
- As importações BOD de ordens de compra mantêm as sublinhas ligadas à linha
  certa; uma flag transportada de linha em linha ligava-as à linha errada.
- Importar um CSV com vários fornecedores novos funciona (os ids gerados já
  não colidem), os aliases de condições de desconto de pronto pagamento são
  importados e respeitam a definição "em caso de conflito", e a opção IGNORE
  em caso de conflito aplica-se para além dos fornecedores.
- A sugestão de fornecedor (TF-IDF) mantém o id do fornecedor quando uma
  preferência é atualizada, pelo que as sugestões deixam de apontar para nada.

### Outras correções

- As linhas do dashboard resolvem as etiquetas das listas no idioma do
  utilizador, sem bloquear o pedido.
- Depois de editar campos, o estado de correspondência de PO é atualizado em
  vez de mostrar o estado anterior à edição.
- Os documentos de Purchase Order Change ganham cinco campos com paridade com
  a Purchase Order e um layout de validação de campos predefinido.
- As respostas de erro em 152 endpoints devolvem mensagens legíveis em vez de
  objetos de exceção em bruto, e a página de analytics de registos já não
  responde com 502 para organizações sem índice de registos.

## Auth Service — `1.77.9`

- Os e-mails de reposição da palavra-passe estavam silenciosamente a não ser
  enviados; corrigido, juntamente com o problema de thread safety subjacente.
- Um refresh token reutilizado é rejeitado: a verificação autoritativa na base
  de dados corre agora de todas as vezes, em vez de ser saltada num acerto de
  cache.
- Autenticação de dois fatores: uma aplicação de autenticação pode ser
  inscrita em paralelo com os códigos por e-mail, e remover a última chave de
  acesso ou regenerar os códigos de backup exige primeiro um segundo fator
  recente.
- Um id de suborganização válido já não é rejeitado com "Organization not
  found", e uma chave de API criada numa suborganização resolve o seu
  utilizador técnico a partir dessa suborganização.
- Editar uma organização valida o id de parceiro e já não repõe o tipo de
  organização como efeito colateral.
- "Remaining tokens" na vista de subscrição está ancorado ao ano do contrato,
  e não ao ano civil.

## Auth Bridge Service — `0.5.7`

- A replicação de contas entre as regiões UE e EUA recupera por si própria. Um
  fluxo de replicação interrompido volta a ligar-se no ponto em que estava, a
  replicação continua a fluir enquanto uma reconciliação decorre, e a memória
  da reconciliação é limitada, pelo que o serviço deixa de reiniciar em ciclo
  em tabelas grandes.

## Barcode Service — `1.18.7`

- A leitura de códigos de barras corre com um limite de tempo e comunica um
  timeout em vez de ficar pendurada, o que antes deixava o documento preso em
  processamento.

## Docflow Service — `2.9.8`

- Os valores de campos escritos por um cartão de fluxo de trabalho ficam
  gravados no documento em ambas as representações armazenadas, pelo que uma
  exportação posterior já não os reverte.
- Um acionador repetido preserva o trabalho que a execução já tinha feito, os
  acionadores em disputa sobre o mesmo documento entram em fila em vez de
  roubarem o bloqueio, e uma nova tentativa escalada é colocada em primeiro
  lugar na fila.
- Cartões de comparação de ordens de compra: as tolerâncias comparam-se como
  decimais exatos e baseiam-se no valor da ordem de compra, as direções de
  comparação invertidas estão disponíveis como opções, um responsável de grupo
  é reportado como grupo em vez de falhar uma comparação de id de utilizador,
  os ids de atribuição comparam-se corretamente como UUID, as linhas com
  valores numéricos vazios são ignoradas, e uma comparação de "received" sem
  quaisquer dados de receção reporta dados em falta em vez de fingir uma
  correspondência.
- O cartão Apply Decision Table foi descontinuado.

## Email Service — `1.41.0`

- As importações do Gmail recolhem cada anexo exatamente uma vez; acabaram-se
  os duplicados provenientes de recolhas sobrepostas.
- O cursor de leitura da importação só avança depois de uma importação ser
  confirmada, pelo que uma falha a meio da importação já não pode saltar
  e-mails.
- Quando uma configuração de importação é desativada por existir outra
  semelhante, essa desativação é visível e notificada em vez de silenciosa.

## Extraction Service — `1.54.5`

- Se um documento é uma nota de crédito ou uma fatura passa a ser decidido
  pela palavra-chave que está mais próxima da menção ao tipo de documento, em
  vez de valer a primeira ocorrência.
- Quando várias interpretações de impostos estão dentro da tolerância, a
  reconciliação exata é preferida a uma quase correspondência.
- Depois de um re-OCR forçado, o tipo de documento e a configuração regional
  são restaurados, pelo que a extração de tabelas e o treino voltam a
  funcionar em documentos re-OCR.
- Os documentos sem tipo de documento já não fazem falhar a consulta das
  regras de tabela.

## FTP Service — `1.32.8`

- A análise de pastas faz uma única ida e volta de listagem por pasta, com
  profundidade limitada, pelo que as importações de diretórios FTP grandes
  ficam muito mais rápidas e deixam de exceder o tempo limite.

## Fulltext Service — `1.42.3`

- Os documentos cujo payload de pesquisa armazenado não tinha campos extraídos
  são reindexados a partir da base de dados, pelo que voltam a aparecer na
  pesquisa do dashboard.
- A janela de pesquisa do dashboard suporta até 10.000 documentos.
- As pesquisas por facetas já não falham quando a pesquisa semântica está
  ativa.

## OCR Service — `1.10.7`

- O orçamento de tempo do OCR é dimensionado pelo custo real por página, pelo
  que os documentos longos terminam em vez de atingirem o limite do pipeline.

## PO Match Service — `1.59.8`

- As linhas de tabela com quantidade zero são ignoradas nas verificações de
  divergência em vez de produzirem falsas divergências.
- Quando faltam colunas obrigatórias da correspondência de PO, o resultado
  indica quais são.
