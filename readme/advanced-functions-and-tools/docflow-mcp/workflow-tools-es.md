# Herramientas de flujos de trabajo

DocFlow MCP expone herramientas para gestionar y probar flujos de trabajo avanzados, además de herramientas para leer los registros de los flujos de trabajo y gestionar las variables de los flujos de trabajo. Las herramientas del Card SDK tienen su propia página — consulta [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Listar todos los flujos de trabajo de la organización actual.

**Parámetros:** Ninguno

## get\_workflow

Obtener los detalles de un flujo de trabajo específico, incluyendo su estructura de nodos y aristas.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo |

## create\_advanced\_workflow

Crear un nuevo flujo de trabajo avanzado con nodos y aristas.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `name` | string | Sí | Nombre del flujo de trabajo (3-126 caracteres) |
| `description` | string | No | Descripción opcional |
| `nodes` | array | Sí | Array de nodos del flujo de trabajo |
| `edges` | array | Sí | Array de aristas que conectan los nodos |

### Estructura de los nodos

Cada nodo requiere:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `node_id` | string | Identificador único del nodo |
| `node_type` | string | Ver los tipos de nodo abajo |
| `position` | object | `{x: number, y: number}` posición en el lienzo |
| `label` | string | Etiqueta de visualización |
| `card` | object | Configuración de la tarjeta (obligatoria para `when`, `and`, `then` — ver abajo) |

**Tipos de nodo:**

| Tipo | Tarjeta requerida | Propósito |
|------|------------------|---------|
| `start` | Sin tarjeta | Nodo disparador — punto de entrada del flujo de trabajo |
| `when` | Tarjeta de condición | Condición disparadora (también punto de entrada válido) |
| `and` | Tarjeta de condición | Compuerta de condición adicional tras un `when` |
| `or` | Sin tarjeta | Nodo de bifurcación — continúa si alguna rama entrante tiene éxito |
| `then` | Tarjeta de acción | Acción a ejecutar |
| `delay` | Sin tarjeta | Nodo de espera — pausa la ejecución durante una duración configurada |
| `all` | Sin tarjeta | Nodo de fusión — espera todas las ramas entrantes |
| `any` | Sin tarjeta | Nodo de fusión — continúa con la primera rama entrante |
| `note` | Sin tarjeta | Nota adhesiva / anotación; no se ejecuta |

### Estructura de las aristas

Cada arista requiere:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `edge_id` | string | Identificador único de la arista |
| `source_node_id` | string | ID del nodo origen |
| `target_node_id` | string | ID del nodo destino |
| `source_handle` | string | `success`, `error` o `failed_condition` (opcional) |
| `target_handle` | string | `input` (opcional) |

**Handles de origen:**

- `success` — se toma cuando el nodo origen tiene éxito (disponible en cada nodo ejecutable).
- `failed_condition` — se toma cuando una tarjeta de condición `when` o `and` se evalúa como false.
- `error` — se toma cuando un nodo `and` o `then` lanza un error.

### Configuración de la tarjeta

Las tarjetas definen qué hace un nodo. Usa `list_cards` o `sdk_list_cards_picker` para obtener las tarjetas disponibles.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
Solo necesitas proporcionar `id`, `card_type`, `version` y `variables` para cada tarjeta. El servidor enriquece automáticamente las tarjetas con los metadatos de visualización (svg, text, category) desde la base de datos.
{% endhint %}

**Ejemplo de solicitud:**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Actualizar un flujo de trabajo avanzado existente. Puedes actualizar cualquier combinación de nombre, descripción, nodos y aristas.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo a actualizar |
| `name` | string | No | Nuevo nombre |
| `description` | string | No | Nueva descripción |
| `nodes` | array | No | Nuevos nodos (reemplaza todos los nodos existentes) |
| `edges` | array | No | Nuevas aristas (reemplaza todas las aristas existentes) |

## delete\_workflow

Eliminar un flujo de trabajo por ID (eliminación suave).

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo a eliminar |

## test\_advanced\_workflow

Probar la ejecución de un flujo de trabajo avanzado. Opcionalmente proporciona un ID de documento para probar con un documento real.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo avanzado |
| `doc_id` | string | No | UUID de un documento con el que probar |

## list\_test\_scenarios

Listar todos los escenarios de prueba de flujos de trabajo de la organización.

**Parámetros:** Ninguno

## list\_cards

Listar todas las tarjetas de flujo de trabajo disponibles con sus condiciones y configuración.

**Parámetros:** Ninguno

{% hint style="info" %}
Las tarjetas tienen banderas de rol: `when_condition` (disparador), `and_condition` (condición adicional) y `then_condition` (acción). Úsalas para determinar en qué tipos de nodo puede usarse una tarjeta.
{% endhint %}
