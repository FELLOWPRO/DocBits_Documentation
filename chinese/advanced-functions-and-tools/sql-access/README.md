# SQL 访问

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="SQL 直接访问设置"><figcaption></figcaption></figure>

## 概述

在 DocBits 设置模块中，管理员可以使用 SQL 直接访问 BI 数据库。此功能面向高级数据管理和自定义报告需求。

### 访问 SQL 直接访问

前往设置模块中的 SQL Direct Access 部分。在这里，您可以找到凭据和访问信息，包括用户名、密码、数据库名称和主机信息。

* **用户名：** user\_23f3d6
* **密码：** _已加密_
* **数据库：** demo
* **主机：** 请参阅截图

## **示例访问信息：**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### 示例查询结果

以下结果显示了按状态和发票类型统计的文档数量：

* **待验证：** 71 张发票，6 个未指定类型
* **待确认：** 1 个未指定类型
* **已完成：** 3 个未指定类型，1 张发票
* **错误：** 2 个未指定类型

#### 使用 clickhouse-client 通过终端访问

对于偏好使用终端的开发人员，可以通过 `clickhouse-client` 建立访问：

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### 使用 SELECT 进行汇总的示例

以下查询汇总已有行，并不会创建物化视图。只读访问不提供创建物化视图所需的写入权限。请根据实际表结构、数字格式和币种调整表名及转换方式；不要在未明确换算的情况下累加不同币种。

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

此示例展示了如何按创建周汇总总金额，可用于每周财务汇总或审计跟踪。

## 其他资源

如需进一步协助或高级配置，请联系支持团队，或在帮助部分观看我们提供的完整视频培训。
