# Ejemplos

Consulte los prompts y el procedimiento de diagnóstico, borrador, activación y reversión en [Configurar DocBits con Claude o Codex](../docbits-mcp/configuration-with-claude-or-codex.md). Los ejemplos usan los parámetros actuales. Sustituya todos los marcadores por valores de su organización y use fuentes completas, correctamente escapadas como cadenas JSON.

## 1. Modificar una regla Custom existente

Lea la `TRANSFORMATION` efectiva con `get_edoc_attribute_source`, usando la etiqueta exacta del formato devuelta por la clasificación:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Registre `attribute_id`, `active_value_id`, `active_version` y `value`. Lea `source: "default"` por separado para comparar, y el historial con `list_edoc_attribute_versions`. Los siguientes pasos suponen un atributo Custom existente de su organización.

Pruebe el candidato completo sin guardarlo con `preview_edoc_custom_xslt`. Use un documento ya existente en la misma organización:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

El resultado es XML transformado para `TRANSFORMATION`, PDF para `PREVIEW` o campos/tablas para `EXTRACTION_PATHS`. La vista previa no selecciona un borrador guardado ni prueba scripts posteriores o exportaciones.

Tras revisar el diff y la vista previa, vuelva a leer la fuente activa y guarde un borrador con `update_edoc_custom_attribute`. Indique `activate: false` explícitamente; el valor predeterminado es `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Tras probar en la organización de prueba y confirmar el cambio concreto, llame a `activate_edoc_attribute_version`. `draft_id` es el ID del valor de versión. Vuelva a leer la fuente efectiva. Para revertir, use el `active_value_id` anterior en la misma llamada.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Si no existe un atributo Custom

`create_edoc_custom_attribute` crea una primera versión activa inmediatamente, no un borrador. Pruebe la nueva personalización en una organización de prueba o use el flujo compatible del editor DocBits. No cree ni elimine personalizaciones de producción solo para obtener una vista previa. Preserve las asignaciones necesarias; no modifique globalmente los valores predeterminados compartidos.

## 3. Probar la configuración activa

Llame a `test_electronic_document` con el XML original codificado en base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Esto prueba las reglas activas sin guardar un documento, no un borrador inactivo. MCP HTTP remoto no puede leer un `file_path` local de su equipo. `compare_edoc_extraction` solo compara Extraction Paths y requiere un atributo Custom de rutas de extracción; no compara transformaciones.

`validate_all_edocs` prueba sin persistencia las muestras disponibles en el servidor. `verify_electronic_documents` las sube y procesa, creando documentos. Ninguno demuestra entrega al ERP. Use ejemplos representativos, compruebe campos/importes guardados y exportación por separado y no reinicie documentos históricos en bloque.
