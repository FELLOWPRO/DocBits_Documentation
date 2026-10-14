# SQL Access

<figure><img src="../.gitbook/assets/docbits_sql_access_overview.png" alt="Docbits Sql Access Overview"><figcaption></figcaption></figure>

## Overview

In the DocBits settings module, administrators can directly access the BI database using SQL. This feature is designed for advanced data management and custom reporting needs.

### Accessing SQL Direct Access

Navigate to the SQL Direct Access section in the settings module. Here, you will find credentials and access details, including username, password, database name, and host information.

* **Username:** user\_23f3d6
* **Password:** _Encrypted_
* **Database:** demo
* **Host:** see in the Screenshot

## **Example Access Details:**

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

#### Results of a Sample Query

The following results display the number of documents by their respective status and invoice type:

* **Ready for Validation:** 71 Invoices, 6 unspecified
* **Pending Confirmation:** 1 unspecified
* **Finished:** 3 unspecified, 1 Invoice
* **Error:** 2 unspecified

#### Using clickhouse-client for Terminal Access

For developers preferring terminal usage, access can be established via `clickhouse-client`:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Creating Materialized Views

We recommend creating materialized views for pre-calculating data to enhance performance in analytics tools like PowerBI:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

This example shows how to group total amounts by the week they were created, which is useful for weekly financial summaries or audit trails.

## Additional Resources

For further assistance or advanced configurations, please consult our support team or access our comprehensive video training available in the help section.
