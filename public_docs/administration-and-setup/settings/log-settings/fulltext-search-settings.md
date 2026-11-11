# Configurações de Pesquisa de Texto Completo

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Configurações de Pesquisa de Texto Completo na sandbox, com uma caixa de diálogo que explica que o módulo é necessário e botões para Go to Modules e Enable Now"><figcaption><p>Quando a Pesquisa de Texto Completo está desativada, esta caixa de diálogo explica os próximos passos.</p></figcaption></figure>

As Configurações de Pesquisa de Texto Completo definem o que o DocBits indexa e como torna esse conteúdo pesquisável em documentos, dados-mestre ERP e modelos. A página de definições apresenta uma caixa de diálogo de requisito até que o **Fulltext Search module** esteja ativado — consulte [Pesquisa de texto completo](../document-processing/module/fulltext-search.md) para conhecer a linguagem de consulta destinada ao utilizador.

## Pré-requisitos

O módulo Fulltext Search tem de estar ativado em **Settings → Module → Dashboards & Analytics → Full text search**. Se o módulo não estiver ativado, a caixa de diálogo oferece três ações:

* **Help (?)** — Abre a documentação de Fulltext Search num novo separador antes de alterar qualquer definição.
* **Go to Modules** — Abre as definições do módulo Dashboards & Analytics para rever a configuração.
* **Enable Now** — Abre a caixa de diálogo de subscrição. Reveja e confirme essa caixa de diálogo antes de o módulo ser ativado; clicar apenas neste botão não o ativa.

A própria página de definições fica disponível assim que o módulo estiver ativo.

## Estrutura da página

A página de definições está organizada em três abas: **Documents**, **ERP** e **Templates**. Cada aba abrange um tipo de conteúdo diferente que Fulltext Search pode indexar.

### Aba Documents

A aba Documents abrange tudo o que está relacionado com a indexação de documentos processados:

* **Indexing statistics** — totais de documentos indexados e pendentes, atualizados sob pedido.
* **Vector preferences** — três interruptores ao nível da organização que controlam se a indexação vetorial é executada em conjunto com o índice de texto dos documentos. A indexação vetorial alimenta o modo de consulta `vector:` e a funcionalidade "Find Similar".
* **Reindex actions** — inicia uma reindexação completa ou incremental. Enquanto uma reindexação está em curso, vê o progresso em tempo real (documentos por minuto, ETA), o estado atual do fluxo e a última falha (se existir).
* **Sync diagnostics** — diagnóstico sob pedido para os casos em que o índice parece estar dessincronizado em relação ao repositório de documentos subjacente.

<mark>A reindexação não é destrutiva — a pesquisa existente continua a funcionar enquanto o novo índice está a ser reconstruído.</mark>

### Aba ERP

A aba ERP controla a indexação dos dados-mestre ERP — fornecedores, clientes, artigos e entidades semelhantes. Cada entidade tem o seu próprio interruptor:

* **Indexing** — indexa a entidade no índice de texto para que possa ser pesquisada a partir do painel.
* **Vector** — indexa a entidade no índice vetorial para que possa ser encontrada por consultas semânticas.

Utilize a ação **Toggle all** no topo da lista para aplicar o mesmo estado ligado/desligado a todas as entidades de uma vez. A indexação é iniciada em segundo plano; um indicador em cada linha mostra quando está em curso.

### Aba Templates

A aba Templates lista as versões de modelo conhecidas pelo índice Fulltext. Utilize esta vista para confirmar que as versões de modelo das quais depende estão presentes no índice após uma nova implementação.

## O que é indexado

Uma vez ativada e configurada, Fulltext Search permite aos utilizadores:

* Pesquisar em todo o conteúdo dos documentos (não apenas nos campos de metadados).
* Encontrar documentos pelo texto contido nos ficheiros carregados.
* Utilizar operadores de pesquisa avançados para consultas precisas.
* Aceder aos resultados de pesquisa diretamente a partir do painel.
* Utilizar a pesquisa semântica (prefixo `vector:`) quando a indexação vetorial estiver ativa para esse tipo de conteúdo.

Consulte a página do módulo [Pesquisa de texto completo](../document-processing/module/fulltext-search.md) para obter a referência completa da linguagem de consulta, incluindo consultas por intervalo, filtros inteligentes e o modo de pesquisa por IA.
