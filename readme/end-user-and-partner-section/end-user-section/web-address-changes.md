# Cambios en las direcciones web

Las direcciones web (URL) que utiliza para acceder a las páginas de DocBits se han depurado y unificado. Esta página explica qué ha cambiado, por qué sus enlaces antiguos siguen funcionando y cómo encontrar cualquier página con su nueva dirección.

## Qué ha cambiado

Las direcciones web de DocBits siguen ahora un patrón claro: primero va el elemento en el que está trabajando y después la vista del mismo. Por ejemplo, la pantalla de validación de un documento es ahora:

```
/documents/<document-id>/validation
```

en lugar de la antigua:

```
/field_validation_v1/<document-id>
```

Con el tiempo, algunas pantallas acabaron teniendo varias versiones y direcciones; por ejemplo, la aprobación tenía direcciones distintas para la primera aprobación, la segunda aprobación y las versiones anteriores de cada una. Ahora comparten una única dirección, y DocBits muestra automáticamente la versión correcta para su organización. Ya no necesita saber ni adivinar qué versión le corresponde.

Además, las direcciones utilizan ahora palabras en minúsculas separadas únicamente por guiones, en lugar de una mezcla de guiones bajos, mayúsculas y abreviaturas.

## Sus enlaces antiguos siguen funcionando

No necesita cambiar nada de inmediato. Los marcadores, los enlaces guardados en correos electrónicos y los enlaces guardados en cualquier otro lugar siguen funcionando exactamente igual que antes. Cuando abre una dirección antigua, DocBits le redirige automáticamente a su nueva dirección, incluidos los filtros u opciones que formaran parte del enlace original.

Después de la redirección, la barra de direcciones del navegador muestra la nueva dirección. Es lo esperado: significa que la redirección ha funcionado. Con el tiempo, le recomendamos actualizar sus marcadores guardados para que apunten directamente a las nuevas direcciones y llegar sin el paso adicional de redirección. Pero no hay ninguna fecha límite: las direcciones antiguas seguirán funcionando.

## Encontrar una página

Si no está seguro de cuál es la nueva dirección de una página, o simplemente quiere ir directamente a algo, hay tres formas de orientarse:

* **Sitemap.** La página [Sitemap](sitemap.md) enumera todas las páginas de DocBits, agrupadas por área, con un cuadro de búsqueda y filtros. Ábrala desde la barra lateral o desde Global Quick Search eligiendo **View all results**.
* **Global Quick Search.** Pulse <kbd>Cmd</kbd> + <kbd>K</kbd> en Mac o <kbd>Ctrl</kbd> + <kbd>K</kbd> en Windows desde cualquier lugar de DocBits y escriba el nombre de lo que busca. Consulte [Global Quick Search](global-quick-search.md) para más detalles.
* **La pantalla de página no encontrada.** Si escribe o pega solo la primera parte de una dirección (por ejemplo, `/documents` o `/analytics`) sin el resto, DocBits muestra una pantalla de página no encontrada con todas las páginas que se encuentran bajo esa dirección. Funciona como un índice de ese grupo de páginas y dispone del mismo cuadro de búsqueda que Global Quick Search, por lo que también puede buscar desde ahí.

## Direcciones antiguas y nuevas

La tabla siguiente enumera todas las direcciones que han cambiado, agrupadas por área. Cuando varias direcciones antiguas conducen ahora a la misma dirección nueva, cada dirección antigua aparece en su propia fila. Las direcciones utilizadas únicamente por desarrolladores (por ejemplo, páginas de depuración o de demostración) no se incluyen, ya que no afectan al uso diario.

Los marcadores de posición de la tabla representan valores reales:

* `<document-id>` — el ID de un documento
* `<task-id>` — el ID de una tarea
* `<workflow-id>` — el ID de un flujo de trabajo
* `<document-type>` — un tipo de documento, como factura u orden de compra
* `<file-name>` — un nombre de archivo
* `<order-number>` / `<sales-order-id>` — una referencia de orden de compra o de venta
* `<organisation-id>` — el ID de una organización
* `<layout-type>` — un tipo de diseño
* `<supplier-id>` — el ID de un proveedor
* `<page>` — un número de página

### Documentos

| Dirección antigua | Dirección nueva |
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

### Tareas

| Dirección antigua | Dirección nueva |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Flujos de trabajo

| Dirección antigua | Dirección nueva |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Pedidos y facturas

| Dirección antigua | Dirección nueva |
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

### Analítica y búsqueda

| Dirección antigua | Dirección nueva |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Enlaces compartidos

| Dirección antigua | Dirección nueva |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Cuenta e inicio de sesión

| Dirección antigua | Dirección nueva |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Diseños

| Dirección antigua | Dirección nueva |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
