# Processo di trasformazione dei dati EDI



<figure><img src="../../../.gitbook/assets/site-all-edi-list-it.png" alt="Formato EDI esistente con i quattro attributi configurati."><figcaption><p>Formato EDI esistente con i quattro attributi configurati.</p></figcaption></figure>

DocBits analizza il messaggio EDI originale e lo converte in JSON tramite un descrittore di struttura JSON. Crea quindi un XML intermedio, applica XSLT per produrre l’XML standard e usa questo XML per estrarre campi e tabelle e generare l’anteprima.

Gli esempi seguenti sono frammenti illustrativi, non configurazioni complete pronte per l’importazione. Alcuni omettono contenuti o includono segnaposto come `...`. Adattarli e verificarli con il messaggio EDI effettivo, l’XML intermedio e l’output trasformato; mantenere gli identificatori dei campi richiesti dalla propria configurazione.

## Passaggio 1: descrivere la struttura EDI

Il descrittore di struttura JSON definisce segmenti come SAC, N1 e PO1, i relativi campi e i cicli annidati. Determina come il messaggio EDI originale viene analizzato per ottenere JSON strutturato.

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

## Passaggio 2: trasformare l’XML intermedio con XSLT

DocBits converte il JSON analizzato in XML intermedio prima di applicare il foglio di trasformazione. XSLT legge questo XML intermedio, non direttamente il JSON, e produce la struttura XML standard per le elaborazioni successive. L’esempio seleziona dati di conferma e condizioni dai nodi XML.

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

## Passaggio 3: creare un’anteprima HTML

Un foglio di stile per l’anteprima converte in HTML l’XML trasformato nel passaggio 2. Adattare l’impaginazione e i collegamenti ai dati al tipo di documento e verificare che l’anteprima rappresenti correttamente i dati trasformati.

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

## Passaggio 4: configurare l’estrazione XPath

La configurazione di estrazione è memorizzata in JSON, ma i suoi percorsi sono espressioni XPath valutate sull’XML trasformato nel passaggio 2. I percorsi dei campi selezionano valori; il percorso delle righe di una tabella seleziona le righe e i percorsi delle colonne selezionano valori all’interno di ciascuna riga. Non sono espressioni JSONPath.

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

Il flusso completo è: EDI originale → JSON strutturato → XML intermedio → XML standard tramite XSLT → estrazione di campi e tabelle con XPath e anteprima HTML. Convalidare l’output e i valori estratti con messaggi rappresentativi prima di usare una configurazione in produzione.


Le viste mostrano una configurazione e una versione esistenti. Le impostazioni variano in base al tipo di documento e al formato. Convalidare le modifiche in una bozza prima dell’attivazione.

Nella versione dell’interfaccia illustrata, l’intestazione Version del pannello delle versioni resta in inglese. Gli identificatori tecnici degli attributi e il codice di configurazione restano invariati.
