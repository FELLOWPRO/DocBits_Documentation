# EDI Data Transformation Process

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/site-all-edi-list-en.png" alt="Existing EDI format with its four configured attributes."><figcaption><p>Existing EDI format with its four configured attributes.</p></figcaption></figure>

DocBits parses the raw EDI message into JSON using a JSON structure descriptor. It then creates intermediate XML, applies XSLT to produce the standard XML, and uses that XML for field/table extraction and the preview.

The examples below are illustrative fragments, not complete configurations ready to import. Some omit content or contain placeholders such as `...`. Adapt and test them against your actual EDI message, intermediate XML and transformed output; retain the field identifiers required by your configuration.

## Step 1: Describe the EDI structure

The JSON structure descriptor defines segments such as SAC, N1 and PO1, their fields and nested loops. It controls how the raw EDI message is parsed into structured JSON.

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

## Step 2: Transform intermediate XML with XSLT

DocBits converts the parsed JSON to intermediate XML before applying the transformation stylesheet. XSLT reads this intermediate XML, not the JSON directly, and produces the standard XML structure used for further processing. The example selects acknowledgement data and conditions from XML nodes.

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

## Step 3: Build an HTML preview

A preview stylesheet converts the transformed XML from step 2 to HTML. Adapt its layout and data bindings to the document type and verify that the preview represents the transformed data correctly.

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

## Step 4: Configure XPath extraction

The extraction configuration is stored in JSON, but its paths are XPath expressions evaluated against the transformed XML from step 2. Field paths select values; a table row path selects rows, and column paths select values within each row. These are not JSONPath expressions.

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

The complete flow is raw EDI → structured JSON → intermediate XML → standard XML through XSLT → field/table extraction with XPath and an HTML preview. Validate the output and extracted values with representative messages before using a configuration in production.


The views show an existing configuration and version. Settings vary by document type and format. Validate changes in a draft before activation.
