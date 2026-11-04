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

# Processo di Trasformazione dei Dati EDI

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Immagine 4"><figcaption></figcaption></figure>

#### Passo 1: Descrittore della Struttura

* **Formato**: JSON
* **Scopo**: Questo passo implica la definizione della struttura dei dati EDI. Include la specifica dei segmenti come `SAC`, `N1` e `PO1`, e dettaglia i campi contenuti all'interno di ciascun segmento. Per i segmenti che contengono strutture nidificate, vengono definiti cicli per organizzare correttamente l'iterazione dei dati.
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
#### Passo 2: Trasformazione Utilizzando XSLT

* **Formato**: XSLT
* **Scopo**: Questo passaggio coinvolge la trasformazione dei dati JSON strutturati in un formato XML strutturato, adattando specificamente l'output per soddisfare i requisiti per ulteriori elaborazioni o integrazioni. Questa trasformazione aiuta nell'estrazione di informazioni precise come tipi di conferma, dettagli dell'ordine ed elementi condizionali basati su valori specifici.
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
#### Passo 3: Anteprima (Conversione HTML)

* **Formato**: XSLT (output in HTML)
* **Scopo**: Converte i dati XML dal Passo 2 in un formato HTML per visualizzare i dati trasformati in un formato leggibile e visivamente accattivante. Il layout HTML include stili per la presentazione e struttura i dati come ordini di acquisto, dettagli del fornitore e termini dell'ordine per una visualizzazione semplice.
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
#### Passo 4: Percorsi di Estrazione

* **Formato**: JSON
* **Scopo**: Specifica i percorsi JSON per estrarre i valori chiave dai dati XML prodotti nel Passo 2. Questi percorsi vengono utilizzati per recuperare punti dati specifici come ordini di acquisto e valuta, che sono cruciali per l'elaborazione successiva e l'integrazione in altri sistemi.
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
Questo sequenza aggiornata garantisce un processo accurato, trasformando i dati EDI grezzi in informazioni strutturate e utilizzabili utilizzando JSON per la strutturazione dei dati, XSLT per la trasformazione e l'anteprima HTML, seguita dai percorsi JSON per l'estrazione e l'integrazione dei dati.
