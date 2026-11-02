# Workflow Tools

DocFlow MCP expone herramientas para gestionar y probar flujos de trabajo avanzados, además de herramientas para leer los registros de los flujos de trabajo y gestionar las variables de flujo de trabajo.

{% hint style="info" %}
**Nombres de las herramientas a través de la pasarela DocBits MCP.** Cuando se conecta a través del DocBits MCP unificado (`api.docbits.com/v3/mcp`), todas las herramientas de DocFlow llevan el prefijo `docflow_`: `list_workflows` se llama `docflow_list_workflows`, `run_workflow_with_assertions` es `docflow_run_workflow_with_assertions`. Los parámetros son idénticos. Los nombres que figuran a continuación son los nombres de DocFlow sin prefijo.

Los flujos de trabajo se **crean y editan en el diseñador de DocFlow** de la aplicación web. El MCP los lee, los prueba, los ejecuta y los elimina; no crea ni modifica grafos de flujos de trabajo.
{% endhint %} Las herramientas del Card SDK tienen su propia página, consulte [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Lista todos los flujos de trabajo de la organización actual.

**Parámetros:** ninguno

## get\_workflow

Obtiene los detalles de un flujo de trabajo concreto, incluida la estructura de sus nodos y aristas.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo |

## delete\_workflow

Elimina un flujo de trabajo por ID (eliminación lógica).

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo que se va a eliminar |

## test\_advanced\_workflow

Prueba la ejecución de un flujo de trabajo avanzado. Opcionalmente, indique un ID de documento para probarlo con un documento real.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo avanzado |
| `doc_id` | string | No | UUID de un documento con el que probar |

## list\_test\_scenarios

Lista todos los escenarios de prueba de flujos de trabajo de la organización.

**Parámetros:** ninguno

## list\_cards

Lista todas las tarjetas de flujo de trabajo disponibles con sus condiciones y su configuración.

**Parámetros:** ninguno

{% hint style="info" %}
Las tarjetas tienen indicadores de rol: `when_condition` (disparador), `and_condition` (condición adicional) y `then_condition` (acción). Utilícelos para determinar en qué tipos de nodo se puede usar una tarjeta.
{% endhint %}

## list\_workflow\_variables

Lista todas las variables de flujo de trabajo de la organización con su nombre, tipo y valor actual.

**Parámetros:** ninguno

## set\_workflow\_variable

Crea una variable de flujo de trabajo o actualiza su valor. Las variables de tipo documento no tienen un valor propio; las establece el flujo de trabajo en tiempo de ejecución.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `name` | string | Sí | Nombre de la variable |
| `value` | string | No | Nuevo valor |
| `var_type` | string | No | Tipo de variable al crearla (por ejemplo `string`, `number`, `document`) |

## search\_workflow\_logs

Busca en los registros de ejecución de flujos de trabajo para averiguar por qué las ejecuciones fallaron, se completaron con éxito o no cumplieron una condición.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | string | No | Limita la búsqueda a un flujo de trabajo |
| `doc_id` | string | No | Limita la búsqueda a las ejecuciones de un documento |
| `status` | string | No | Estado de ejecución por el que filtrar |
| `keyword` | string | No | Filtro de texto libre sobre el registro |
| `include_workflow_data` | boolean | No | Incluye la instantánea de la definición del flujo de trabajo de cada ejecución |
| `limit` / `offset` | integer | No | Paginación |

## get\_workflow\_log\_detail

Detalle completo de una ejecución: los registros en bruto de la ejecución de las tarjetas y la definición del flujo de trabajo tal como estaba en el momento de la ejecución.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `log_id` | string | Sí | ID de la entrada de registro obtenida de `search_workflow_logs` |

## run\_workflow\_with\_assertions

Inicializa variables de flujo de trabajo, ejecuta un flujo de trabajo avanzado con el ejecutor real y comprueba el resultado contra la base de datos. Las variables son escrituras reales, no simulaciones; utilícelo para probar la integración de un flujo de trabajo desde un asistente.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Sí | UUID del flujo de trabajo que se va a ejecutar |
| `doc_id` | string | No | Documento sobre el que se ejecuta el flujo de trabajo |
| `seed_variables` | array | No | Variables que se crean o actualizan antes de la ejecución; las variables de tipo documento pueden apuntar a un `doc_id` mediante `value` |
