# Herramientas del Card SDK

Las herramientas del Card SDK le permiten crear, validar, probar y gestionar tarjetas de socio personalizadas a través de MCP. Las tarjetas de socio amplían DocFlow con lógica de negocio personalizada escrita en Python.

## Ciclo de vida de una tarjeta

Una tarjeta de socio pasa por los siguientes estados de envío (`partner_status`):

| Estado | Significado | Visibilidad en flujos de trabajo |
|-------|---------|---------------------|
| `validating` | Envío aceptado; la canalización de validación se está ejecutando. | Solo la organización que lo envía |
| `validated` | Se han superado todas las etapas de validación. A la espera de la aprobación de un administrador. | Solo la organización que lo envía |
| `rejected` | La validación falló o un administrador rechazó la tarjeta. El código fuente se conserva para su inspección. | Solo la organización que lo envía |
| `approved` | Un administrador aprobó la tarjeta; `enabled = true`. | **Todas las organizaciones** |
| `disabled` | Tarjeta aprobada anteriormente que un administrador desactivó. | Solo la organización que lo envía |
| `deleted` | Eliminada de forma lógica; no se devuelve en los listados de envíos. | Oculta |

{% hint style="warning" %}
**Visibilidad por organización:** una tarjeta de socio solo está disponible para los nodos de flujo de trabajo en `list_cards` una vez que ha sido **aprobada**. Las tarjetas de socio aprobadas son visibles para todas las organizaciones de la plataforma: la aprobación es una activación global, no una activación por organización. Las tarjetas no aprobadas (validating, validated, rejected, disabled) solo son visibles para la organización que las envió.
{% endhint %}

Flujo habitual:

1. **Cree** una tarjeta con `sdk_create_card` o `sdk_import_github`: se ejecuta la canalización de validación y la tarjeta se almacena con `partner_status = validated` (o `rejected` si falla).
2. **Valide** con `sdk_validate_card` para volver a comprobar una tarjeta existente o para hacer una ejecución de prueba de código fuente nuevo sin guardarlo.
3. **Pruebe** con `sdk_test_card` para ejecutar la tarjeta en el sandbox con un contexto simulado.
4. **Apruebe** con `sdk_approve_card` (solo administrador de la organización): se vuelven a ejecutar la validación AST y la de comportamiento, y después se establece `partner_status = approved` y `enabled = true`.
5. Una vez aprobada, la tarjeta aparece en `list_cards` para todas las organizaciones y se puede referenciar desde los nodos de flujo de trabajo.

## Herramientas de desarrollo

### sdk\_create\_card

Crea una nueva tarjeta de socio a partir del código fuente y los manifiestos. Ejecuta la canalización de validación completa (consulte [Etapas de validación](#sdk_validate_card) más abajo) y almacena la tarjeta en la base de datos. La tarjeta queda en estado `validated` y requiere la aprobación de un administrador antes de poder usarse en flujos de trabajo.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `app_manifest` | object | Sí | Manifiesto de la aplicación con id, name, version e información del socio |
| `card_manifest` | object | Sí | Manifiesto de la tarjeta con id, title, entry\_point, class\_name, args |
| `card_type` | string | Sí | `action` o `condition` |
| `source_code` | string | Sí | Código fuente en Python (debe extender `PartnerCard`) |
| `test_code` | string | Sí | Código de pruebas Pytest de la tarjeta |
| `locales` | object | No | Traducciones de idioma, p. ej. `{"en": {...}, "de": {...}}` |

**Ejemplo de manifiesto de la aplicación:**

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

**Ejemplo de manifiesto de la tarjeta:**

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
`CardStatus` tiene tres valores y se corresponden directamente con las aristas del flujo de trabajo:

| Estado | Arista que se toma | Úselo para |
|--------|------------|------------|
| `SUCCESS` | `success` | La tarjeta tuvo éxito; se aplica tanto a condiciones como a acciones. |
| `FAILED` | `failed_condition` | **Solo tarjetas de condición.** La condición se evaluó como falsa; el flujo de trabajo toma la rama "else". Las tarjetas de acción no tienen un punto de conexión `failed_condition`, por lo que devolver `FAILED` desde una acción deja la ejecución sin ningún camino a seguir. |
| `ERROR` | `error` | Un fallo inesperado en tiempo de ejecución (excepción). Se aplica tanto a condiciones como a acciones. |

En resumen: las acciones devuelven `SUCCESS` o `ERROR`; las condiciones pueden devolver además `FAILED`.
{% endhint %}

### sdk\_validate\_card

Ejecuta la canalización de validación sobre una tarjeta de socio sin guardarla. Dos modos:

- **Modo A**: validar una tarjeta existente por ID
- **Modo B**: validar código fuente nuevo en línea

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | No | UUID de la tarjeta existente (Modo A) |
| `app_manifest` | object | No | Manifiesto de la aplicación (Modo B) |
| `card_manifest` | object | No | Manifiesto de la tarjeta (Modo B) |
| `card_type` | string | No | `action` o `condition` (Modo B) |
| `source_code` | string | No | Código fuente en Python (Modo B) |
| `test_code` | string | No | Código de pruebas (Modo B) |

{% hint style="info" %}
Indique únicamente `card_id` (Modo A) o `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de validación:**

1. **Estructura**: verifica la disposición de los archivos, el esquema del manifiesto (`app.json`, `.docflowcompose/flow/...`) y que existan los puntos de entrada declarados.
2. **Locales**: concilia las claves de traducción usadas en la tarjeta con los archivos `locales/<lang>.json`; falla si falta una clave en algún idioma declarado.
3. **Análisis AST**: recorre todos los archivos `.py` de `src/` y comprueba que no haya importaciones prohibidas ni llamadas peligrosas, y que se cumplan los requisitos de jerarquía de clases y de firma de métodos.
4. **Dependencias**: valida que todas las importaciones se resuelvan en módulos permitidos de la lista blanca del SDK.
5. **Pruebas**: ejecuta el conjunto de pruebas pytest de la tarjeta con límites de recursos (rlimits) reducidos.
6. **Comportamiento**: ejecuta la tarjeta en el sandbox de producción con un contexto simulado mínimo para confirmar su comportamiento en tiempo de ejecución.

Las etapas se ejecutan en orden; la primera que falla interrumpe las restantes. La etapa 6 (Comportamiento) se vuelve a ejecutar también en el momento de la aprobación, como comprobación de defensa en profundidad antes de activar la tarjeta.

### sdk\_test\_card

Ejecuta una tarjeta de socio en un entorno aislado (sandbox) con un contexto simulado. El sandbox aplica builtins restringidos, una lista blanca de importaciones, un tiempo límite de ejecución y límites reducidos de recursos del proceso: las mismas restricciones bajo las que se ejecuta una tarjeta una vez aprobada.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | No | UUID de la tarjeta existente (Modo A) |
| `source_code` | string | No | Código fuente para pruebas en línea (Modo B) |
| `class_name` | string | No | Nombre de la clase para pruebas en línea (Modo B) |
| `variables` | object | No | Variables que se pasan al constructor de la tarjeta |
| `mock_context` | object | No | Contexto de ejecución simulado |

**Campos del contexto simulado:**

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

La herramienta devuelve `execution_success` (si el sandbox ejecutó la tarjeta hasta el final; un tiempo de espera agotado, una infracción de importación o una excepción lo ponen en `false`), `card_status` (el `CardStatus` devuelto por el propio `execute()`), el `message` y los `data` de la tarjeta, los `logs` capturados y `execution_time_ms`.

### sdk\_import\_github

Importa una aplicación de socio desde un repositorio de GitHub. Clona el repositorio, lee `app.json` e importa todas las tarjetas que encuentra en el directorio `.docflowcompose`.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `github_url` | string | Sí | URL HTTPS de GitHub (p. ej. `https://github.com/org/repo`) |
| `branch` | string | No | Rama que se clona (por defecto: `main`) |
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

Lista todos los envíos de tarjetas de socio de la organización actual.

**Parámetros:** ninguno

### sdk\_get\_submission\_status

Obtiene el estado de validación y el informe de un envío concreto de una tarjeta de socio.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

### sdk\_approve\_card

Aprueba una tarjeta de socio validada y la activa. La aprobación vuelve a ejecutar la validación AST y la de comportamiento como comprobación de defensa en profundidad, establece `partner_status = approved` y `enabled = true`, y registra la tarjeta en el registro de tiempo de ejecución. Una vez aprobada, la tarjeta aparece en `list_cards` para **todas las organizaciones**, no solo para la que la envió.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de administrador de la organización. La tarjeta debe estar en estado `validated`. Las tarjetas rechazadas deben volver a subirse y a validarse antes de poder aprobarse.
{% endhint %}

### sdk\_reject\_card

Rechaza el envío de una tarjeta de socio y la desactiva.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |
| `reason` | string | No | Motivo del rechazo |

{% hint style="warning" %}
Requiere permisos de administrador de la organización.
{% endhint %}

### sdk\_delete\_submission

Elimina de forma lógica el envío de una tarjeta de socio, sea cual sea su estado actual. Establece `partner_status = deleted`, `enabled = false` y `deprecated = true`. La fila se conserva con fines de auditoría, pero se oculta de los listados de envíos y de `list_cards`.

**Parámetros:**

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `card_id` | string | Sí | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de administrador de la organización.
{% endhint %}

### sdk\_list\_cards\_picker

Lista todas las tarjetas habilitadas y no obsoletas con indicadores de rol. Es útil para determinar qué tarjetas se pueden usar en qué tipos de nodo al construir flujos de trabajo.

**Parámetros:** ninguno

## Capacidades actuales y hoja de ruta

El Partner Card SDK se está desplegando de forma incremental. Esto es lo que su tarjeta puede utilizar hoy y lo que todavía se está integrando:

| Capacidad | Estado |
|------------|--------|
| **Condiciones de campo**: leer los campos del documento desde `context.document_fields` y bifurcar según sus valores dentro de las tarjetas de condición | ✅ Implementado |
| **Solicitudes HTTP salientes**: llamar a servicios externos desde dentro de una tarjeta | 🚧 En proceso de incorporación |
| **Información ampliada del documento**: metadatos adicionales del documento (más allá de `document_id`, `document_type` y `document_fields`) expuestos en `ExecutionContext` | 🚧 En proceso de incorporación |
| **Ayudas de búsqueda en tablas de base de datos**: ayudas integradas para leer de las tablas de datos maestros / de búsqueda de DocBits desde una tarjeta | 📅 Previsto para la 1.1 |
| **Visor del código fuente de la tarjeta de socio**: vista de solo lectura del código de la tarjeta de socio enviada en la interfaz de DocBits, para que los administradores puedan inspeccionar lo que aprueban | 📅 Previsto para la 1.1 |

{% hint style="info" %}
Si su tarjeta necesita una capacidad que todavía está en desarrollo, no superará la validación (importación prohibida, atributo de contexto ausente o restricción del sandbox) hasta que llegue la pieza correspondiente. Esta página se actualizará a medida que se publique cada capacidad.
{% endhint %}

{% hint style="danger" %}
**Las tarjetas de socio ejecutan código de terceros: úselas bajo su propia responsabilidad.**

Las tarjetas subidas a través del Partner Card SDK solo están **parcialmente validadas por DocBits**. La canalización de validación comprueba la estructura, los locales, las importaciones, los patrones AST, las dependencias, las pruebas propias de la tarjeta y una ejecución de humo de comportamiento en el sandbox; **no** constituye una auditoría de seguridad completa ni una garantía funcional de la lógica de negocio de la tarjeta.

Cuando un administrador de la organización aprueba una tarjeta de socio, esta pasa a estar disponible para todas las organizaciones de la plataforma y se ejecuta en el sandbox de producción con documentos reales. Por lo tanto, aprobar y habilitar una tarjeta de socio es una decisión de confianza explícita por parte del administrador que la aprueba. DocBits no asume ninguna responsabilidad por pérdida de datos, enrutamiento incorrecto, filtración de información ni ningún otro resultado causado por una tarjeta de socio que usted decida instalar o aprobar.

Si usted no es el autor original de la tarjeta, revise el código fuente (y, cuando se publique la 1.1, utilice el visor del código fuente de la tarjeta de socio) antes de aprobarla.
{% endhint %}
