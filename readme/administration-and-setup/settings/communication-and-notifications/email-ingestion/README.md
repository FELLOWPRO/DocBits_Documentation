# Email Ingestion

<figure><img src="../../../../.gitbook/assets/email_ingestion.png" alt="Email Ingestion"><figcaption><p>Página de configuración de Email Ingestion</p></figcaption></figure>

Email Ingestion configura cómo DocBits procesa los correos electrónicos entrantes y los convierte en documentos. Puede definir reglas de clasificación, ajustes de extracción y lógica de procesamiento para cada tipo de documento.

## Activar Email Ingestion

Utilice el interruptor **ENABLED** en la parte superior derecha para activar o desactivar la ingesta de correos electrónicos de forma global.

## Pestañas de tipos de documento

La fila superior muestra pestañas para cada tipo de documento admitido:

* **Orders** — Pedidos de compra recibidos por correo electrónico
* **Invoices** — Documentos de factura
* **Quotes** — Documentos de presupuesto/oferta
* **Delivery Notes** — Documentos de albarán de entrega
* **COA** — Documentos de certificado de análisis
* **PO Confirm** — Confirmaciones de pedidos de compra

Seleccione una pestaña para configurar los ajustes específicos de ese tipo de documento.

## Pestañas de configuración

Cada tipo de documento tiene cinco pestañas de configuración:

### Classification

Defina reglas para clasificar automáticamente los correos electrónicos entrantes por tipo de documento. Cada regla tiene:

| Campo | Descripción |
|-------|-------------|
| **Rule Type** | Cómo coincidir: Subject Keyword, Sender Domain o Body Keyword. |
| **Pattern** | La palabra clave o el patrón de dominio que debe coincidir (varios valores separados por `|`). |
| **Maps to** | El tipo de documento al que clasifica esta regla (p. ej., ORDER, INVOICE). |

Las reglas se evalúan en orden (arrastre para reordenarlas). Cada regla se puede activar o desactivar, editar o eliminar.

### Field Extraction

Configure qué campos se extraen del cuerpo del correo electrónico y cómo se asignan a los campos del documento.

### Processing Rules

Defina reglas sobre cómo se procesan los correos electrónicos coincidentes (p. ej., aprobación automática, enrutamiento a un flujo de trabajo específico).

### Sender Management

Gestione los remitentes conocidos y sus asignaciones predeterminadas de tipo de documento.

### Training

Entrene el modelo de clasificación con correos electrónicos de muestra para mejorar la precisión de la clasificación automática.
