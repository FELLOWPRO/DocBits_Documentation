---
layout:
title:
visible: true
description:
visible: true
tableOfContents:
visible: true
outline:
visible: true
pagination:
visible: true
---

# Proceso de Transformación de Datos EDI

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Imagen 4"><figcaption></figcaption></figure>

#### Paso 1: Descriptor de Estructura

* **Formato**: JSON
* **Propósito**: Este paso implica definir la estructura de los datos EDI. Incluye la especificación de segmentos como `SAC`, `N1` y `PO1`, y detalla los campos contenidos dentro de cada segmento. Para segmentos que contienen estructuras anidadas, se definen bucles para organizar adecuadamente la jerarquía de datos.
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
#### Paso 2: Transformación Usando XSLT

* **Formato**: XSLT
* **Propósito**: Este paso implica transformar los datos JSON estructurados en un formato XML estructurado, adaptando específicamente la salida para cumplir con los requisitos de procesamiento o integración adicionales. Esta transformación ayuda a extraer información precisa como tipos de acuse de recibo, detalles del pedido y elementos condicionales basados en valores específicos.
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
#### Paso 3: Vista previa (Conversión HTML)

* **Formato**: XSLT (generando HTML)
* **Propósito**: Convierte los datos XML del Paso 2 en un formato HTML para previsualizar los datos transformados de manera legible y visualmente atractiva. El diseño HTML incluye estilos para la presentación y estructura los datos como órdenes de compra, detalles de proveedores y términos de pedido para una visualización sencilla.
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
#### Paso 4: Rutas de Extracción

* **Formato**: JSON
* **Propósito**: Especifica las rutas JSON para extraer valores clave de los datos XML producidos en el Paso 2. Estas rutas se utilizan para recuperar puntos de datos específicos como órdenes de compra y moneda, que son cruciales para el procesamiento posterior e integración en otros sistemas.
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
Esta secuencia actualizada garantiza un proceso exhaustivo, transformando datos EDI sin procesar en información estructurada y accionable utilizando JSON para la estructuración de datos, XSLT para la transformación y vista previa en HTML, seguido de rutas JSON para la extracción e integración de datos.
