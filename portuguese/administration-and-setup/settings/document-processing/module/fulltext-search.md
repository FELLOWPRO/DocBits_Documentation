# Pesquisa de texto completo

A pesquisa de texto completo permite aos utilizadores procurar no conteúdo real dos documentos e em todos os campos extraídos, e não apenas em nomes de ficheiros e IDs.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Caixa de diálogo „Fulltext Module Required“ quando o módulo está desativado"><figcaption><p>A caixa de diálogo «Fulltext Module Required» aparece nas páginas que dependem do módulo.</p></figcaption></figure>

## Sem o módulo

Quando a pesquisa de texto completo não está ativada, a barra de pesquisa do painel apenas consegue consultar um pequeno conjunto de campos estruturados. As pesquisas em texto livre apenas comparam o conteúdo com:

* `filename`
* `ID` do documento
* `invoice_id`
* `purchase_order`

Tudo o que estiver fora destes campos é ignorado. Não existe pesquisa por conteúdo nem suporte para intervalos, operadores ou filtros inteligentes.

## Com o módulo ativado

Ao ativar a pesquisa de texto completo, a pesquisa passa a abranger cada campo extraído de um documento e a barra de pesquisa do painel aceita uma linguagem de consulta mais rica. As consultas podem combinar filtros por campo, intervalos, operadores lógicos, datas relativas e filtros inteligentes.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Barra de pesquisa do painel com uma consulta de intervalo e a lista de documentos filtrada"><figcaption><p>A barra de pesquisa do painel aceita a linguagem de consulta estendida. Digite uma consulta e pressione <kbd>Enter</kbd> para filtrar a lista de documentos.</p></figcaption></figure>

### Consultas por campo

Para pesquisar num campo extraído específico, preceda o nome do campo com dois pontos. Os nomes dos campos seguem a convenção da API (minúsculas, snake\_case) e aplicam-se a qualquer campo capturado pelos seus tipos de documento — fornecedor, dados da fatura, linhas, campos personalizados.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Consultas por intervalo

Os operadores de comparação funcionam em campos numéricos e de data. São suportadas comparações abertas e intervalos delimitados.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Operadores lógicos

Combine cláusulas com `AND`, `OR` e `NOT`, usando parênteses para fixar a precedência. As listas `IN` testam um campo contra um conjunto de valores possíveis.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Datas relativas

Expressões temporais avaliadas no momento da consulta. Podem ser usadas em qualquer lugar onde se espere uma data.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Filtros inteligentes

Atalhos de um único token para consultas comuns. Funcionam isolados ou dentro de uma expressão maior.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documentos cuja data de vencimento já passou.
* `@User` — filtrar por pessoa atribuída; substitua `User` pelo nome do utilizador.
* `#INV-1234` — pesquisa rápida pelo identificador do documento.
* `$5k+` — montantes superiores a 5.000 na moeda do documento.

## Funcionalidades derivadas

Dois modos de pesquisa especializados assentam no módulo de pesquisa de texto completo. Ambos exigem que o módulo esteja ativado e não podem ser usados de forma independente.

### Pesquisa vetorial

A pesquisa vetorial encontra documentos semanticamente semelhantes à consulta, em vez de apenas correspondências léxicas. O painel trata qualquer consulta que comece por `vector:` como uma pesquisa vetorial, executa-a sobre os embeddings dos documentos e ordena os resultados por semelhança.

```
vector: frozen food invoices
```

A indexação vetorial é controlada separadamente do índice de texto na página **Definições de pesquisa de texto completo**. Ao desativar, deixam de ser gerados embeddings para novos documentos, mas o índice de texto mantém-se.

### Pesquisa com IA

A pesquisa com IA aceita consultas em linguagem natural e utiliza um LLM para extrair filtros estruturados, que são depois executados contra o índice de texto completo. Preceda a consulta com `ai:`.

```
ai: invoices from Ruiz over 1000 last quarter
```

A pesquisa com IA e a pesquisa vetorial não são intercambiáveis: a vetorial encontra conteúdo semelhante, a pesquisa com IA traduz linguagem em filtros. A pesquisa com IA não tem um interruptor próprio — apoia-se nos índices de texto completo e vetorial existentes.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Página „Definições de pesquisa de texto completo“ com os subíndices Documents, Vector Index e Fulltext (Text)"><figcaption><p>Definições de pesquisa de texto completo. O índice vetorial tem o seu próprio interruptor; o índice de texto funciona enquanto o módulo estiver ativo.</p></figcaption></figure>

## Pré-requisitos

* A infraestrutura OpenSearch corre em segundo plano para alimentar o índice.
* Na primeira ativação, todos os documentos existentes são reindexados. A duração depende do número de documentos da organização.
* Apenas os administradores da organização podem ativar ou desativar módulos.

## Como ativar o módulo

1. Aceda a **Definições → Processamento de documentos → Módulo**.
2. No grupo **Dashboards**, ative **Full text search**.
3. Confirme a caixa de diálogo de subscrição, se aparecer.
4. Aguarde a conclusão da reindexação inicial antes de utilizar consultas de texto completo.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Página „Módulos“ com o interruptor „Full text search“ sob o grupo Dashboards"><figcaption><p>O interruptor <strong>Full text search</strong> encontra-se em <strong>Módulo → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
O preço do módulo de pesquisa de texto completo é tratado pelo seu contacto comercial DocBits. A confirmação da subscrição aparece na primeira ativação do módulo.
{% endhint %}

## Consulte também

* [Definições de pesquisa de texto completo](../../log-settings/fulltext-search-settings.md) — gestão do índice e interruptor do índice vetorial.
* [Funções Fulltext & Vector Search](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — API de scripting para `fulltext_search()` e `vector_search()`.
* [Visão geral dos módulos](README.md) — lista completa dos módulos opcionais do DocBits.
