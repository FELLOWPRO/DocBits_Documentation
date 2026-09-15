# Herramientas de flujos de trabajo

DocFlow MCP expone herramientas para gestionar y probar flujos de trabajo avanzados, además de herramientas para leer los registros de los flujos de trabajo y gestionar las variables de flujo de trabajo.

{% hint style="info" %}
**Nombres de las herramientas a través de la pasarela DocBits MCP.** Cuando te conectas a través del DocBits MCP unificado (`api.docbits.com/v3/mcp`), todas las herramientas de DocFlow llevan el prefijo `docflow_`: `list_workflows` se llama `docflow_list_workflows`, `run_workflow_with_assertions` es `docflow_run_workflow_with_assertions`. Los parámetros son idénticos. Los nombres de abajo son los nombres de DocFlow sin prefijo.

Los flujos de trabajo se **crean y editan en el diseñador de DocFlow** de la aplicación web. El MCP los lee, prueba, ejecuta y elimina; no crea ni modifica grafos de flujos de trabajo.
{% endhint %} Las herramientas del SDK de tarjetas tienen su propia página; consulta [Herramientas del SDK de Tarjetas](card-sdk-tools.md).

## list\_workflows

Listar todos los flujos de trabajo de la organización actual.

**Parámetros:** Ninguno

**Ejemplo de respuesta:**

```json
[
  {
    "id": "a1b2c3d4-...",
    "name": "Invoice Approval",
    "version": 3,
    "enabled": true,
    "doc_types": ["INVOICE"],
    "workflow_type": "advanced",
    "created_on": "2025-01-15 10:30:00",
    "last_modified_on": "2025-03-20 14:22:00"
  }
]
```

## get\_workflow

Obtener detalles de un flujo de trabajo específico, incluyendo su estructura de nodos y aristas.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo |

**Ejemplo de respuesta:**

```json
{
  "id": "a1b2c3d4-...",
  "name": "Invoice Approval",
  "version": 3,
  "enabled": true,
  "doc_types": ["INVOICE"],
  "workflow_type": "advanced",
  "description": "Routes invoices based on amount",
  "advanced_config": {
    "nodes": [
      {"node_id": "when-1", "node_type": "when", "label": "Amount > 1000"},
      {"node_id": "then-1", "node_type": "then", "label": "Send for Approval"}
    ],
    "edges": [
      {"source_node_id": "when-1", "target_node_id": "then-1"}
    ]
  }
}
```

## delete\_workflow

Eliminar un flujo de trabajo por ID (eliminación lógica).

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo a eliminar |

**Ejemplo de respuesta:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Probar la ejecución de un flujo de trabajo avanzado. Opcionalmente proporciona un ID de documento para probar con un documento real.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo avanzado |
| `doc_id` | string | No | UUID de un documento para probar |

**Ejemplo de respuesta:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-...",
  "execution_time": 0.234,
  "workflow_result": "completed",
  "node_results": {
    "when-1": {"status": "success", "output": true},
    "then-1": {"status": "success"}
  },
  "logs": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "status": "success",
      "error": null,
      "duration_ms": 12
    }
  ]
}
```

## list\_test\_scenarios

Listar todos los escenarios de prueba de flujos de trabajo de la organización.

**Parámetros:** Ninguno

**Ejemplo de respuesta:**

```json
[
  {
    "id": "scenario-uuid",
    "name": "Invoice over 1000 EUR",
    "workflow_id": "a1b2c3d4-...",
    "enabled": true,
    "status": "passed",
    "last_run": "2025-03-20 14:00:00"
  }
]
```

## list\_cards

Listar todas las tarjetas de flujo de trabajo disponibles con sus condiciones y configuración.

**Parámetros:** Ninguno

**Ejemplo de respuesta:**

```json
[
  {
    "id": "card-uuid",
    "text": "Document Type Is",
    "card_type": "document_type_is",
    "card_version": 1,
    "category": "Document",
    "when_condition": true,
    "and_condition": false,
    "then_condition": false
  },
  {
    "id": "card-uuid-2",
    "text": "Send Email Notification",
    "card_type": "send_email",
    "card_version": 1,
    "category": "Communication",
    "when_condition": false,
    "and_condition": false,
    "then_condition": true
  }
]
```

{% hint style="info" %}
Las tarjetas tienen indicadores de rol: `when_condition` (disparador), `and_condition` (condición adicional) y `then_condition` (acción). Utiliza estos indicadores para determinar en qué tipos de nodo se puede usar una tarjeta.
{% endhint %}

## list\_workflow\_variables

Listar todas las variables de flujo de trabajo de la organización con su nombre, tipo y valor actual.

**Parámetros:** Ninguno

## set\_workflow\_variable

Crear una variable de flujo de trabajo o actualizar su valor. Las variables de tipo documento no tienen valor propio; las establece el flujo de trabajo en tiempo de ejecución.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `name` | string | Sí | Nombre de la variable |
| `value` | string | No | Nuevo valor |
| `var_type` | string | No | Tipo de la variable al crearla (por ejemplo `string`, `number`, `document`) |

## search\_workflow\_logs

Buscar en los registros de ejecución de flujos de trabajo para averiguar por qué las ejecuciones fallaron, tuvieron éxito o no cumplieron una condición.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | No | Limitar a un flujo de trabajo |
| `doc_id` | string | No | Limitar a las ejecuciones de un documento |
| `status` | string | No | Estado de ejecución por el que filtrar |
| `keyword` | string | No | Filtro de texto libre sobre el registro |
| `include_workflow_data` | boolean | No | Incluir la instantánea de la definición del flujo de trabajo por ejecución |
| `limit` / `offset` | integer | No | Paginación |

## get\_workflow\_log\_detail

Detalle completo de una ejecución: los registros en bruto de la ejecución de las tarjetas y la definición del flujo de trabajo tal como estaba en el momento de la ejecución.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `log_id` | string | Sí | ID de la entrada de registro obtenido de `search_workflow_logs` |

## run\_workflow\_with\_assertions

Inicializar variables de flujo de trabajo, ejecutar un flujo de trabajo avanzado con el ejecutor real y comprobar el resultado contra la base de datos. Las variables son escrituras reales, no simulaciones; úsalo para hacer pruebas de integración de un flujo de trabajo desde un asistente.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo a ejecutar |
| `doc_id` | string | No | Documento sobre el que ejecutar el flujo de trabajo |
| `seed_variables` | array | No | Variables que se crean o actualizan antes de la ejecución; las variables de tipo documento pueden apuntar a un `doc_id` mediante `value` |
