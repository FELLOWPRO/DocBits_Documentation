# EDI 数据转换流程

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/EDI.png" alt=""><figcaption></figcaption></figure>

#### 第 1 步：结构描述符

* **格式**：JSON
* **用途**：此步骤用于定义 EDI 数据的结构，包括指定 `SAC`、`N1` 和 `PO1` 等段，并详细说明每个段包含的字段。对于包含嵌套结构的段，会定义循环以妥善组织数据层级。

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

#### 第 2 步：使用 XSLT 进行转换

* **格式**：XSLT
* **用途**：此步骤用于将结构化 JSON 数据转换为结构化 XML 格式，并根据后续处理或集成的要求定制输出。此转换有助于提取确认类型、订单详情以及根据特定值确定的条件元素等精确信息。

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

#### 第 3 步：预览（HTML 转换）

* **格式**：XSLT（输出 HTML）
* **用途**：将第 2 步生成的 XML 数据转换为 HTML 格式，以便以清晰且直观的方式预览转换后的数据。HTML 布局包含用于展示的样式，并将采购订单、供应商详情和订单条款等数据进行结构化，便于查看。

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

#### 第 4 步：提取路径

* **格式**：JSON
* **用途**：指定用于从第 2 步生成的 XML 数据中提取关键值的 JSON 路径。这些路径用于检索采购订单和货币等特定数据点，这些数据对于后续处理以及集成到其他系统至关重要。

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

这一更新后的流程确保了完整的处理过程：使用 JSON 对原始 EDI 数据进行结构化，使用 XSLT 进行转换并生成 HTML 预览，随后通过 JSON 路径提取数据并进行集成，最终将其转换为结构化且可操作的信息。
