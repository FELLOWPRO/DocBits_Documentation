# OCR Settings

<figure><img src="../../../../.gitbook/assets/ocr_settings.png" alt="OCR Settings"><figcaption><p>Página de OCR Settings</p></figcaption></figure>

OCR (Optical Character Recognition, reconocimiento óptico de caracteres) Settings controla cómo DocBits lee y extrae el texto de sus documentos. Esta página se organiza en cuatro secciones.

## OCR Quality

Establezca el porcentaje mínimo de calidad que debe tener un documento para procesarse automáticamente.

* **Quality Slider**: arrástrelo para establecer el umbral (10%–100%). Los documentos con una calidad inferior no se procesarán automáticamente.
* **Below 75% Warning**: si la calidad es inferior al 75%, DocBits no puede garantizar una extracción correcta.
* **What to do when document quality is lower than selected**: elija el comportamiento alternativo:
  * **Run again after confirmation** — Vuelve a ejecutar el OCR tras la confirmación manual.
  * **Skip** — Omite el documento por completo.

## General OCR Settings

| Ajuste | Descripción |
|---------|-------------|
| **Use E-Text if available** | Si está activado, DocBits utiliza el texto electrónico incrustado (p. ej., de PDF digitales) en lugar de ejecutar el OCR. Esto mejora la precisión en documentos creados digitalmente. |
| **Use DESKEW if available** | Endereza automáticamente los documentos escaneados inclinados o torcidos antes del procesamiento OCR. |
| **AI OCR Version** | Seleccione la versión del motor de OCR (p. ej., 2_0). Las versiones más recientes pueden ofrecer un mejor reconocimiento. |

## OCR Settings for Tables

| Ajuste | Descripción |
|---------|-------------|
| **Use AI data for tables if available** | Si está activado, utiliza la extracción basada en IA para los datos de las tablas, lo que puede mejorar la precisión en estructuras de tabla complejas. |

## OCR Settings for Header Fields

Controla cómo se extraen los campos de cabecera (los datos que no pertenecen a tablas):

| Ajuste | Descripción |
|---------|-------------|
| **Use Rules Extraction** | Extrae los campos de cabecera mediante reglas y patrones predefinidos. |
| **Use AI Extraction** | Extrae los campos de cabecera mediante reconocimiento basado en IA. |

{% hint style="info" %}
Si tanto Rules Extraction como AI Extraction están activados, se ejecutan de forma secuencial: primero Rules Extraction y después AI Extraction.
{% endhint %}
