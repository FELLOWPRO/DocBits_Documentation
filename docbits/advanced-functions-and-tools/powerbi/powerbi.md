---
description: Connect Power BI to ClickHouse through ODBC
---

# Connect via ClickHouse

Use this guide when your DocBits organization has ClickHouse access enabled and an administrator has supplied the connection parameters. Availability depends on your installation and permissions.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

## 1. Install the driver

Install the [official ClickHouse ODBC driver](https://github.com/ClickHouse/clickhouse-odbc). Match the driver's architecture to Power BI Desktop and install its required dependencies.

## 2. Configure an ODBC data source

Open Windows ODBC Data Source Administrator for the matching architecture. Add a system DSN using the ClickHouse driver and give it a descriptive name.

Enter the server, port, database, username and password provided for your organization's ClickHouse access. Use the endpoint and TLS settings supplied by your administrator; do not assume a PostgreSQL endpoint or copy example credentials. Consult the driver's configuration documentation for the fields supported by your installed version. Test the connection if the driver provides a test function.

## 3. Connect from Power BI Desktop

Choose **Get data → ODBC**, select your DSN and authenticate using the method appropriate to its configuration. In Navigator, select the required tables or views. Choose **Load** to import them or **Transform Data** to prepare them in Power Query.

For authentication failures, verify the DSN and the supplied credentials. Enter the real password in the credential dialog; connection-string escaping is separate driver syntax.

## 4. Build and validate the report

Check the data types, date interpretation and row counts before building visuals. Apply filters or aggregations needed for the report and compare a small sample with the source data. Access is limited to the data and permissions granted to your account.

## 5. Configure refresh when required

Publish the report to Power BI Service when it is ready. Scheduled refresh depends on the workspace license/capacity and the connection mode. Configure a reachable gateway for the ODBC source, including the appropriate driver, DSN and credentials. Run a refresh and inspect its history before relying on the schedule.

[ODBC connector documentation](https://learn.microsoft.com/en-us/power-query/connectors/odbc) · [Scheduled refresh documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
