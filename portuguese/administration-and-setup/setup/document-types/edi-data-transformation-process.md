# EDI Data Transformation Process

####

<figure><img src="../../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Imagem 4"><figcaption></figcaption></figure>

#### Step 1: Structure Descriptor

* **Format**: JSON
* **Purpose**: This step involves defining the structure of the EDI data. It includes specifying segments such as `SAC`, `N1`, and `PO1`, and details the fields contained within each segment. For segments that contain nested structures, loops are defined to properly organize the data hierarchy.

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

#### Step 2: Transformation Using XSLT

* **Format**: XSLT
* **Purpose**: This step involves transforming the structured JSON data into a structured XML format, specifically tailoring the output to meet the requirements for further processing or integration. This transformation helps in extracting precise information like acknowledgement types, order details, and conditional elements based on specific values.

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

#### Step 3: Preview (HTML Conversion)

* **Format**: XSLT (outputting HTML)
* **Purpose**: Converts the XML data from Step 2 into an HTML format for previewing the transformed data in a readable and visually appealing format. The HTML layout includes styles for presentation and structures data like purchase orders, supplier details, and order terms for easy viewing.

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

#### Step 4: Extraction Paths

* **Format**: JSON
* **Purpose**: Specifies JSON paths for extracting key values from the XML data produced in Step 2. These paths are used to retrieve specific data points such as purchase orders and currency, which are crucial for downstream processing and integration into other systems.

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

This updated sequence ensures a thorough process, transforming raw EDI data into structured, actionable information using JSON for data structuring, XSLT for transformation and HTML preview, followed by JSON paths for data extraction and integration.
