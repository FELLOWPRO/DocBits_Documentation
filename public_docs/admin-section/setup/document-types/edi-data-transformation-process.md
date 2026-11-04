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

# Processus de Transformation des Données EDI

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Image 4"><figcaption></figcaption></figure>

#### Étape 1 : Descripteur de Structure

* **Format** : JSON
* **Objectif** : Cette étape consiste à définir la structure des données EDI. Cela inclut la spécification des segments tels que `SAC`, `N1` et `PO1`, et détaille les champs contenus dans chaque segment. Pour les segments contenant des structures imbriquées, des boucles sont définies pour organiser correctement la hiérarchie des données.
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
#### Étape 2 : Transformation à l'aide de XSLT

* **Format** : XSLT
* **Objectif** : Cette étape consiste à transformer les données JSON structurées en un format XML structuré, en adaptant spécifiquement la sortie pour répondre aux exigences de traitement ou d'intégration ultérieurs. Cette transformation aide à extraire des informations précises telles que les types d'accusé de réception, les détails de commande et les éléments conditionnels en fonction de valeurs spécifiques.
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
#### Étape 3: Aperçu (Conversion HTML)

* **Format**: XSLT (sortie HTML)
* **Objectif**: Convertit les données XML de l'étape 2 en un format HTML pour prévisualiser les données transformées dans un format lisible et visuellement attrayant. La mise en page HTML inclut des styles de présentation et structure les données telles que les bons de commande, les détails des fournisseurs et les conditions de commande pour une visualisation facile.
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
#### Étape 4 : Chemins d'extraction

* **Format** : JSON
* **Objectif** : Spécifie les chemins JSON pour extraire les valeurs clés des données XML produites à l'étape 2. Ces chemins sont utilisés pour récupérer des points de données spécifiques tels que les commandes d'achat et la devise, qui sont essentiels pour le traitement en aval et l'intégration dans d'autres systèmes.
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
Cela garantit une transformation complète des données EDI brutes en informations structurées et exploitables en utilisant JSON pour la structuration des données, XSLT pour la transformation et l'aperçu HTML, suivi des chemins JSON pour l'extraction et l'intégration des données.
