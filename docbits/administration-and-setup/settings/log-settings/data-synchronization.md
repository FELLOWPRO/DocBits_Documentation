# Data Synchronization

Use this overview when DocBits cannot find a supplier, purchase order or other expected master-data record. It shows the recorded synchronization time per data type in the current organization, rather than the contents of every imported record.

## Check synchronization

1. Confirm the intended organization, relevant sub-organization and source ERP company.
2. Open **Settings → Activity Logging → Data Synchronization**. Older layouts place it under **Log Settings**.
3. Find the relevant **Data Type** and read its **Last Synchronization Time** using your configured date format. Newest updates appear first.
4. Compare that time with the expected source change. A recent supplier update says nothing about purchase-order freshness.
5. Find the actual missing identifier in the appropriate master-data or PO view. Compare company, supplier/PO number and line identifiers with the source.
6. For missing or outdated data, inspect the import channel and its logs. Check the outgoing source message, destination organization, mapping and response. Correct the integration cause; this overview has no start or retry button.
7. After the corrected update, reload this overview and reopen the lookup or document. Verify both the time and the actual record values.

## Interpret the result

| Observation | Next check |
| --- | --- |
| No rows | Organization, import setup and whether any synchronization was recorded. Empty does not mean successful. |
| One old data type | Trace that type independently of other rows. |
| Old-data warning | The current warning can appear with no rows or when all updates are older than two weeks. Your process may require much fresher data. |
| Recent time, missing record | Source scope, identifiers, message contents, mapping and response. The timestamp does not prove completeness. |

For support, retain environment, organization, data type, affected identifier, expected update time and the exact error or trace ID, with relevant sanitized evidence.

See [Importing Master Data](../../../infor-integration-and-configuration/importing-customer-master-data/README.md), [Activity Logging](README.md) and [Master Data Lookup](../document-processing/master-data-lookup.md).
