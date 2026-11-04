# eDocs MCP

La API de DocBits expone un servidor de **Model Context Protocol (MCP)** con herramientas para inspeccionar y personalizar el procesamiento de documentos electrónicos (eDoc). Cualquier cliente compatible con MCP (Claude Code, Claude Desktop o integraciones personalizadas) puede conectarse y utilizar estas herramientas.

## ¿Qué puede hacer?

Con las herramientas de eDocs MCP puede:

- **Inspeccionar** cómo se clasifica cualquier tipo de documento electrónico y qué reglas de extracción se aplican
- **Probar** documentos a través del pipeline de procesamiento completo sin guardarlos en la base de datos
- **Crear reglas personalizadas** para su organización: vistas previas XSLT, rutas de extracción, transformaciones
- **Actualizar** una regla personalizada con una nueva versión (con o sin activarla de inmediato)
- **Eliminar** una regla personalizada para volver a la regla predeterminada integrada
- **Verificar** que todos los fixtures de eDoc admitidos se procesan correctamente

## Modelo de permisos

DocBits incluye una biblioteca de reglas predeterminadas integradas, compartidas por todos los clientes. Estas reglas predeterminadas utilizan el ID de organización reservado `00000000-0000-0000-0000-000000000000`.

**Las reglas predeterminadas son inmutables mediante MCP.** Cada herramienta de escritura comprueba el ID de su organización antes de realizar cualquier solicitud. Si corresponde a la organización predeterminada, la operación se rechaza de inmediato: nunca se realiza ninguna llamada a la API.

Los clientes solo pueden crear, modificar o eliminar reglas **dentro de su propia organización**. Cuando existe una regla personalizada para su organización, tiene prioridad sobre la predeterminada. Al eliminar una regla personalizada se restablece automáticamente el comportamiento predeterminado.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Resumen de herramientas

### Inspección (solo lectura)

| Herramienta | Descripción |
|------|-------------|
| `test_electronic_document` | Ejecuta en modo de prueba el pipeline completo de eDoc (clasificación, extracción, vista previa) sin guardar |
| `list_electronic_document_types` | Lista todos los tipos de eDoc admitidos con su estado de configuración |
| `get_extraction_rules` | Muestra las reglas XPath utilizadas para extraer los campos de un tipo de documento determinado |
| `get_extracted_fields` | Obtiene los campos de cabecera extraídos de un documento procesado |
| `get_extracted_tables` | Obtiene las líneas extraídas de un documento procesado |
| `get_preview_pdf` | Recupera el PDF de vista previa generado con XSLT para un documento |
| `get_preview_image` | Recupera una imagen de página renderizada de un documento procesado |
| `extract_edoc_table` | Extrae un archivo XML/EDI que usted indique y devuelve los campos como una tabla plana junto con la regla que produjo cada uno |
| `compare_edoc_extraction` | Compara la extracción predeterminada y la suya personalizada (y, opcionalmente, una regla candidata) en un documento |

### Personalización (limitada a la organización, organización predeterminada bloqueada)

| Herramienta | Descripción |
|------|-------------|
| `list_edoc_custom_attributes` | Lista las personalizaciones de su organización frente a los valores predeterminados integrados para un tipo de documento |
| `create_edoc_custom_attribute` | Crea una nueva regla personalizada (EXTRACTION_PATHS, TRANSFORMATION o PREVIEW) |
| `update_edoc_custom_attribute` | Añade una nueva versión de una regla personalizada, con la opción de activarla de inmediato |
| `delete_edoc_custom_attribute` | Elimina una regla personalizada; el sistema vuelve automáticamente a la predeterminada |
| `preview_edoc_custom_xslt` | Ejecuta en modo de prueba una transformación XSLT sobre un documento XML antes de activarla |
| `get_edoc_attribute_source` | Obtiene el código fuente editable de un atributo (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) para modificarlo |
| `list_edoc_attribute_versions` | Historial de versiones de un atributo personalizado: borradores y versión activa |
| `activate_edoc_attribute_version` | Activa una versión o un borrador concretos (así se realiza una reversión) |
| `delete_edoc_attribute_draft` | Elimina un borrador que nunca se activó |

### Verificación

| Herramienta | Descripción |
|------|-------------|
| `verify_electronic_documents` | Sube fixtures y verifica de extremo a extremo la clasificación, la extracción y la vista previa |
| `validate_all_edocs` | Ejecuta todos los fixtures de eDoc a través de un pipeline en modo de prueba e informa de los problemas |

## Tipos de atributos

Cada regla personalizable tiene un tipo y un formato específicos:

| Nombre del atributo | Formato | Finalidad |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | Expresiones XPath que asignan nodos XML a campos de DocBits |
| `TRANSFORMATION` | XSLT | Hoja de estilos aplicada al XML antes de la extracción |
| `PREVIEW` | XSLT | Hoja de estilos que genera la vista previa en PDF legible para personas |
| `STRUCTURE_DESCRIPTOR` | JSON | Mapa de estructura solo para documentos EDI |

La herramienta `create_edoc_custom_attribute` deduce automáticamente el formato correcto a partir del nombre del atributo.

## Inicio rápido

### Listar lo que su organización ha personalizado

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Devuelve dos listas: `custom` (las personalizaciones de su organización) y `default` (las reglas compartidas que hereda).

### Crear una vista previa personalizada para XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Devuelve el nuevo `attribute_id`; guárdelo para las actualizaciones y la eliminación.

### Actualizar una regla personalizada existente

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Crea una nueva versión y la activa. La versión anterior se conserva en el historial.

### Volver a la regla predeterminada

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Elimina la personalización. El sistema vuelve de inmediato a la regla predeterminada integrada.

## Reglas de seguridad

| Acción | Permitida |
|--------|---------|
| Leer reglas predeterminadas | ✅ Sí |
| Crear una regla personalizada para su organización | ✅ Sí |
| Actualizar una regla personalizada de su organización | ✅ Sí |
| Eliminar una regla personalizada de su organización | ✅ Sí |
| Modificar o eliminar reglas predeterminadas | ❌ **Nunca**: bloqueado en la capa MCP |

Intentar escribir en `00000000-0000-0000-0000-000000000000` devuelve:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

[Configurar DocBits con Claude o Codex](../configuration-with-claude-or-codex.md): conexión, prompts, vistas previas, cambios con versiones, comprobaciones y reversión.
