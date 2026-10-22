# Proceso de transformación de datos EDI



<figure><img src="../../../.gitbook/assets/site-all-edi-list-es.png" alt="Formato EDI existente con sus cuatro atributos configurados."><figcaption><p>Formato EDI existente con sus cuatro atributos configurados.</p></figcaption></figure>

DocBits analiza el mensaje EDI original y lo convierte en JSON mediante un descriptor de estructura JSON. Después genera un XML intermedio, aplica XSLT para producir el XML estándar y utiliza ese XML para extraer campos y tablas y generar la vista previa.

Los ejemplos siguientes son fragmentos ilustrativos, no configuraciones completas listas para importar. Algunos omiten contenido o incluyen marcadores como `...`. Adáptelos y pruébelos con su mensaje EDI real, el XML intermedio y el resultado transformado; conserve los identificadores de campo que necesita su configuración.

## Paso 1: Describir la estructura EDI

El descriptor de estructura JSON define segmentos como SAC, N1 y PO1, sus campos y los bucles anidados. Determina cómo se analiza el mensaje EDI original para obtener JSON estructurado.

```json
{
  "SAC": {"fields": ["SAC", "DTM", "TX1", "TD5"]},
  "N1": {"fields": ["N1", "N2", "N3", "N4", "PER"]},
  "PO1": {
    "fields": ["PO1", "REF"],
    "loops": {
      "SAC": {"fields": ["SAC", "TX1", "DTM"]}
    }
  }
}
```

## Paso 2: Transformar el XML intermedio con XSLT

DocBits convierte el JSON analizado en XML intermedio antes de aplicar la hoja de transformación. XSLT lee este XML intermedio, no el JSON directamente, y produce la estructura XML estándar para el procesamiento posterior. El ejemplo selecciona datos de confirmación y condiciones a partir de nodos XML.

```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" />
    <xsl:template match="/">
        <ORDER_CONFIRMATION>
            <ACKNOWLEDGEMENT_TYPE>
                <xsl:value-of select="//BAK/VALUE_2/text()" />
            </ACKNOWLEDGEMENT_TYPE>
            <ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
                <xsl:choose>
                    <xsl:when test="//BAK/VALUE_2='AD'">With detail, no change</xsl:when>
                    <xsl:when test="//BAK/VALUE_2='AC'">With detail and change</xsl:when>
                    <xsl:otherwise>Unknown</xsl:otherwise>
                </xsl:choose>
            </ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
            <!-- Additional fields and conditions are similarly transformed -->
        </ORDER_CONFIRMATION>
    </xsl:template>
</xsl:stylesheet>

```

## Paso 3: Crear una vista previa HTML

Una hoja de estilo de vista previa convierte en HTML el XML transformado en el paso 2. Adapte el diseño y los enlaces de datos al tipo de documento y compruebe que la vista previa representa correctamente los datos transformados.

```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" />
    <xsl:template match="/">
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Preview of Transformed EDI Data</title>
                <!-- Styles and head elements -->
            </head>
            <body>
                <div>
                    <!-- HTML structure mimicking an invoice or other document type, with data bindings from the transformed XML -->
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>


```

## Paso 4: Configurar la extracción con XPath

La configuración de extracción se guarda en JSON, pero sus rutas son expresiones XPath evaluadas sobre el XML transformado en el paso 2. Las rutas de campos seleccionan valores; la ruta de filas de una tabla selecciona filas, y las rutas de columnas seleccionan valores dentro de cada fila. No son expresiones JSONPath.

```json
{
  "fields": {
    "purchase_order": "//ORDER_CONFIRMATION/PURCHASE_ORDER/text()",
    "currency": "//ORDER_CONFIRMATION/CURRENCY/text()",
    ...
  },
  "tables": [
    {
      "name": "ORDER_CONFIRMATION_TABLE",
      "row_path": "//ORDER_CONFIRMATION/ORDER_LINES/ORDER_LINE",
      "columns": [
        {"name": "POSITION", "path": "POSITION/text()"},
        ...
      ]
    }
  ]
}
```

El flujo completo es: EDI original → JSON estructurado → XML intermedio → XML estándar mediante XSLT → extracción de campos y tablas con XPath y vista previa HTML. Valide la salida y los valores extraídos con mensajes representativos antes de utilizar una configuración en producción.


Las vistas muestran una configuración y una versión existentes. Los ajustes varían según el tipo de documento y el formato. Valide los cambios en un borrador antes de activarlos.

Algunas etiquetas, como Custom, Default, Version y Last Modified At, siguen apareciendo en inglés en la interfaz actual del producto. Los identificadores técnicos de atributos y el código de configuración se conservan sin cambios.
