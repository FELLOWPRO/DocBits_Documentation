# Transformatieproces voor EDI-gegevens

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/site-all-edi-list-nl.png" alt="Bestaand EDI-formaat met de vier geconfigureerde attributen."><figcaption><p>Bestaand EDI-formaat met de vier geconfigureerde attributen.</p></figcaption></figure>

DocBits verwerkt het onbewerkte EDI-bericht tot JSON met behulp van een JSON-structuurbeschrijving. Vervolgens maakt het een tussenliggende XML-versie, past XSLT toe om standaard-XML te maken en gebruikt die XML voor veld- en tabelextractie en het voorbeeld.

De onderstaande voorbeelden zijn illustratieve fragmenten, geen volledige configuraties die direct kunnen worden geïmporteerd. Sommige laten inhoud weg of bevatten tijdelijke aanduidingen zoals `...`. Pas ze aan en test ze met uw daadwerkelijke EDI-bericht, de tussenliggende XML en de getransformeerde uitvoer. Behoud de veldidentificatoren die uw configuratie nodig heeft.

## Stap 1: De EDI-structuur beschrijven

De JSON-structuurbeschrijving definieert segmenten zoals SAC, N1 en PO1, hun velden en geneste lussen. Ze bepaalt hoe het onbewerkte EDI-bericht wordt ingelezen als gestructureerde JSON.

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

## Stap 2: Tussenliggende XML transformeren met XSLT

DocBits zet de ingelezen JSON om in tussenliggende XML voordat het transformatie-stylesheet wordt toegepast. XSLT leest deze XML, niet rechtstreeks de JSON, en maakt de standaard-XML-structuur voor verdere verwerking. Het voorbeeld selecteert bevestigingsgegevens en voorwaarden uit XML-knooppunten.

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

## Stap 3: Een HTML-voorbeeld maken

Een voorbeeld-stylesheet zet de getransformeerde XML uit stap 2 om in HTML. Pas de indeling en gegevensbindingen aan het documenttype aan en controleer of het voorbeeld de getransformeerde gegevens correct weergeeft.

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

## Stap 4: XPath-extractie configureren

De extractieconfiguratie wordt in JSON opgeslagen, maar de paden zijn XPath-expressies die worden geëvalueerd op de getransformeerde XML uit stap 2. Veldpaden selecteren waarden; een tabelrijpad selecteert rijen en kolompaden selecteren waarden binnen elke rij. Dit zijn geen JSONPath-expressies.

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

Het volledige proces is: onbewerkte EDI → gestructureerde JSON → tussenliggende XML → standaard-XML via XSLT → veld- en tabelextractie met XPath en een HTML-voorbeeld. Valideer de uitvoer en geëxtraheerde waarden met representatieve berichten voordat u een configuratie in productie gebruikt.


De weergaven tonen een bestaande configuratie en versie. De instellingen verschillen per documenttype en formaat. Valideer wijzigingen in een concept voordat u ze activeert.

De afbeeldingen tonen de Nederlandstalige proceskaarten en de actieve, alleen-lezen configuratieversie. De tabnaam Builder, technische attribuutnamen en configuratiecode zijn overgenomen uit de geïllustreerde productversie.
