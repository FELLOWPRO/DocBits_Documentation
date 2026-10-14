# Búsqueda de texto completo

La búsqueda de texto completo permite a los usuarios buscar en el contenido real de los documentos y en todos los campos extraídos, no solo en los nombres de archivo e IDs.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Diálogo „Fulltext Module Required“ cuando el módulo está desactivado"><figcaption><p>El diálogo «Fulltext Module Required» aparece en las páginas que dependen del módulo.</p></figcaption></figure>

## Sin el módulo

Cuando la búsqueda de texto completo no está activada, la barra de búsqueda del panel solo puede consultar un conjunto reducido de campos estructurados. Las entradas de texto libre se comparan únicamente con:

* `filename`
* `ID` del documento
* `invoice_id`
* `purchase_order`

Cualquier término fuera de estos campos se ignora. No existe búsqueda por contenido ni soporte para rangos, operadores o filtros inteligentes.

## Con el módulo activado

Al activar la búsqueda de texto completo se habilita la búsqueda sobre cada campo extraído de un documento y la barra de búsqueda del panel pasa a aceptar un lenguaje de consulta enriquecido. Las consultas pueden combinar filtros por campo, rangos, operadores lógicos, fechas relativas y filtros inteligentes.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Barra de búsqueda del panel mostrando una consulta por rango y la lista de documentos filtrada"><figcaption><p>La barra de búsqueda del panel acepta el lenguaje de consulta extendido. Escriba una consulta y pulse <kbd>Enter</kbd> para filtrar la lista de documentos.</p></figcaption></figure>

### Consultas por campo

Para buscar en un campo extraído específico, anteponga el nombre del campo seguido de dos puntos. Los nombres de campo siguen la convención de la API (minúsculas, snake\_case) y se aplican a cualquier campo capturado por sus tipos de documento — proveedor, datos de factura, líneas, campos personalizados.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Consultas por rango

Se admiten operadores de comparación en campos numéricos y de fecha. Tanto las comparaciones abiertas como los rangos acotados son válidos.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Operadores lógicos

Combine cláusulas con `AND`, `OR` y `NOT`; agrupe con paréntesis para fijar la precedencia. Las listas `IN` evalúan un campo contra un conjunto de valores posibles.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Fechas relativas

Expresiones temporales que se evalúan en el momento de la consulta. Pueden usarse en cualquier lugar donde se espere una fecha.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Filtros inteligentes

Atajos de un solo término para consultas habituales. Funcionan de forma independiente o como parte de una expresión mayor.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documentos cuya fecha de vencimiento ha pasado.
* `@User` — filtrar por persona asignada; sustituya `User` por el nombre del usuario.
* `#INV-1234` — búsqueda rápida por identificador de documento.
* `$5k+` — importes superiores a 5.000 en la moneda del documento.

## Funciones derivadas

Dos modos de búsqueda especializados se construyen sobre el módulo de texto completo. Ambos requieren que el módulo esté activado y no funcionan de forma independiente.

### Búsqueda vectorial

La búsqueda vectorial encuentra documentos semánticamente similares a la consulta, no solo coincidencias léxicas. El panel interpreta cualquier consulta que empiece con `vector:` como una búsqueda vectorial, la ejecuta sobre los embeddings de los documentos y ordena los resultados por similitud.

```
vector: frozen food invoices
```

La indexación vectorial se controla por separado del índice de texto en la página **Configuración de búsqueda de texto completo**. Al desactivarla se dejan de generar embeddings para los documentos nuevos, pero el índice de texto se mantiene.

### Búsqueda con IA

La búsqueda con IA acepta consultas en lenguaje natural y utiliza un LLM para extraer filtros estructurados, que después se ejecutan contra el índice de texto completo. Anteponga `ai:` a la consulta.

```
ai: invoices from Ruiz over 1000 last quarter
```

La búsqueda con IA y la búsqueda vectorial no son intercambiables: la vectorial encuentra contenido similar; la búsqueda con IA traduce el lenguaje a filtros. La búsqueda con IA no tiene un interruptor propio — se apoya en los índices de texto completo y vectorial existentes.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Página „Configuración de búsqueda de texto completo“ mostrando los subíndices Documents, Vector Index y Fulltext (Text)"><figcaption><p>Configuración de búsqueda de texto completo. El índice vectorial tiene su propio interruptor; el índice de texto se ejecuta siempre que el módulo esté activo.</p></figcaption></figure>

## Requisitos previos

* La infraestructura OpenSearch funciona en segundo plano para alimentar el índice.
* La primera vez que se activa el módulo se reindexan todos los documentos existentes. La duración escala con la cantidad de documentos de la organización.
* Solo los administradores de la organización pueden activar o desactivar módulos.

## Cómo activar el módulo

1. Vaya a **Configuración → Procesamiento de documentos → Módulo**.
2. Bajo el grupo **Dashboards**, active **Full text search**.
3. Confirme el cuadro de diálogo de suscripción si aparece.
4. Espere a que termine la reindexación inicial antes de utilizar consultas de texto completo.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Página „Módulos“ con el interruptor „Full text search“ bajo el grupo Dashboards"><figcaption><p>El interruptor <strong>Full text search</strong> se encuentra en <strong>Módulo → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
El precio del módulo de búsqueda de texto completo se gestiona a través de su contacto comercial de DocBits. La confirmación de suscripción se muestra la primera vez que se activa el módulo.
{% endhint %}

## Véase también

* [Configuración de búsqueda de texto completo](../../log-settings/fulltext-search-settings.md) — gestión del índice e interruptor del índice vectorial.
* [Funciones de Fulltext y Vector Search](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — API de scripting para `fulltext_search()` y `vector_search()`.
* [Resumen de módulos](README.md) — lista completa de los módulos opcionales de DocBits.
