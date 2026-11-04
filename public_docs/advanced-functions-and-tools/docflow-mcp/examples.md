# Ejemplos

Ejemplos completos de principio a fin que muestran cómo usar las herramientas de DocFlow MCP en conjunto.

## Ejemplo 1: Crear una tarjeta personalizada y usarla en un flujo de trabajo

Este ejemplo recorre el ciclo de vida completo: crear una tarjeta de socio, validarla, probarla, aprobarla y construir un flujo de trabajo que la utilice.

### Paso 1: Crear la tarjeta

Llama a `sdk_create_card`:

```json
{
  "app_manifest": {
    "id": "com.example.invoice-tools",
    "name": "Invoice Tools",
    "version": "1.0.0",
    "partner": {
      "id": "example-partner",
      "name": "Example Corp"
    }
  },
  "card_manifest": {
    "id": "high-value-check",
    "title": {"en": "High Value Invoice Check"},
    "entry_point": "src/high_value.py",
    "class_name": "HighValueCheck",
    "args": [
      {
        "id": "threshold",
        "title": {"en": "Amount Threshold"},
        "type": "number",
        "required": true
      }
    ]
  },
  "card_type": "condition",
  "source_code": "from api.sdk.base import PartnerCard\nfrom api.sdk.result import CardResult, CardStatus\n\nclass HighValueCheck(PartnerCard):\n    def execute(self, context):\n        threshold = float(self.variables.get('threshold', 1000))\n        total = float(context.document_fields.get('total_amount', 0))\n        if total > threshold:\n            return CardResult(status=CardStatus.SUCCESS, message=f'High value: {total}')\n        return CardResult(status=CardStatus.FAILURE, message=f'Below threshold: {total}')",
  "test_code": "def test_high_value():\n    assert True  # Basic test"
}
```

Anota el `card_id` de la respuesta; lo necesitarás en los pasos siguientes.

### Paso 2: Validar la tarjeta

Llama a `sdk_validate_card` con el ID de la tarjeta:

```json
{
  "card_id": "returned-card-uuid"
}
```

Revisa el informe de validación. Las 5 etapas deberían pasar.

### Paso 3: Probar la tarjeta

Llama a `sdk_test_card` con un contexto de documento simulado:

```json
{
  "card_id": "returned-card-uuid",
  "variables": {"threshold": "1000"},
  "mock_context": {
    "document_type": "INVOICE",
    "document_fields": {
      "total_amount": "2500.00",
      "currency": "EUR"
    }
  }
}
```

Verifica que la respuesta muestre `CardStatus.SUCCESS`.

### Paso 4: Aprobar la tarjeta

Llama a `sdk_approve_card` (requiere administrador):

```json
{
  "card_id": "returned-card-uuid"
}
```

La tarjeta ahora está activa y disponible para su uso en flujos de trabajo.

### Paso 5: Construir un flujo de trabajo con la tarjeta

Abre el **diseñador de DocFlow** en la aplicación web, crea un flujo de trabajo avanzado y añade la tarjeta aprobada como nodo, por ejemplo un disparador *Document Received*, la tarjeta *High Value Check* y un nodo *Approval* para la rama `true`. Los grafos de flujos de trabajo se crean y editan en el diseñador; el MCP no los crea.

De vuelta en el asistente, confirma que el flujo de trabajo existe y lee su estructura:

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id from list_workflows>"
}
```

### Paso 6: Probar el flujo de trabajo

Llama a `test_advanced_workflow`:

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Revisa los registros de ejecución para verificar que cada nodo se ejecutó correctamente.

---

## Ejemplo 2: Construir un flujo de trabajo con tarjetas integradas

Este ejemplo crea un flujo de trabajo usando solo tarjetas integradas (no se necesitan tarjetas personalizadas).

### Paso 1: Descubrir las tarjetas disponibles

Llama a `sdk_list_cards_picker` para ver todas las tarjetas disponibles con sus indicadores de rol:

```json
// Response includes cards like:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

Filtra por rol:
- `is_when: true` — Usar en nodos WHEN (disparadores)
- `is_and: true` — Usar en nodos AND (condiciones adicionales)
- `is_then: true` — Usar en nodos THEN (acciones)

### Paso 2: Crear el flujo de trabajo

```json
{
  "name": "Invoice Document Type Router",
  "description": "When document is an invoice, apply validation",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 250, "y": 50},
      "label": "Document is Invoice",
      "card": {
        "id": "doc-type-card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "and-1",
      "node_type": "and",
      "position": {"x": 250, "y": 200},
      "label": "Amount > 1000",
      "card": {
        "id": "amount-card-uuid",
        "card_type": "field_value_check",
        "version": 1,
        "variables": [
          {"id": "field-var", "data": "total_amount", "data_type": "string"},
          {"id": "op-var", "data": ">", "data_type": "string"},
          {"id": "val-var", "data": "1000", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 250, "y": 350},
      "label": "Set Status to Review",
      "card": {
        "id": "status-card-uuid",
        "card_type": "set_document_status",
        "version": 1,
        "variables": [
          {"id": "status-var", "data": "review", "data_type": "string"}
        ]
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "and-1",
      "source_handle": "success",
      "target_handle": "input"
    },
    {
      "edge_id": "e2",
      "source_node_id": "and-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

Esto crea un flujo de trabajo: **WHEN** el documento es una factura **AND** el monto > 1000 **THEN** establecer el estado a revisión.

---

## Ejemplo 3: Importar tarjetas desde GitHub

Si tus tarjetas de socios están en un repositorio de GitHub, puedes importarlas directamente:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Para repositorios privados, incluye un token de GitHub:

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Después de la importación, las tarjetas pasan por la validación automáticamente. Verifica su estado con `sdk_list_submissions` y apruébalas con `sdk_approve_card`.
