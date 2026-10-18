# Configurar DocBits con Claude o Codex

Describa el resultado deseado, deje que el asistente lea la configuración, revise su propuesta y aplique el cambio acordado. DocBits MCP ofrece estas herramientas en Claude y Codex con los permisos de su cuenta conectada. Los cambios de configuración requieren los permisos de administrador correspondientes.

Esta guía describe un procedimiento; no acredita una corrección ya realizada para un cliente ni una prueba de exportación satisfactoria.

## 1. Conectarse a la organización correcta

Elija región y entorno en la [guía de endpoints e inicio de sesión](setup-and-configuration.md). Los comandos utilizan el **sandbox de la UE**: sustituya la URL si su organización de prueba usa otro endpoint. Ejecútelos en el equipo donde se ejecuta el asistente e inicie sesión y autorice el acceso a DocBits en el navegador.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

En la aplicación Codex, use los ajustes MCP o la configuración compartida con la CLI en el mismo equipo. En Claude Desktop, use un conector remoto personalizado si su plan lo permite, con el mismo endpoint HTTP. Si no aparecen las herramientas, abra una conversación nueva. Instrucciones actuales: [Codex MCP](https://developers.openai.com/codex/mcp) y [Claude MCP](https://code.claude.com/docs/en/mcp).

```text
Solo lectura. Comprueba el entorno y la organización de DocBits conectados
con get_api_info y get_current_user. Enumera las herramientas de configuración.
Muestra el ID de organización y el host API, sin tokens ni fragmentos de claves.
No cambies ajustes ni proceses documentos.
```

Si la organización aún no está resuelta, lea la configuración pertinente y compruebe el `org_id` de la respuesta. Deténgase si no corresponde a la organización prevista. Los nombres pueden llevar un prefijo del cliente/servidor; use las herramientas y esquemas de argumentos anunciados por su conexión.

## 2. Cambiar un ajuste sencillo

```text
Busca con find_setting el ajuste de extracción de códigos QR de esta
organización de prueba. Muestra su setting_key exacto y valor actual.
Si hay varias coincidencias, pregunta cuál quiero. Si apply_setting admite
el ajuste, prepara una vista previa para activarlo. Muestra current_value
y proposed_value; espera mi confirmación antes de confirm_setting_change.
```

`apply_setting` solo crea una vista previa. Tras confirmar esa propuesta concreta, `confirm_setting_change(preview_id)` guarda el cambio. Lea de nuevo el valor y conserve el `undo_id`: `undo_setting_change` permite revertirlo dentro del plazo devuelto. Normalmente la vista previa caduca a los 5 minutos y la reversión a los 15. Si el valor cambió o la vista previa caducó, genere y revise otra.

Para cambios estructurados compatibles: `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Lea primero los tipos de acción disponibles. Si no existe una acción de escritura compatible, solicite el `app_path` y realice el cambio en DocBits. No invente una clave de preferencia ni recurra a una llamada genérica a `set_preference`.

## 3. Investigar una nota de crédito guardada como Invoice

Una transformación Custom puede producir siempre `<INVOICE_TYPE>Invoice</INVOICE_TYPE>`, aunque el XML original contenga un código de nota de crédito. Es el escenario de la [guía de diagnóstico con vídeo de la interfaz real de DocBits](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Solo lectura. Para el XML original y el ID de documento proporcionados,
identifica familia eDoc, sintaxis, versión/perfil y código de tipo original.
Enumera atributos Custom y Default. Lee TRANSFORMATION y EXTRACTION_PATHS
efectivos y predeterminados con get_edoc_attribute_source. Registra
attribute_id, active_version y active_value_id y lee el historial.
Rastrea TypeCode -> XML transformado -> invoice_type -> valor guardado,
vista previa de exportación y scripts posteriores. Expón pruebas e incógnitas.
No actives, elimines, reinicies, apruebes ni exportes nada.
```

Use la **etiqueta exacta del formato detectado**, sin adivinar la versión de ZUGFeRD o Factur-X. El `doc_type_key` técnico puede seguir siendo `INVOICE`; el valor de negocio investigado es `invoice_type`.

| Consulta | Herramienta MCP |
| --- | --- |
| Atributos Custom y Default | `list_edoc_custom_attributes` |
| Fuente efectiva o predeterminada e IDs activos | `get_edoc_attribute_source`, con `source: "effective"` o `"default"` |
| Historial y borradores | `list_edoc_attribute_versions`, con `include_values: true` si es necesario |
| Campos guardados, registros, vista previa de exportación | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

La versión activa hoy no demuestra cuál procesó un documento antiguo. Si los registros no lo aclaran, mantenga esa incertidumbre. Una vista previa PDF no demuestra el tipo guardado ni los importes exportados.

<figure><img src="../../.gitbook/assets/edocs-transformation-es.png" alt="Ejemplo de desarrollo de solo lectura: editor de fuente y versiones de DocBits. Lea su propia fuente efectiva y valor activo por MCP; la imagen no demuestra un cambio guardado."><figcaption><p>Ejemplo de desarrollo de solo lectura: editor de fuente y versiones de DocBits. Lea su propia fuente efectiva y valor activo por MCP; la imagen no demuestra un cambio guardado.</p></figcaption></figure>

## 4. Probar la corrección mínima sin guardarla

```text
Propón el cambio mínimo de nuestra transformación Custom existente para
que 381 produzca Credit Note. Conserva las demás asignaciones y los códigos
de abono ya admitidos. No clasifiques 383 ni 384 como Credit Note.
Muestra el diff. Previsualiza el candidato con nuestros documentos de prueba
sin guardarlo. Muestra INVOICE_TYPE transformado e importes pertinentes,
y especifica las pruebas que aún faltan.
```

Para un **atributo existente de la propia organización**, llame a `preview_edoc_custom_xslt` con el candidato completo:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Sustituya todos los marcadores por valores de sus respuestas; el XSLT/JSON debe ser completo y estar correctamente escapado como cadena JSON. Se usa un documento existente de la misma organización. La herramienta devuelve **XML** para `TRANSFORMATION`, campos/tablas para `EXTRACTION_PATHS` y **PDF** para `PREVIEW`, sin guardar el candidato. Para comparar con la transformación predeterminada, pruebe su fuente como otro candidato con el mismo atributo Custom y documento.

`compare_edoc_extraction` compara **EXTRACTION_PATHS** y requiere un atributo Custom de rutas de extracción. No compara transformaciones. No cree una personalización innecesaria solo para usarlo.

Si no existe un atributo Custom, deténgase antes de crearlo en producción: `create_edoc_custom_attribute` crea una primera versión **activa inmediatamente** y no tiene opción de solo borrador. Prepare la nueva personalización en una organización de prueba o use el flujo de creación/vista previa compatible del editor DocBits. No intente modificar globalmente los valores predeterminados compartidos.

## 5. Guardar un borrador y activarlo expresamente

Tras revisar el diff y la salida, vuelva a leer la fuente activa. Si cambió durante el trabajo, compare otra vez. Para un atributo Custom existente, use `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Indique siempre `activate: false` en este paso: su valor predeterminado es `true`. Registre el ID del valor de versión devuelto y compruebe con `list_edoc_attribute_versions` que la versión anterior sigue activa. Guardar un borrador no afecta al procesamiento normal.

Después de las pruebas, el administrador confirma la organización, atributo, diff y versión concretos. Active con `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` es el **ID del valor de la versión**, no su número ni el ID del atributo. Lea de nuevo la fuente efectiva y el historial para comprobar que ese valor está activo. eDocs utiliza estas herramientas directamente, no el flujo genérico de ajustes con `preview_id`. Obtenga los IDs del entorno de destino; los del sandbox no sirven en producción.

## 6. Verificar clasificación, importes y exportación

`test_electronic_document` ejecuta un dry-run de la configuración **activa actualmente**, sin guardar un documento. No permite seleccionar un candidato o borrador. Por MCP HTTP remoto, envíe el XML original como `file_content_base64` con `file_name`; el servidor no puede leer un `file_path` local de su equipo. Para probar la canalización completa del candidato, actívelo primero expresamente en la organización de prueba. La vista previa XSLT no prueba scripts posteriores ni exportaciones.

| Código original | Comprobación esperada |
| --- | --- |
| 380 | Invoice sigue siendo Invoice |
| 381 | La nota de crédito resulta en Credit Note |
| 261 | Conservar el comportamiento de abono si el formato/asignación lo admite |
| 383 | Una nota de débito no pasa a Credit Note por ajustar una factura |
| 384 | Una factura corregida no pasa a Credit Note por ser una corrección |

Compruebe campos personalizados, líneas, totales y el ajuste de signo negativo. Procese un **documento de prueba nuevo** en una organización aislada con exportaciones automáticas controladas. Compare `invoice_type` guardado, panel y `get_export_preview`. Una exportación real al sistema de destino requiere una prueba acordada por separado; ni el dry-run ni la vista previa demuestran entrega al ERP.

`validate_all_edocs` prueba los archivos de muestra disponibles en el servidor sin persistir documentos; `verify_electronic_documents` **sube y procesa** muestras. No sustituyen sus documentos representativos ni las comprobaciones posteriores. Si no hay muestras/herramientas disponibles, use ejemplos proporcionados.

## 7. Revertir y tratar los documentos antiguos por separado

Para revertir, use `activate_edoc_attribute_version` con el `active_value_id` anterior como `draft_id` y compruebe la fuente efectiva. No elimine toda la personalización para corregir un campo: perdería otras asignaciones y se aplicaría el valor predeterminado.

No reinicie documentos históricos en bloque. El reinicio puede borrar datos extraídos y registros de exportación y repetir aprobaciones o exportaciones. Revise por documento el estado de exportación, aprobaciones y cambios manuales antes de decidir su corrección.

Para otras configuraciones, empiece por `find_setting` o `run_config_checks` y solicite la acción compatible o ruta en la interfaz. Conserve la propuesta antes/después, resultados de pruebas, IDs de valores activos y referencia de reversión en el registro del cambio.
