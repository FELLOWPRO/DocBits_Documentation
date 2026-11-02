# Alterações nos Endereços Web

Os endereços web (URLs) que você usa para acessar as páginas do DocBits foram organizados e padronizados. Esta página explica o que mudou, por que seus links antigos continuam funcionando e como encontrar qualquer página pelo novo endereço.

## O que mudou

Os endereços web do DocBits agora seguem um padrão claro: primeiro vem o item em que você está trabalhando e, depois, a visualização dele. Por exemplo, a tela de validação de um documento agora é:

```
/documents/<document-id>/validation
```

em vez do endereço antigo:

```
/field_validation_v1/<document-id>
```

Com o tempo, algumas telas acabaram ficando com várias versões e endereços diferentes. Na aprovação, por exemplo, havia endereços separados para a primeira aprovação, para a segunda aprovação e para as versões mais antigas de cada uma. Agora todos compartilham um único endereço, e o DocBits exibe automaticamente a versão correta para a sua organização. Você não precisa mais saber (nem adivinhar) qual versão se aplica ao seu caso.

Os endereços também passam a usar apenas palavras em letras minúsculas separadas por hífens, em vez de uma mistura de sublinhados, letras maiúsculas e abreviações.

## Seus links antigos continuam funcionando

Você não precisa alterar nada imediatamente. Favoritos, links salvos em e-mails e links salvos em qualquer outro lugar continuam funcionando exatamente como antes. Ao abrir um endereço antigo, o DocBits o redireciona automaticamente para o novo endereço, inclusive com os filtros ou as opções que faziam parte do link original.

Depois do redirecionamento, a barra de endereços do navegador mostra o novo endereço. Isso é esperado: significa que o redirecionamento funcionou. Com o tempo, recomendamos atualizar seus favoritos para que apontem diretamente para os novos endereços, assim você chega ao destino sem a etapa extra de redirecionamento. Mas não há prazo: os endereços antigos continuarão funcionando.

## Como encontrar uma página

Se você não souber qual é o novo endereço de uma página, ou se quiser apenas ir direto a algum lugar, há três maneiras de se orientar:

* **Mapa do site.** A página [Mapa do site](sitemap.md) lista todas as páginas do DocBits, agrupadas por área, com uma caixa de pesquisa e filtros. Abra-a pela barra lateral ou pela Pesquisa Rápida Global, escolhendo **Ver todos os resultados**.
* **Pesquisa Rápida Global.** Pressione <kbd>Cmd</kbd> + <kbd>K</kbd> no Mac ou <kbd>Ctrl</kbd> + <kbd>K</kbd> no Windows em qualquer lugar do DocBits e digite o nome do que você procura. Veja [Pesquisa Rápida Global](global-quick-search.md) para mais detalhes.
* **A tela de página não encontrada.** Se você digitar ou colar apenas a primeira parte de um endereço (por exemplo, `/documents` ou `/analytics`), sem o restante, o DocBits exibe uma tela de página não encontrada com a lista de todas as páginas que existem sob esse endereço. Ela funciona como um índice desse grupo de páginas e tem a mesma caixa de pesquisa da Pesquisa Rápida Global, portanto você também pode pesquisar a partir dela.

## Endereços antigos e novos

A tabela abaixo lista todos os endereços que mudaram, agrupados por área. Quando vários endereços antigos agora levam ao mesmo endereço novo, cada endereço antigo aparece em sua própria linha. Endereços usados apenas por desenvolvedores (por exemplo, páginas de depuração ou de demonstração) não estão listados, pois não afetam o uso no dia a dia.

Os marcadores de posição na tabela representam valores reais:

* `<document-id>` — o ID de um documento
* `<task-id>` — o ID de uma tarefa
* `<workflow-id>` — o ID de um fluxo de trabalho
* `<document-type>` — um tipo de documento, como fatura ou pedido de compra
* `<file-name>` — um nome de arquivo
* `<order-number>` / `<sales-order-id>` — a referência de um pedido de compra ou de venda
* `<organisation-id>` — o ID de uma organização
* `<layout-type>` — um tipo de layout
* `<supplier-id>` — o ID de um fornecedor
* `<page>` — um número de página

### Documentos

| Endereço antigo | Endereço novo |
|---|---|
| `/document/<document-id>` | `/documents/<document-id>` |
| `/field_validation_v1/<document-id>` | `/documents/<document-id>/validation` |
| `/field_validation/<document-id>` | `/documents/<document-id>/validation` |
| `/medi_order_v3/<document-id>` | `/documents/<document-id>/validation` |
| `/ready_for_approval_v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/in_review/<document-id>` | `/documents/<document-id>/review` |
| `/in-review-v2/<document-id>` | `/documents/<document-id>/review` |
| `/rejected/<document-id>` | `/documents/<document-id>/rejected` |
| `/summary/<document-id>` | `/documents/<document-id>/summary` |
| `/tbl_ext_v3/<document-id>` | `/documents/<document-id>/table-extraction` |
| `/tbl_training/<document-id>` | `/documents/<document-id>/table-training` |
| `/table_train_v3` | `/table-training` |
| `/doc_flow/<document-id>` | `/documents/<document-id>/flow` |
| `/document_pdf/<file-name>/<document-id>` | `/documents/<document-id>/pdf/<file-name>` |
| `/document_error/<document-id>` | `/documents/<document-id>/error` |
| `/document_classifiy/<document-id>` | `/documents/<document-id>/classify` |
| `/accounting/<document-id>` | `/documents/<document-id>/accounting` |
| `/quote-details/<document-id>` | `/documents/<document-id>/quote` |
| `/vertex-details/<document-id>` | `/documents/<document-id>/vertex` |
| `/po-matching/<document-id>` | `/documents/<document-id>/po-matching` |
| `/po-matching-v3/<document-id>` | `/documents/<document-id>/po-matching-v3` |
| `/ocr-document/<document-id>/<page>` | `/documents/<document-id>/ocr/<page>` |
| `/fields_sep_comp_v3/<document-id>` | `/documents/<document-id>/window/medi-fields` |
| `/simple_fields_comp/<document-id>` | `/documents/<document-id>/window/fields` |
| `/show_pdf/<document-id>` | `/documents/<document-id>/window/pdf` |

### Tarefas

| Endereço antigo | Endereço novo |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Fluxos de trabalho

| Endereço antigo | Endereço novo |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Pedidos e faturas

| Endereço antigo | Endereço novo |
|---|---|
| `/purchase-order` | `/supplier/purchase-orders` |
| `/purchase-order-detail/<order-number>` | `/supplier/purchase-orders/<order-number>` |
| `/sales_order_detail/<sales-order-id>` | `/sales-orders/<sales-order-id>` |
| `/asn_shipment` | `/shipments/asn` |
| `/asn_shipment/dashboard` | `/shipments/asn` |
| `/shipment-order` | `/shipments/orders` |
| `/invoice/dashboard` | `/invoices` |
| `/invoice/details/<document-id>` | `/invoices/<document-id>` |
| `/accounting_range` | `/accounting/range` |

### Análises e pesquisa

| Endereço antigo | Endereço novo |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Links compartilhados

| Endereço antigo | Endereço novo |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Conta e login

| Endereço antigo | Endereço novo |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Layouts

| Endereço antigo | Endereço novo |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
