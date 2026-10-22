# EDI-Datentransformationsprozess

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/site-all-edi-list-de.png" alt="Vorhandenes EDI-Format mit seinen vier konfigurierten Attributen."><figcaption><p>Vorhandenes EDI-Format mit seinen vier konfigurierten Attributen.</p></figcaption></figure>

DocBits verarbeitet die EDI-Rohnachricht mithilfe einer JSON-Strukturbeschreibung zu JSON. Anschließend erzeugt es ein XML-Zwischenformat, wandelt dieses mit XSLT in Standard-XML um und nutzt das Ergebnis für die Feld- und Tabellenextraktion sowie die Vorschau.

Die folgenden Beispiele sind illustrative Ausschnitte und keine vollständigen, direkt importierbaren Konfigurationen. Manche lassen Inhalte aus oder enthalten Platzhalter wie `...`. Passen Sie sie an Ihre tatsächliche EDI-Nachricht an und testen Sie sie mit dem XML-Zwischenformat und der transformierten Ausgabe. Behalten Sie die von Ihrer Konfiguration benötigten Feldkennungen bei.

## Schritt 1: EDI-Struktur beschreiben

Die JSON-Strukturbeschreibung definiert Segmente wie SAC, N1 und PO1, deren Felder und verschachtelte Schleifen. Sie steuert, wie die EDI-Rohnachricht in strukturiertes JSON eingelesen wird.

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

## Schritt 2: XML-Zwischenformat mit XSLT transformieren

DocBits wandelt das eingelesene JSON vor der Transformation in ein XML-Zwischenformat um. XSLT liest dieses XML und nicht direkt das JSON. Es erzeugt die Standard-XML-Struktur für die weitere Verarbeitung. Das Beispiel liest Bestätigungsdaten und Bedingungen aus XML-Knoten.

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

## Schritt 3: HTML-Vorschau erstellen

Ein Vorschau-Stylesheet wandelt das transformierte XML aus Schritt 2 in HTML um. Passen Sie Layout und Datenbindungen an den Dokumenttyp an und prüfen Sie, ob die Vorschau die transformierten Daten richtig darstellt.

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

## Schritt 4: XPath-Extraktion konfigurieren

Die Extraktionskonfiguration wird als JSON gespeichert. Ihre Pfade sind jedoch XPath-Ausdrücke, die gegen das transformierte XML aus Schritt 2 ausgewertet werden. Feldpfade wählen Werte aus; ein Tabellenzeilenpfad wählt Zeilen aus, und Spaltenpfade wählen Werte innerhalb der jeweiligen Zeile. Es handelt sich nicht um JSONPath-Ausdrücke.

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

Der vollständige Ablauf lautet: EDI-Rohdaten → strukturiertes JSON → XML-Zwischenformat → Standard-XML durch XSLT → Feld- und Tabellenextraktion mit XPath sowie HTML-Vorschau. Prüfen Sie Ausgabe und extrahierte Werte mit repräsentativen Nachrichten, bevor Sie eine Konfiguration produktiv einsetzen.


Die Ansichten zeigen eine vorhandene Konfiguration und Version. Die Einstellungen unterscheiden sich je nach Dokumenttyp und Format. Prüfen Sie Änderungen in einem Entwurf vor der Aktivierung.
