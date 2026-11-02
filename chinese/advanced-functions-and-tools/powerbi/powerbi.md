---
description: 通过 ODBC 将 Power BI 连接到 ClickHouse
---

# 通过 ClickHouse 连接

仅在您的 DocBits 组织已启用 ClickHouse 访问、且管理员已提供连接参数时使用本指南。功能是否可用取决于安装版本和权限。

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

## 1. 安装驱动程序

安装 [ClickHouse 官方 ODBC 驱动程序](https://github.com/ClickHouse/clickhouse-odbc)。驱动程序的架构必须与 Power BI Desktop 匹配，并应安装所需的依赖项。

## 2. 配置 ODBC 数据源

打开架构匹配的 Windows ODBC 数据源管理器，使用 ClickHouse 驱动程序添加系统 DSN，并设置便于识别的名称。

填写管理员为您的组织提供的 ClickHouse 服务器、端口、数据库、用户名和密码。使用指定的端点和 TLS 设置，不要误用 PostgreSQL 端点或照抄示例凭据。具体字段取决于已安装的驱动程序版本，请查阅其配置文档。如果驱动程序提供测试功能，请先测试连接。

## 3. 在 Power BI Desktop 中连接

选择**获取数据 → ODBC**，选择配置好的 DSN，并使用与其配置相符的身份验证方式。在导航器中选择所需的表或视图，选择**加载**进行导入，或选择**转换数据**在 Power Query 中处理数据。

如果身份验证失败，请检查 DSN 和管理员提供的凭据。在凭据对话框中输入实际密码；连接字符串的转义属于单独的驱动程序语法。

## 4. 创建并核对报表

创建可视化之前，检查数据类型、日期解释和行数。按报表需要设置筛选或汇总，并抽取少量数据与源数据核对。可读取的数据范围取决于该账号获得的访问权限。

## 5. 按需配置刷新

报表准备好后，可发布到 Power BI Service。计划刷新取决于工作区的许可证或容量及连接模式。为 ODBC 数据源配置可访问的网关，并准备匹配的驱动程序、DSN 和凭据。启用日常计划之前，先执行刷新并检查刷新历史记录。

[ODBC 连接器文档](https://learn.microsoft.com/en-us/power-query/connectors/odbc) · [计划刷新文档](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
