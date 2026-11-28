# Usar o painel

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Seleção e carimbo de data dos dados](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=01).
<!-- touchless-admin-video-v2-20261104:end -->

### Filtros

| Filtro                            | O que faz                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **7D / 30D / 90D**                | O período dos indicadores principais e da fila. O padrão é 30 dias                                                                                                                                                           |
| **Document Type**                 | Filtra as métricas Touchless e a análise relacionada para um único tipo, por exemplo INVOICE. As propostas de regras aprendidas têm atualmente seleção própria; veja abaixo                                                                                                                                                                        |
| **Segment field / Segment value** | Somente se a sua organização executa vários processos por um único tipo de documento (por exemplo, pedidos diretos, indiretos e EAM no campo `order_type`). Escolha um campo para ver a divisão, escolha um valor para restringir tudo a ele |
| **Document ID**                   | Abre o **Document Trace** de um documento                                                                                                                                                                                  |

A **sub-organização** que você selecionou no topo do DocBits restringe os indicadores principais e a fila de fornecedores. Os clusters de problemas e a análise com IA sempre abrangem a organização inteira.

### Tipo de documento de nível superior versus propostas de regras aprendidas

O seletor superior e o tipo de documento em **Learned rule proposals** são independentes na implementação verificada atualmente. A seção carrega os seus próprios tipos disponíveis e escolhe inicialmente a primeira entrada. Selecionar **ORDER_CONFIRMATION** acima pode, portanto, deixar **INVOICE** selecionado abaixo. Essas propostas dizem respeito a faturas, não às confirmações de pedido escolhidas para as métricas.

Antes de aplicar uma regra, verifique o tipo mostrado dentro dessa seção. Se nenhum tipo correspondente estiver disponível ali, as propostas para ele não foram estabelecidas. A seção também usa uma base de dados própria, como documentos corrigidos dos últimos 60 dias, em vez de adotar automaticamente o período do cabeçalho. Isso descreve os controles separados atuais; não afirma que uma sincronização tenha sido implementada.

### Os cinco indicadores principais

<figure><img src="../../../.gitbook/assets/touchless-outcome-cards-pt-20261126.png" alt="Os quatro cartões de resultados Puro sem contato, Somente para aprovação, Intervenção manual e Exceções de processo mostram a percentagem em grande e o número de documentos abaixo. Cobertura de diagnóstico é o quinto cartão."><figcaption><p>Os quatro cartões de resultados e a Cobertura de diagnóstico. Este relatório de teste de 30 dias contém 54 exceções de processo e nenhum documento nas outras categorias de resultados.</p></figcaption></figure>

Os primeiros quatro cartões são **categorias de resultados independentes**. Em cada cartão, o valor grande é a participação dessa categoria em todos os documentos contados e a linha menor é o seu número de documentos. As quatro participações totalizam 100%; não adicione uma taxa combinada separada.

| Cartão | O que conta | Informações adicionais |
| --- | --- | --- |
| **Puro sem contato** | Documentos concluídos sem intervenção manual ou aprovação separada | Diferença em pontos percentuais em relação à meta touchless |
| **Somente para aprovação** | Documentos que exigiram aprovação, mas nenhuma outra correção manual | Apenas a participação e o número desta categoria |
| **Intervenção manual** | Documentos que exigiram uma correção manual ou outra interação do utilizador | A sua própria participação e número |
| **Exceções de processo** | Documentos que não puderam ser concluídos devido a uma exceção de processamento ou integração | A sua própria participação e número |
| **Cobertura de diagnóstico** | Em quantos documentos bloqueados a **primeira causa** do bloqueio é conhecida | Número sem causa conhecida |

A caixa separada **Taxa touchless · Puro sem contato + Somente para aprovação** abaixo dos cartões combina as duas primeiras categorias. Por exemplo, 60 documentos puros sem contato mais 15 documentos somente para aprovação de 100 produzem uma **taxa touchless de 75%**. O cartão Somente para aprovação continua a mostrar **15%**, não 75%.

* Um cartão mostra um travessão (—) em vez de **0%** quando não há nada para medir. Um travessão significa «sem dados», não «zero».
* **Cobertura de diagnóstico** = documentos com uma causa de bloqueio conhecida ÷ todos os documentos bloqueados. Exemplo: 50 documentos bloqueados, 10 com causa desconhecida → 40 ÷ 50 = **80%**. Um valor baixo significa que ainda não compreendemos por que os documentos param. Melhore-o antes de corrigir causas individuais.
* **Clique num cartão** para abrir a lista de documentos por trás do número numa nova aba. Os cartões com 0 documentos não são clicáveis. Cobertura de diagnóstico abre os documentos sem causa conhecida.

### Taxa de contato sem contato ao longo do tempo

<figure><img src="../../../.gitbook/assets/touchless-report-trend-pt-20261104.png" alt="Tendência do relatório com Puro sem contato, a Taxa touchless combinada e a linha tracejada da meta."><figcaption><p>Puro sem contato e a Taxa touchless combinada ao longo do tempo. A linha tracejada marca a meta.</p></figcaption></figure>

O gráfico mostra **Puro sem contato**, a **Taxa touchless** combinada e a **linha da meta**. A taxa combinada inclui Puro sem contato e Somente para aprovação, pelo que é igual ou superior à taxa pura sem contato; não some os dois valores. Cada ponto tem o seu próprio número de documentos concluídos elegíveis, portanto uma taxa diária não é automaticamente a taxa de todo o período. Períodos curtos mostram pontos diários e períodos longos, pontos semanais. Os pontos baseados em dados recentes incompletos são marcados como **Provisório**.

**Exemplo.** Depois de ativar a correspondência automática de pedidos em 1 de outubro, a taxa pura sem contato sobe de 55% para 68% em duas semanas. O gráfico mostra o dia em que a curva muda, permitindo investigar o momento. Uma associação antes/depois não prova por si só que esta configuração causou a melhoria. Compare o tipo de documento, a combinação de fornecedores e outras alterações.

### Onde o touchless se perde primeiro

<figure><img src="../../../.gitbook/assets/touchless-blocking-stages-pt.png" alt="Gráfico de barras dos documentos bloqueados por primeira etapa e motivo de bloqueio"><figcaption><p>Documentos bloqueados pela etapa e motivo em que pararam primeiro. Aqui, <strong>Field validation: Required field missing</strong> afeta o maior número de documentos (58), seguido de <strong>Export mapping failed</strong> (46) e <strong>PO item mismatch</strong> (27). Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

Um gráfico de barras de **Documentos bloqueados** por etapa do processo: a **primeira** etapa que parou um documento.

**Exemplo.** Barras: Supplier Identification 12, Field Validation 41, PO Line Match 7. A maior barra indica que deve examinar primeiro **Field Validation**. Um valor extraído em falta é uma causa possível; compare a fatura original, as regras de campos e os dados de origem disponíveis antes de a confirmar.

#### Por que os documentos não são totalmente sem contato? (canal de lançamento Nova)

As organizações no canal de lançamento **Nova** veem a resposta à mesma pergunta numa lista expansível em vez do gráfico de barras. O painel chama-se **Por que os documentos não são totalmente sem contato?** e fica ao lado de **Taxa de contato sem contato ao longo do tempo**.

<figure><img src="../../../.gitbook/assets/touchless-why-reasons-pt-20261126.png" alt="Área Validação expandida com 32 documentos e o motivo A validação da fatura eletrônica falhou. A ação Documentos abre o painel lateral correspondente."><figcaption><p>Expanda uma área para ver os seus motivos e abrir os documentos por trás de um motivo. O relatório de teste também contém uma área Exportar e configurar com 22 documentos.</p></figcaption></figure>

* O cabeçalho indica quantos documentos a lista abrange. Cada linha é uma área do primeiro bloqueio com a sua percentagem, número de documentos e barra. As linhas são ordenadas da maior para a menor.
* Clique numa linha para abrir os seus motivos. Apenas uma área fica aberta de cada vez; clique novamente para a fechar. São mostrados os primeiros **cinco** motivos; selecione **+N mais** para revelar os restantes. Ao fechar a área, a lista volta a cinco.
* **Corrigido sem um bloqueio** é uma área separada para documentos corrigidos por um utilizador, embora o relatório não tenha encontrado um primeiro bloqueio técnico. Use-a para investigar oportunidades de melhoria dos processos dos utilizadores e da formação, em vez de procurar uma etapa do processo que falhou.
* A lista provém dos mesmos dados do relatório que os indicadores principais. Os números não são recalculados no navegador, portanto o total no cabeçalho e as linhas coincidem.
* Se a sua instalação ainda não envia estes dados, o painel indica isso em vez de mostrar **0**. Uma lista vazia com a mensagem de «nada registado» significa que não se perderam documentos no período; são estados diferentes e não deve interpretar o primeiro como uma boa notícia.

##### Documentos por trás de um motivo

Selecione **Documentos** num motivo para abrir um painel lateral sem sair do relatório. O cabeçalho mantém visíveis o motivo, a área, o período e o tipo de documento.

<figure><img src="../../../.gitbook/assets/touchless-reason-documents-pt-20261126.png" alt="Painel lateral de documentos do motivo com pesquisa, Abrir na lista de documentos, detalhes dos documentos e paginação."><figcaption><p>O painel de documentos do motivo apresenta 25 documentos por página. Neste exemplo de teste, A validação da fatura eletrônica falhou tem 32 documentos correspondentes.</p></figcaption></figure>

* **Pesquise** por fornecedor, nome de ficheiro ou número de documento. Limpe a pesquisa para voltar a todos os documentos do motivo; uma mensagem sem correspondências não significa que o motivo não tenha documentos.
* A tabela mostra o **documento, fornecedor, data de receção, resultado, primeira etapa bloqueada e um detalhe curto**. Selecione uma linha ou o nome do documento para abrir o **Rastreio do documento**. **Voltar** do rastreio regressa ao mesmo motivo, pesquisa e página.
* Use **Anterior** e **Avançar** para percorrer páginas de **25 documentos**. O rodapé mostra o intervalo visível, o total e a página atual.
* **Abrir na lista de documentos** abre a lista completa numa nova aba com os filtros de motivo, período do relatório e tipo de documento aplicados. O relatório e o painel lateral permanecem abertos na aba original.
* Se o carregamento falhar, use **Tentar novamente**. Um resultado vazio e um erro de carregamento são estados diferentes.

O canal de lançamento **Vesta** mantém o gráfico de barras descrito acima. Se a sua página mostrar barras, está em Vesta; se mostrar a lista expansível, está em Nova. Ambos respondem à mesma pergunta, portanto o resto desta página aplica-se em ambos os casos.

### Oportunidades de fornecedores

<figure><img src="../../../.gitbook/assets/touchless-supplier-queue-pt.png" alt="A tabela Supplier opportunities com volume, pure rate, documentos perdidos, causa raiz, documentos recuperáveis, ganho esperado, confiança e status"><figcaption><p>A fila de fornecedores (reduzida às quatro primeiras linhas). O primeiro fornecedor tem 106 documentos, uma pure rate de 38.7 % e 65 documentos recuperáveis, por isso corrigi-lo vale <strong>+21 pp</strong>. Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

A fila responde a **"Qual fornecedor devemos corrigir primeiro?"** Ela é ordenada por documentos **Recoverable**, do maior para o menor, com 25 linhas por página.

| Coluna                         | Significado                                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Supplier Number / Supplier** | O fornecedor. Documentos sem fornecedor reconhecido aparecem como **No supplier identified (n documents)**                                                  |
| **Volume**                     | Documentos elegíveis do fornecedor no período                                                                                                          |
| **Pure Rate**                  | Participação de documentos pure touchless. Verde se estiver na meta ou acima dela, vermelho se abaixo                                                                          |
| **Lost Documents**             | Documentos que terminaram como AP assisted ou como exceção de processo. Nem sempre é uma pessoa: uma rejeição do ERP ou um documento parado por sete dias também conta |
| **Root Cause**                 | Quem é o responsável pela correção: Configuration, ERP integration, Export, Extraction, Master data, Measurement, PO matching, User process, Validation ou Unknown          |
| **Recoverable**                | Documentos perdidos cuja causa o DocBits pode corrigir: configuração, dados mestres ou modelo do fornecedor                                                               |
| **Expected Lift**              | Quantos **pontos percentuais** a taxa da sua organização ganharia se todos os documentos recuperáveis deste fornecedor passassem touchless (**+x pp**)               |
| **Confidence**                 | **High**, **Medium** ou **Low**: o quão segura é a causa diagnosticada                                                                                                |
| **Status**                     | New, Open, Investigating, In progress, Confirmed, Resolved, Dismissed. Um fornecedor com poucos documentos mostra **NEEDS\_DIAGNOSIS**                       |

**Exemplo.** A sua organização tem 1,000 documentos elegíveis no período. O fornecedor A tem 40 documentos recuperáveis, o fornecedor B tem 90 documentos perdidos, mas apenas 10 recuperáveis (o problema está do lado deles).

* Fornecedor A: 40 ÷ 1,000 = **+4.0 pp de ganho esperado**
* Fornecedor B: 10 ÷ 1,000 = **+1.0 pp**, embora B tenha mais documentos perdidos

A fila classifica A acima de B porque o **ganho esperado** é medido em relação à sua organização inteira, não em relação ao fornecedor. Um fornecedor com quatro documentos ruins não pode superar um com quatrocentos.

Use a caixa de busca ("Search supplier number or name") para encontrar um fornecedor. Clique em uma linha para abrir o **Supplier Diagnosis**.

### Vista de fornecedor ou de grupo

Por padrão, a fila tem uma linha por fornecedor. O seletor **Supplier | Group** ao lado da caixa de busca muda isso:

* **Supplier** lista cada chave de fornecedor como ela aparece nos seus documentos. É o padrão e se comporta como a fila antes de o grafo existir.
* **Group** agrupa em uma única linha as chaves de fornecedor que o DocBits agrupou. Uma linha agrupada lista os nomes mesclados na coluna **Members** e mostra todos eles em uma dica de ferramenta.

Uma linha agrupada não abre um **Supplier Diagnosis**, porque o diagnóstico trabalha com uma única chave de fornecedor. Volte para **Supplier** e clique no fornecedor desejado. Enquanto o DocBits não tiver construído um grafo para a sua organização, a vista de grupo retorna as mesmas linhas da vista de fornecedor, sem erro.

### Comparar fornecedores

<figure><img src="../../../.gitbook/assets/touchless-compare-suppliers-pt.png" alt="A página Compare suppliers com três fornecedores lado a lado e um gráfico de barras dos seus resultados"><figcaption><p>Três fornecedores lado a lado: pure rate, documentos perdidos e recuperáveis, causa raiz, ganho esperado e um gráfico de barras dos resultados. Cada <strong>Open</strong> leva ao Supplier Diagnosis. Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

Clique em **Compare suppliers**, marque **dois a cinco** fornecedores (cada um aparece com o seu número de documentos bloqueados) e clique em **Compare**.

A comparação mostra os fornecedores lado a lado: **Pure rate**, **Lost documents**, **Recoverable**, **Root cause**, **Expected lift**, um gráfico de barras dos resultados e um link para cada **Supplier Diagnosis**.

**Exemplo.** Os fornecedores A e B enviam o mesmo layout de fatura. B tem uma pure rate de 80 %, A apenas 35 %. O diagnóstico de A sugere "Master data". Compare as faturas originais, os valores extraídos e os registros de fornecedor importados antes de confirmar essa causa. A diferença de taxas por si só não prova que o layout está correto nem que os dados mestres de A estão incompletos.

### Analisar com IA

O botão **Analyse n clusters with AI** analisa os clusters de problemas com o maior potencial touchless (com pelo menos um número mínimo de documentos cada). Leva cerca de 13 segundos por cluster e abrange a **organização inteira**. Somente administradores podem iniciá-lo.

Enquanto ele é executado, você vê **Queued**, **Running**, **Done**, **Already analysed** ou **Error** para cada cluster, com um link **Open cluster**. Se a IA estiver desativada ou não configurada no ambiente, o botão fica desabilitado com o motivo, e **todo o resto da página continua funcionando**.

## Ontology: como o DocBits agrupa seus fornecedores

A área tem duas abas: **Report** contém o painel descrito acima e **Ontology** mostra o grafo de fornecedores usado pela vista de grupo da fila. A aba é somente leitura. Ela não altera nenhuma configuração nem documento.

O DocBits deriva o grafo uma vez por noite a partir dos documentos processados pela sua organização. Um nó de fornecedor carrega um nome tal como está impresso em um documento; uma aresta une os nomes que o DocBits lê como a mesma empresa, por exemplo porque a grafia difere apenas levemente ou porque ambos têm o mesmo número de identificação fiscal. Ao lado do título você vê a versão do grafo e quando ele foi calculado. **Reload** busca novamente o grafo atual.

A aba tem três partes:

| Parte | Conteúdo |
| --- | --- |
| **Your suppliers, grouped** | Os grupos e quantas grafias cada um contém. Um grupo com uma única grafia também é listado. |
| **How it all connects** | O grafo: fornecedores e grupos de fornecedores, as áreas temáticas em que as faturas ficam presas, os motivos concretos e os campos que as pessoas precisam corrigir com mais frequência. |
| **Explanation** | Os detalhes do nó selecionado: **What this is based on** lista as evidências por trás dele, **Also written as** lista as outras grafias que o DocBits viu e **fixed by DocBits** (com ícone de cadeado) marca um nó que o próprio DocBits mantém e não a sua organização. |

Os tipos de nó são explicados em linguagem simples na aba: um nome de fornecedor é um nome exatamente como aparece nos seus documentos, uma área temática é um ponto em que as faturas costumam ficar presas e precisam de uma pessoa, um motivo é uma causa concreta de uma execução automática malsucedida e um campo é um campo do documento que as pessoas frequentemente precisam corrigir ou preencher.

Um grafo vazio é um estado normal. Ele mostra **DocBits is still learning** com a nota de que a visão geral é construída todas as noites e aparece após a próxima execução. Uma organização nova ou uma execução noturna perdida se apresentam assim; não é um erro.

O grafo também funciona sem mouse: Tab passa para um grupo ou nó, Enter ou Space o seleciona e preenche a **Explanation**.

## Trabalhar com o Touchless Intelligence: uma rotina

1. **Semanalmente**: abra a aba e verifique a **taxa** e a **tendência** em relação à meta.
2. Veja **Diagnosis coverage**. Abaixo de cerca de 80 %, descubra primeiro por que os documentos param.
3. Leia **Where touchless is lost first** (Vesta) ou **Why documents are not touchless** (Nova) e escolha a maior etapa ou área.
4. Abra **Supplier opportunities**. Ordene por **Expected lift** e pegue o fornecedor principal com o status **RECOVERABLE**.
5. Leia os **clusters de problemas**, verifique **Missing evidence** e depois siga **What to change**.
6. Corrija uma causa confirmada. Para uma proposta DocBits suportada, use a pré-visualização e o histórico de alterações. Para uma correção no Infor, documente a origem e a importação separadamente; ela não cria automaticamente uma entrada de histórico de alteração de configuração no DocBits.
7. Depois de duas semanas, verifique o resultado **antes/depois**.

## Quem pode ver

* A aba faz parte do Analytics Dashboard. O seu administrador a habilita para a organização. Se a aba estiver faltando, pergunte ao seu administrador.
* **Administradores da organização** sempre a veem.
* Outros usuários a veem quando um administrador concedeu à função deles a aba **Analytics dashboard** (**Settings → Roles**). Sem essa concessão, somente administradores têm acesso.
* Algumas ações são exclusivas de administradores: **AI analysis**, **aplicar e desfazer uma alteração**, **learned rule proposals** e o **Consulting report**.

Se você não tiver permissão, a página mostra _Action not allowed, please contact the administrator_.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Métricas e cálculo](touchless-metrics.md)
* [Exemplos práticos: preço e quantidade](touchless-examples.md)
* [Supplier Diagnosis e clusters de problemas](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals e relatórios](touchless-change-proposals.md)
* [Explicar e melhorar o Touchless com MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
