---
description: "如何配置 PowerBI"
---

# 将 DocBits 连接到 Power BI

您可以通过两种不同的方式将 DocBits 数据连接到 Power BI。合适的方法取决于您希望如何使用这些数据。

{% embed url="https://youtu.be/O1MtuXf_R_M" %}

### 如何选择连接方式：

* **方法 1：通过 ClickHouse 连接**
  * **分析大量数据**。
  * **历史趋势和仪表板**。

{% content-ref url="powerbi.md" %}
[通过 ClickHouse 连接](powerbi.md)
{% endcontent-ref %}

* **方法 2：通过只读数据库连接**
  * **运营数据或近实时数据**。
  * **直接访问当前 DocBits 表**。

{% content-ref url="connect-via-read-only-database.md" %}
[通过只读数据库连接](connect-via-read-only-database.md)
{% endcontent-ref %}
