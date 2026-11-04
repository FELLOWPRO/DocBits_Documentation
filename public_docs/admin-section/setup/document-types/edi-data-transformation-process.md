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

# EDI Daten Transformationsprozess

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits Bild"><figcaption></figcaption></figure>

#### Schritt 1: Struktur-Deskriptor

* **Format**: JSON
* **Zweck**: Dieser Schritt beinhaltet die Definition der Struktur der EDI-Daten. Es umfasst die Spezifizierung von Segmenten wie `SAC`, `N1` und `PO1` und erläutert die in jedem Segment enthaltenen Felder. Für Segmente, die verschachtelte Strukturen enthalten, werden Schleifen definiert, um die Datenhierarchie ordnungsgemäß zu organisieren.
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
#### Schritt 2: Transformation mit XSLT

* **Format**: XSLT
* **Zweck**: Dieser Schritt beinhaltet die Umwandlung der strukturierten JSON-Daten in ein strukturiertes XML-Format, wobei der Output speziell an die Anforderungen für weitere Verarbeitung oder Integration angepasst wird. Diese Transformation hilft dabei, präzise Informationen wie Bestätigungstypen, Bestelldetails und bedingte Elemente basierend auf spezifischen Werten zu extrahieren.
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
#### Schritt 3: Vorschau (HTML-Konvertierung)

* **Format**: XSLT (Ausgabe von HTML)
* **Zweck**: Konvertiert die XML-Daten aus Schritt 2 in ein HTML-Format, um die transformierten Daten in einem lesbaren und visuell ansprechenden Format anzuzeigen. Das HTML-Layout enthält Stile für die Präsentation und strukturiert Daten wie Bestellungen, Lieferantendetails und Bestellbedingungen für eine einfache Ansicht.
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
#### Schritt 4: Extraktionspfade

* **Format**: JSON
* **Zweck**: Legt JSON-Pfade fest, um Schlüsselwerte aus den im Schritt 2 erstellten XML-Daten zu extrahieren. Diese Pfade werden verwendet, um spezifische Datenpunkte wie Bestellungen und Währungen abzurufen, die für die nachgelagerte Verarbeitung und Integration in andere Systeme entscheidend sind.
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
Diese aktualisierte Abfolge gewährleistet einen gründlichen Prozess, der rohe EDI-Daten in strukturierte, handlungsfähige Informationen umwandelt, wobei JSON für die Datenstrukturierung, XSLT für die Transformation und die HTML-Vorschau sowie JSON-Pfade für die Datenextraktion und Integration verwendet werden.
