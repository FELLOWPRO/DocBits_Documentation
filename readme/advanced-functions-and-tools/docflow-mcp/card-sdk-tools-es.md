# Herramientas del Card SDK

Las herramientas del Card SDK te permiten crear, validar, probar y gestionar tarjetas de socios personalizadas a través de MCP. Las tarjetas de socios extienden DocFlow con lógica de negocio personalizada escrita en Python.

## Ciclo de vida de una tarjeta

Una tarjeta de socio pasa por los siguientes estados de envío (`partner_status`):

| Estado | Significado | Visibilidad en los flujos |
|-------|---------|---------------------|
| `validating` | Envío aceptado; la pipeline de validación está en ejecución. | Solo la organización remitente |
| `validated` | Todas las etapas de validación pasaron. A la espera de aprobación del admin. | Solo la organización remitente |
| `rejected` | Validación fallida o un admin rechazó la tarjeta. El código fuente se conserva para inspección. | Solo la organización remitente |
| `approved` | Un admin aprobó la tarjeta; `enabled = true`. | **Todas las organizaciones** |
| `disabled` | Tarjeta previamente aprobada que un admin desactivó. | Solo la organización remitente |
| `deleted` | Eliminada suavemente; no se devuelve en los listados de envíos. | Oculta |

{% hint style="warning" %}
**Visibilidad entre organizaciones:** Una tarjeta de socio solo está disponible para los nodos de flujo de trabajo en `list_cards` una vez que ha sido **aprobada**. Las tarjetas de socio aprobadas son visibles para todas las organizaciones de la plataforma — la aprobación es una activación global, no una activación por organización. Las tarjetas no aprobadas (validating, validated, rejected, disabled) solo son visibles para la organización que las envió.
{% endhint %}

Flujo típico:

1. **Crear** una tarjeta con `sdk_create_card` o `sdk_import_github` — ejecuta la pipeline de validación y almacena la tarjeta con `partner_status = validated` (o `rejected` si falla).
2. **Validar** con `sdk_validate_card` para volver a comprobar una tarjeta existente o ejecutar en seco un nuevo código fuente sin persistirlo.
3. **Probar** con `sdk_test_card` para ejecutar la tarjeta en el entorno aislado contra un contexto ficticio.
4. **Aprobar** con `sdk_approve_card` (solo admin de la organización) — vuelve a ejecutar las validaciones AST y de comportamiento, luego establece `partner_status = approved` y `enabled = true`.
5. Una vez aprobada, la tarjeta aparece en `list_cards` para cada organización y puede referenciarse desde los nodos de flujo de trabajo.

## Herramientas de desarrollo

### sdk\_create\_card

Crear una nueva tarjeta de socio a partir de código fuente y manifiestos. Ejecuta la pipeline de validación completa (consulta [Etapas de validación](#sdk_validate_card) más abajo) y almacena la tarjeta en la base de datos. La tarjeta queda en estado `validated` y requiere la aprobación de un admin antes de poder usarse en los flujos de trabajo.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `app_manifest` | object | Sí | Manifiesto de la aplicación con id, name, version, info del socio |
| `card_manifest` | object | Sí | Manifiesto de la tarjeta con id, title, entry\_point, class\_name, args |
| `card_type` | string | Sí | `action` o `condition` |
| `source_code` | string | Sí | Código fuente en Python (debe extender `PartnerCard`) |
| `test_code` | string | Sí | Código de pruebas Pytest para la tarjeta |
| `locales` | object | No | Traducciones de idiomas, ej. `{"en": {...}, "de": {...}}` |

**Ejemplo de manifiesto de aplicación:**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Ejemplo de manifiesto de tarjeta:**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Ejemplo de código fuente:**

```python
from api.sdk.base import PartnerCard
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` tiene tres valores que se mapean directamente sobre las aristas del flujo de trabajo:

| Estado | Arista tomada | Para qué usarlo |
|--------|------------|------------|
| `SUCCESS` | `success` | La tarjeta tuvo éxito — aplica tanto a condiciones como a acciones. |
| `FAILED` | `failed_condition` | **Solo tarjetas de condición.** La condición se evaluó como false — el flujo toma la rama "else". Las tarjetas de acción no tienen handle `failed_condition`, así que devolver `FAILED` desde una acción deja la ejecución sin salida. |
| `ERROR` | `error` | Un fallo inesperado en tiempo de ejecución (excepción). Aplica tanto a condiciones como a acciones. |

En resumen: las acciones devuelven `SUCCESS` o `ERROR`; las condiciones pueden además devolver `FAILED`.
{% endhint %}

### sdk\_validate\_card

Ejecutar la pipeline de validación sobre una tarjeta de socio sin guardarla. Dos modos:

- **Modo A** — Validar una tarjeta existente por ID
- **Modo B** — Validar nuevo código fuente en modo inline

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID de una tarjeta existente (Modo A) |
| `app_manifest` | object | No | Manifiesto de la aplicación (Modo B) |
| `card_manifest` | object | No | Manifiesto de la tarjeta (Modo B) |
| `card_type` | string | No | `action` o `condition` (Modo B) |
| `source_code` | string | No | Código fuente en Python (Modo B) |
| `test_code` | string | No | Código de pruebas (Modo B) |

{% hint style="info" %}
Proporciona `card_id` solo (Modo A) o `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de validación:**

1. **Structure** — Verifica la disposición de archivos, el esquema del manifiesto (`app.json`, `.docflowcompose/flow/...`) y que los entry points declarados existen.
2. **Locales** — Concilia las claves de traducción usadas en la tarjeta con los archivos `locales/<lang>.json`; falla si una clave falta en un idioma declarado.
3. **AST Analysis** — Recorre cada archivo `.py` bajo `src/` y comprueba los imports prohibidos, las llamadas peligrosas y los requisitos de jerarquía de clases / firma de métodos.
4. **Dependencies** — Valida que todos los imports se resuelvan a módulos permitidos de la lista blanca del SDK.
5. **Tests** — Ejecuta la suite pytest de la tarjeta bajo rlimits reducidos.
6. **Behavioral** — Ejecuta la tarjeta en el entorno aislado de producción contra un contexto ficticio mínimo para confirmar el comportamiento en ejecución.

Las etapas se ejecutan en orden; la primera que falla cortocircuita las demás. La etapa 6 (Behavioral) también se vuelve a ejecutar en el momento de la aprobación como comprobación de defensa en profundidad antes de activar la tarjeta.

### sdk\_test\_card

Ejecutar una tarjeta de socio en un entorno aislado con un contexto ficticio. El entorno aislado aplica builtins restringidos, una lista blanca curada de imports, un timeout de ejecución y límites reducidos de recursos del proceso — las mismas restricciones bajo las que se ejecuta una tarjeta una vez aprobada.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | No | UUID de una tarjeta existente (Modo A) |
| `source_code` | string | No | Código fuente para pruebas inline (Modo B) |
| `class_name` | string | No | Nombre de la clase para pruebas inline (Modo B) |
| `variables` | object | No | Variables a pasar al constructor de la tarjeta |
| `mock_context` | object | No | Contexto de ejecución ficticio |

**Campos del mock context:**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

La herramienta devuelve `execution_success` (indica si el entorno aislado ejecutó la tarjeta hasta el final — un timeout, una violación de import o una excepción lanzada lo ponen a `false`), `card_status` (el `CardStatus` devuelto por `execute()` mismo), el `message` y `data` de la tarjeta, los `logs` capturados y `execution_time_ms`.

### sdk\_import\_github

Importar una aplicación de socio desde un repositorio de GitHub. Clona el repositorio, lee `app.json` e importa todas las tarjetas encontradas en el directorio `.docflowcompose`.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `github_url` | string | Sí | URL HTTPS de GitHub (ej. `https://github.com/org/repo`) |
| `branch` | string | No | Rama a clonar (por defecto: `main`) |
| `token` | string | No | Token de GitHub para repositorios privados |

**Estructura esperada del repositorio:**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

## Herramientas de gestión

### sdk\_list\_submissions

Listar todos los envíos de tarjetas de socios para la organización actual.

**Parámetros:** Ninguno

### sdk\_get\_submission\_status

Obtener el estado de validación y el informe de un envío específico de tarjeta de socio.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

### sdk\_approve\_card

Aprobar una tarjeta de socio validada y activarla. La aprobación vuelve a ejecutar las validaciones AST y de comportamiento como comprobación de defensa en profundidad, establece `partner_status = approved` y `enabled = true`, y registra la tarjeta en el registro de tiempo de ejecución. Una vez aprobada, la tarjeta aparece en `list_cards` para **todas las organizaciones**, no solo para la remitente.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de admin de la organización. La tarjeta debe estar en estado `validated`. Las tarjetas rechazadas deben volver a subirse y validarse antes de poder ser aprobadas.
{% endhint %}

### sdk\_reject\_card

Rechazar un envío de tarjeta de socio y desactivarlo.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |
| `reason` | string | No | Motivo del rechazo |

{% hint style="warning" %}
Requiere permisos de admin de la organización.
{% endhint %}

### sdk\_delete\_submission

Eliminar suavemente un envío de tarjeta de socio, sin importar su estado actual. Establece `partner_status = deleted`, `enabled = false` y `deprecated = true`. La fila se conserva con fines de auditoría, pero se oculta de los listados de envíos y de `list_cards`.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|----------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de admin de la organización.
{% endhint %}

### sdk\_list\_cards\_picker

Listar todas las tarjetas habilitadas y no obsoletas con sus banderas de rol. Útil para determinar qué tarjetas pueden usarse en qué tipos de nodo al construir flujos de trabajo.

**Parámetros:** Ninguno

## Capacidades actuales y hoja de ruta

El Partner Card SDK se está implantando de forma incremental. Esto es lo que tu tarjeta puede usar hoy y lo que aún se está conectando:

| Capacidad | Estado |
|------------|--------|
| **Condiciones sobre campos** — leer los campos de documento desde `context.document_fields` y ramificar según sus valores en las tarjetas de condición | ✅ Implementado |
| **Solicitudes HTTP salientes** — llamar a servicios externos desde dentro de una tarjeta | 🚧 En proceso de adición |
| **Información extendida del documento** — metadatos adicionales del documento (más allá de `document_id`, `document_type` y `document_fields`) expuestos en `ExecutionContext` | 🚧 En proceso de adición |
| **Ayudantes de consulta a tablas de base de datos** — ayudantes integrados para leer desde las tablas de datos maestros / de consulta de DocBits dentro de una tarjeta | 📅 Planificado para 1.1 |
| **Visor del código fuente de la tarjeta de socio** — vista de solo lectura del código de la tarjeta de socio enviada en la interfaz de DocBits, para que los admins puedan inspeccionar lo que están aprobando | 📅 Planificado para 1.1 |

{% hint style="info" %}
Si tu tarjeta necesita una capacidad que aún está en progreso, fallará en la validación (import prohibido, atributo de contexto inexistente o restricción del entorno aislado) hasta que la pieza correspondiente esté disponible. Esta página se actualizará a medida que se entregue cada capacidad.
{% endhint %}

{% hint style="danger" %}
**Las tarjetas de socios ejecutan código de terceros — uso bajo tu propia responsabilidad.**

Las tarjetas subidas a través del Partner Card SDK solo están **parcialmente validadas por DocBits**. La pipeline de validación comprueba estructura, locales, imports, patrones AST, dependencias, las propias pruebas de la tarjeta y una ejecución de comportamiento tipo smoke en el entorno aislado — **no** constituye una auditoría completa de seguridad ni una garantía funcional de la lógica de negocio de la tarjeta.

Una vez que un admin de la organización aprueba una tarjeta de socio, esta queda disponible para todas las organizaciones de la plataforma y se ejecuta en el entorno aislado de producción contra documentos reales. Aprobar y habilitar una tarjeta de socio es, por tanto, una decisión explícita de confianza por parte del admin que la aprueba. DocBits no acepta ninguna responsabilidad por pérdida de datos, enrutamiento incorrecto, filtración de información o cualquier otro resultado causado por una tarjeta de socio que decidas instalar o aprobar.

Si no eres el autor original de la tarjeta, revisa el código fuente (y, una vez se entregue la 1.1, utiliza el visor del código fuente de tarjeta de socio) antes de aprobarla.
{% endhint %}
