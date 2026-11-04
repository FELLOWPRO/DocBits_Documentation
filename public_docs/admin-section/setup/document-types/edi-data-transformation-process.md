---
układ:
tytuł:
widoczny: true
opis:
widoczny: true
spisTreści:
widoczny: true
szkic:
widoczny: true
paginacja:
widoczny: true
---

# Proces transformacji danych EDI

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Obraz 4"><figcaption></figcaption></figure>

#### Krok 1: Deskryptor Struktury

* **Format**: JSON
* **Cel**: Ten krok polega na zdefiniowaniu struktury danych EDI. Obejmuje określenie segmentów takich jak `SAC`, `N1` i `PO1`, oraz szczegółowe informacje o polach zawartych w każdym segmencie. Dla segmentów zawierających zagnieżdżone struktury, definiowane są pętle w celu właściwej organizacji hierarchii danych.
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
#### Krok 2: Transformacja za pomocą XSLT

* **Format**: XSLT
* **Cel**: Ten krok polega na przekształceniu strukturalnych danych JSON w strukturalny format XML, specjalnie dostosowując wynik, aby spełnić wymagania dalszego przetwarzania lub integracji. Ta transformacja pomaga w wydobyciu precyzyjnych informacji, takich jak typy potwierdzeń, szczegóły zamówienia i elementy warunkowe na podstawie określonych wartości.
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
#### Krok 3: Podgląd (Konwersja HTML)

* **Format**: XSLT (wyjście HTML)
* **Cel**: Konwertuje dane XML z Kroku 2 na format HTML w celu podglądu przekształconych danych w czytelnej i atrakcyjnej wizualnie formie. Układ HTML zawiera style prezentacji i strukturyzuje dane, takie jak zamówienia zakupu, szczegóły dostawcy i warunki zamówienia, aby ułatwić przeglądanie.
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
#### Krok 4: Ścieżki Wyodrębniania

* **Format**: JSON
* **Cel**: Określa ścieżki JSON do wyodrębniania kluczowych wartości z danych XML wygenerowanych w kroku 2. Te ścieżki są używane do pobierania konkretnych punktów danych, takich jak zamówienia zakupu i waluta, które są kluczowe dla przetwarzania w dół i integracji z innymi systemami.
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
To zaktualizowana sekwencja zapewnia dokładny proces przekształcania surowych danych EDI w uporządkowane, działania informacje, używając JSON do strukturyzacji danych, XSLT do transformacji i podglądu HTML, a następnie ścieżek JSON do ekstrakcji danych i integracji.
