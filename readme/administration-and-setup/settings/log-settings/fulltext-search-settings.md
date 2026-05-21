# Configurações de Pesquisa de Texto Completo

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Configurações de Pesquisa de Texto Completo"><figcaption><p>Configurações de Pesquisa de Texto Completo — Diálogo "Módulo Necessário"</p></figcaption></figure>

As Configurações de Pesquisa de Texto Completo controlam o que o DocBits indexa e como esse conteúdo fica pesquisável em documentos, dados-mestre ERP e modelos. A página de configurações só abre quando o **módulo Pesquisa de Texto Completo** está ativo — veja [Pesquisa de Texto Completo](../document-processing/module/fulltext-search.md) para a linguagem de consulta voltada ao usuário.

## Pré-requisitos

O módulo Pesquisa de Texto Completo deve ser ativado em **Configurações → Processamento de Documentos → Módulo → Painéis → Pesquisa de texto completo**. Se o módulo não estiver ativo, um diálogo solicita que você:

* **Ir para Módulos** — Abra a página de configuração de Módulos para revisar as definições.
* **Ativar agora** — Ative o módulo Pesquisa de Texto Completo diretamente (inicia uma assinatura DocSearch).

A página de configurações em si fica disponível assim que o módulo estiver ativo.

## Layout da página

A página de configurações é organizada em três abas, cada uma cobrindo um tipo de conteúdo diferente que a Pesquisa de Texto Completo pode indexar.

### Aba "Documentos"

A aba Documentos cobre tudo relacionado à indexação de documentos processados:

* **Estatísticas de indexação** — totais de documentos indexados e pendentes, atualizados sob demanda.
* **Preferências de vetores** — três interruptores no nível da organização que decidem se a indexação vetorial roda em paralelo ao índice textual para documentos. A indexação vetorial alimenta o modo de consulta `vector:` e a função "Encontrar semelhantes".
* **Ações de reindexação** — inicie uma reindexação total ou incremental. Enquanto uma reindexação roda, você vê o progresso ao vivo (documentos por minuto, tempo restante), o estado atual do fluxo e a última falha (se houver).
* **Diagnóstico de sincronização** — diagnóstico sob demanda para casos em que o índice parece dessincronizado do armazenamento de documentos subjacente.

<mark>A reindexação não é destrutiva — a pesquisa existente continua funcionando enquanto o novo índice é reconstruído.</mark>

### Aba "ERP"

A aba ERP controla a indexação dos dados-mestre ERP — fornecedores, clientes, itens e entidades semelhantes. Cada entidade tem o próprio interruptor:

* **Indexação** — indexa textualmente a entidade para que fique pesquisável a partir do painel.
* **Vetor** — indexa vetorialmente a entidade para que possa ser combinada por consultas semânticas.

Use a ação **Alternar tudo** no topo da lista para aplicar o mesmo estado a todas as entidades de uma vez. A indexação começa em segundo plano; um indicador em cada linha mostra quando está em andamento.

### Aba "Modelos"

A aba Modelos lista as versões de modelo conhecidas pelo índice de Texto Completo. Use esta visualização para confirmar, após um redeploy, que as versões dos modelos das quais você depende estão presentes no índice.

## O que é indexado

Uma vez ativa e configurada, a Pesquisa de Texto Completo permite que os usuários:

* Pesquisem em todo o conteúdo do documento (não apenas nos campos de metadados).
* Encontrem documentos pelo texto contido nos arquivos enviados.
* Usem operadores avançados de pesquisa para consultas precisas.
* Acessem os resultados diretamente do painel.
* Usem pesquisa semântica (prefixo `vector:`) quando a indexação vetorial estiver ativa para aquele tipo de conteúdo.

Consulte a página do módulo [Pesquisa de Texto Completo](../document-processing/module/fulltext-search.md) para a referência completa da linguagem de consulta, incluindo consultas por intervalo, filtros inteligentes e o modo de pesquisa por IA.
