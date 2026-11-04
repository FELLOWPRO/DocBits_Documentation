# EDI 数据转换流程

{% embed url="https://youtu.be/OmYbGG0ea0w?si=7okB6WP8kiKIZuec" %}

<figure><img src="../../../.gitbook/assets/site-all-edi-list-zh.png" alt="EDI 配置中的转换、提取路径、预览及结构描述入口。"><figcaption><p>EDI 配置中的转换、提取路径、预览及结构描述入口。</p></figcaption></figure>

DocBits 使用 JSON 结构描述符，将原始 EDI 消息解析为 JSON。随后生成中间 XML，使用 XSLT 将其转换为标准 XML，再使用该 XML 提取字段和表格并生成预览。

以下示例是用于说明的片段，并非可直接导入的完整配置。部分示例省略了内容或包含 `...` 等占位符。请根据实际的 EDI 消息、中间 XML 和转换结果进行调整和测试，并保留配置所需的字段标识符。

## 步骤 1：描述 EDI 结构

JSON 结构描述符定义 SAC、N1 和 PO1 等段、各段的字段以及嵌套循环。它决定如何将原始 EDI 消息解析为结构化 JSON。

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

## 步骤 2：使用 XSLT 转换中间 XML

DocBits 在应用转换样式表之前，先将解析得到的 JSON 转换为中间 XML。XSLT 读取的是中间 XML，而非直接读取 JSON，并生成供后续处理使用的标准 XML 结构。示例从 XML 节点中选择确认信息和条件。

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

## 步骤 3：生成 HTML 预览

预览样式表将步骤 2 中转换后的 XML 转换为 HTML。请根据文档类型调整布局和数据绑定，并检查预览是否正确显示转换后的数据。

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

## 步骤 4：配置 XPath 提取

提取配置以 JSON 格式存储，但其中的路径是针对步骤 2 中转换后的 XML 求值的 XPath 表达式。字段路径选择值；表格行路径选择行，列路径则选择每行中的值。这些不是 JSONPath 表达式。

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

完整流程为：原始 EDI → 结构化 JSON → 中间 XML → 通过 XSLT 生成标准 XML → 使用 XPath 提取字段和表格并生成 HTML 预览。在生产环境使用配置前，请使用有代表性的消息验证输出和提取值。


这些视图显示现有配置及其版本。设置因文档类型和格式而异。请在草稿中验证更改后再激活。

图片展示中文流程卡片和只读配置。在所示版本中，Active 状态误译为“积极的”，实际表示已生效。技术编辑器标题、属性标识符及配置代码保留原文。
