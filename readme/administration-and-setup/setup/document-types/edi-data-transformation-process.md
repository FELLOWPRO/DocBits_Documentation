# Proces transformacji danych EDI



<figure><img src="../../../.gitbook/assets/site-all-edi-list-pl.png" alt="Istniejący format EDI z czterema skonfigurowanymi atrybutami."><figcaption><p>Istniejący format EDI z czterema skonfigurowanymi atrybutami.</p></figcaption></figure>

DocBits analizuje surowy komunikat EDI i przekształca go w JSON przy użyciu deskryptora struktury JSON. Następnie tworzy pośredni XML, stosuje XSLT w celu uzyskania standardowego XML i używa go do ekstrakcji pól i tabel oraz do podglądu.

Poniższe przykłady to fragmenty poglądowe, a nie kompletne konfiguracje gotowe do importu. Niektóre pomijają treść lub zawierają symbole zastępcze, takie jak `...`. Dostosuj je i przetestuj z rzeczywistym komunikatem EDI, pośrednim XML i przekształconym wynikiem. Zachowaj identyfikatory pól wymagane przez swoją konfigurację.

## Krok 1: Opisz strukturę EDI

Deskryptor struktury JSON definiuje segmenty takie jak SAC, N1 i PO1, ich pola oraz zagnieżdżone pętle. Określa sposób analizowania surowego komunikatu EDI i tworzenia ustrukturyzowanego JSON.

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

## Krok 2: Przekształć pośredni XML za pomocą XSLT

DocBits konwertuje wynikowy JSON na pośredni XML przed zastosowaniem arkusza transformacji. XSLT odczytuje ten pośredni XML, a nie bezpośrednio JSON, i tworzy standardową strukturę XML do dalszego przetwarzania. Przykład wybiera dane potwierdzenia i warunki z węzłów XML.

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

## Krok 3: Utwórz podgląd HTML

Arkusz stylów podglądu konwertuje przekształcony XML z kroku 2 na HTML. Dostosuj układ i powiązania danych do typu dokumentu oraz sprawdź, czy podgląd prawidłowo przedstawia przekształcone dane.

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

## Krok 4: Skonfiguruj ekstrakcję XPath

Konfiguracja ekstrakcji jest zapisana w JSON, ale jej ścieżki są wyrażeniami XPath wykonywanymi na przekształconym XML z kroku 2. Ścieżki pól wybierają wartości; ścieżka wierszy tabeli wybiera wiersze, a ścieżki kolumn wybierają wartości w poszczególnych wierszach. Nie są to wyrażenia JSONPath.

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

Pełny przebieg to: surowe EDI → ustrukturyzowany JSON → pośredni XML → standardowy XML przez XSLT → ekstrakcja pól i tabel za pomocą XPath oraz podgląd HTML. Sprawdź wynik i wyodrębnione wartości na reprezentatywnych komunikatach przed użyciem konfiguracji w środowisku produkcyjnym.


Widoki przedstawiają istniejącą konfigurację i wersję. Ustawienia różnią się w zależności od typu dokumentu i formatu. Sprawdź zmiany w wersji roboczej przed aktywacją.

Ilustracje przedstawiają polskie karty etapów oraz aktywną wersję konfiguracji w trybie tylko do odczytu. W pokazanej wersji interfejsu przycisk podglądu ma błędny podpis „Zapowiedź”; odpowiada on funkcji podglądu, oznaczonej w karcie jako „Podgląd”. Techniczne nagłówki edytora, identyfikatory atrybutów i kod konfiguracji pozostają w oryginalnej postaci.
