# Herramientas del SDK de Tarjetas

Las herramientas del Card SDK te permiten crear, validar, probar y gestionar tarjetas de socios personalizadas a través de MCP. Las tarjetas de socios extienden DocFlow con lógica de negocio personalizada escrita en Python.

## Ciclo de vida de una tarjeta

```
Crear → Validar → Probar → Aprobar → Usar en flujos de trabajo
```

1. **Crear** una tarjeta con `sdk_create_card` o `sdk_import_github`
2. **Validar** con `sdk_validate_card` (validación de 5 etapas)
3. **Probar** con `sdk_test_card` (ejecución en entorno aislado)
4. **Aprobar** con `sdk_approve_card` (requiere administrador)
5. La tarjeta ahora está disponible en `list_cards` y puede usarse en flujos de trabajo

## Herramientas de desarrollo

### sdk\_create\_card

Crear una nueva tarjeta de socio a partir de código fuente y manifiestos. Ejecuta la validación completa de 5 etapas y almacena la tarjeta en la base de datos. La tarjeta comienza en estado pendiente y requiere aprobación del administrador para activarse.

**Parámetros:**

| Parámetro       | Tipo   | Obligatorio | Descripción                                                             |
| --------------- | ------ | ----------- | ----------------------------------------------------------------------- |
| `app_manifest`  | object | Sí          | Manifiesto de la aplicación con id, name, version, info del socio       |
| `card_manifest` | object | Sí          | Manifiesto de la tarjeta con id, title, entry\_point, class\_name, args |
| `card_type`     | string | Sí          | `action` o `condition`                                                  |
| `source_code`   | string | Sí          | Código fuente en Python (debe extender `PartnerCard`)                   |
| `test_code`     | string | Sí          | Código de pruebas Pytest para la tarjeta                                |
| `locales`       | object | No          | Traducciones de idiomas, ej. `{"en": {...}, "de": {...}}`               |

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
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context):
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}"
            )
        return CardResult(
            status=CardStatus.FAILURE,
            message=f"Amount {total} below threshold {threshold}"
        )
```

**Ejemplo de respuesta:**

```json
{
  "success": true,
  "cards": ["amount-threshold"],
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_validate\_card

Ejecutar la validación de 5 etapas en una tarjeta de socio sin guardar. Dos modos:

* **Modo A** — Validar una tarjeta existente por ID
* **Modo B** — Validar código fuente nuevo en línea

**Parámetros:**

| Parámetro       | Tipo   | Obligatorio | Descripción                           |
| --------------- | ------ | ----------- | ------------------------------------- |
| `card_id`       | string | No          | UUID de la tarjeta existente (Modo A) |
| `app_manifest`  | object | No          | Manifiesto de la aplicación (Modo B)  |
| `card_manifest` | object | No          | Manifiesto de la tarjeta (Modo B)     |
| `card_type`     | string | No          | `action` o `condition` (Modo B)       |
| `source_code`   | string | No          | Código fuente en Python (Modo B)      |
| `test_code`     | string | No          | Código de pruebas (Modo B)            |

{% hint style="info" %}
Proporciona `card_id` solo (Modo A) o `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de validación:**

1. **Estructura** — Verifica la disposición de archivos, esquema del manifiesto, archivos requeridos
2. **Análisis AST** — Comprueba la sintaxis de Python, jerarquía de clases, firmas de métodos
3. **Dependencias** — Valida las importaciones contra los módulos permitidos
4. **Pruebas** — Ejecuta el conjunto de pruebas de la tarjeta
5. **Comportamental** — Ejecuta la tarjeta en un entorno aislado para verificar el comportamiento en tiempo de ejecución

### sdk\_test\_card

Ejecutar una tarjeta de socio en un entorno aislado (sandbox) con un contexto simulado. Usa el mismo modelo de seguridad que producción (builtins restringidos, lista blanca de importaciones, tiempo límite de 10 segundos).

**Parámetros:**

| Parámetro      | Tipo   | Obligatorio | Descripción                                       |
| -------------- | ------ | ----------- | ------------------------------------------------- |
| `card_id`      | string | No          | UUID de la tarjeta existente (Modo A)             |
| `source_code`  | string | No          | Código fuente para pruebas en línea (Modo B)      |
| `class_name`   | string | No          | Nombre de la clase para pruebas en línea (Modo B) |
| `variables`    | object | No          | Variables para pasar al constructor de la tarjeta |
| `mock_context` | object | No          | Contexto de ejecución simulado                    |

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

**Ejemplo de respuesta:**

```json
{
  "success": true,
  "status": "CardStatus.SUCCESS",
  "message": "Amount 1500.00 exceeds threshold 1000",
  "data": {},
  "logs": ["Checking threshold...", "Amount exceeds threshold"]
}
```

### sdk\_import\_github

Importar una aplicación de socio desde un repositorio de GitHub. Clona el repositorio, lee `app.json` e importa todas las tarjetas encontradas en el directorio `.docflowcompose`.

**Parámetros:**

| Parámetro    | Tipo   | Obligatorio | Descripción                                             |
| ------------ | ------ | ----------- | ------------------------------------------------------- |
| `github_url` | string | Sí          | URL HTTPS de GitHub (ej. `https://github.com/org/repo`) |
| `branch`     | string | No          | Rama a clonar (por defecto: `main`)                     |
| `token`      | string | No          | Token de GitHub para repositorios privados              |

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

**Ejemplo de respuesta:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Herramientas de gestión

### sdk\_list\_submissions

Listar todos los envíos de tarjetas de socios de la organización actual.

**Parámetros:** Ninguno

**Ejemplo de respuesta:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Amount Threshold Check",
    "partner_app_id": "com.acme.invoice-tools",
    "partner_status": "validated",
    "version": "1.0.0",
    "card_type": "condition",
    "enabled": false,
    "submitted_at": "2025-03-20T10:00:00"
  }
]
```

### sdk\_get\_submission\_status

Obtener el estado de validación y el informe de un envío específico de tarjeta de socio.

**Parámetros:**

| Parámetro | Tipo   | Obligatorio | Descripción                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Sí          | UUID de la tarjeta de socio |

**Ejemplo de respuesta:**

```json
{
  "card_id": "card-uuid",
  "status": "validated",
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_approve\_card

Aprobar una tarjeta de socio validada y activarla para su uso en flujos de trabajo. La tarjeta se registra en el registro de tiempo de ejecución y queda disponible en `list_cards`.

**Parámetros:**

| Parámetro | Tipo   | Obligatorio | Descripción                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Sí          | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de administrador de la organización. La tarjeta debe estar en estado `validated` o `rejected`.
{% endhint %}

### sdk\_reject\_card

Rechazar un envío de tarjeta de socio y desactivarla.

**Parámetros:**

| Parámetro | Tipo   | Obligatorio | Descripción                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Sí          | UUID de la tarjeta de socio |
| `reason`  | string | No          | Motivo del rechazo          |

{% hint style="warning" %}
Requiere permisos de administrador de la organización.
{% endhint %}

### sdk\_delete\_submission

Desactivar o eliminar un envío de tarjeta de socio. Las tarjetas rechazadas o deshabilitadas se eliminan físicamente de la base de datos. Las tarjetas activas se desactivan primero.

**Parámetros:**

| Parámetro | Tipo   | Obligatorio | Descripción                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Sí          | UUID de la tarjeta de socio |

{% hint style="warning" %}
Requiere permisos de administrador de la organización.
{% endhint %}

### sdk\_list\_cards\_picker

Listar todas las tarjetas habilitadas y no obsoletas con indicadores de rol. Útil para determinar qué tarjetas se pueden usar en qué tipos de nodo al construir flujos de trabajo.

**Parámetros:** Ninguno

**Ejemplo de respuesta:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Document Type Is",
    "category": "Document",
    "card_type": "document_type_is",
    "is_when": true,
    "is_and": false,
    "is_then": false,
    "is_partner_card": false
  }
]
```
