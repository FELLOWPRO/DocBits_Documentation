# Ejemplos

Ejemplos de principio a fin que muestran cómo utilizar conjuntamente las herramientas de eDocs MCP.

## Ejemplo 1: Crear una vista previa personalizada para XRechnung

Este ejemplo recorre el ciclo de vida completo de una regla PREVIEW personalizada:
1. Comprobar qué reglas existen ya
2. Previsualizar el XSLT sin activarlo
3. Crear la regla personalizada
4. Actualizarla a una nueva versión
5. Volver a la versión predeterminada

### Paso 1: Comprobar las personalizaciones existentes

Llame a `list_edoc_custom_attributes`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

La respuesta muestra dos listas. Si `custom` está vacío para el atributo `PREVIEW`, su organización utiliza actualmente la hoja de estilos de vista previa predeterminada integrada.

### Paso 2: Probar su XSLT antes de crearlo

Llame a `preview_edoc_custom_xslt` con el ID de un atributo existente (utilice uno predeterminado de la respuesta de `list`) y un archivo XML de ejemplo codificado en base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Inspeccione el resultado renderizado para comprobar que su XSLT produce el resultado esperado antes de aplicarlo.

### Paso 3: Crear la regla personalizada

Llame a `create_edoc_custom_attribute`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Guarde el `attribute_id` de la respuesta. A partir de este momento, todas las facturas XRechnung 2.1 CII que procese su organización utilizarán su vista previa personalizada.

### Paso 4: Actualizar la regla con una nueva versión

Más adelante, si desea refinar el XSLT, llame a `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Al establecer `activate: true` se cambia inmediatamente a la nueva versión. La versión anterior se conserva en el historial. Establezca `activate: false` para guardarla como borrador y activarla por separado.

### Paso 5: Volver a la versión predeterminada integrada

Si desea volver a la vista previa predeterminada, llame a `delete_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

La regla personalizada se elimina y el sistema vuelve automáticamente a la hoja de estilos predeterminada compartida. Ningún otro cliente se ve afectado.

---

## Ejemplo 2: Personalizar las rutas de extracción para EDI

Su organización recibe facturas EDI con un diseño de campos no estándar. Este ejemplo muestra cómo sobrescribir las rutas de extracción para su organización.

### Paso 1: Comprobar las reglas actuales

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Si ve una entrada `EXTRACTION_PATHS` en `default` pero no en `custom`, su organización hereda las reglas XPath compartidas.

### Paso 2: Crear sus rutas de extracción personalizadas

Llame a `create_edoc_custom_attribute` con su JSON de XPath ajustado:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Paso 3: Verificar con una prueba en seco

Llame a `test_electronic_document` con un archivo EDI de ejemplo para confirmar que las rutas de extracción personalizadas obtienen los valores correctos:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

La respuesta incluye `extracted_fields` y un PNG `preview.image_base64`: inspeccione ambos para verificar que son correctos antes de pasar a producción.

---

## Ejemplo 3: Ejecutar una verificación completa de eDocs

Antes de publicar un cambio, verifique que todos los fixtures de eDocs compatibles siguen superando las pruebas:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

La herramienta ejecuta todos los fixtures de XRechnung a través del pipeline e informa del resultado correcto/incorrecto/advertencia por fixture. Una ejecución limpia confirma que sus personalizaciones no han afectado a otros tipos de documento.

Para probar rápidamente un único tipo:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Esto carga hasta 3 fixtures de ZUGFeRD, espera al procesamiento y verifica de principio a fin la clasificación, la extracción y la generación de la vista previa.
