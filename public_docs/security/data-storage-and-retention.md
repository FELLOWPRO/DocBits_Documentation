# Data Storage, Retention and Deletion

Your data is in good hands with DocBits. We operate DocBits in two regions, **Frankfurt am Main (EU)** and **San Francisco (USA)**, and you decide in your settings how long documents stay with us. This page covers storage locations, retention periods and deletion.

**Documentation as of: 28 October 2026.**

## At a glance

- **You choose the region:** Frankfurt for EU customers, San Francisco for US customers.
- **Your data stays in your region.** EU data is hosted in Frankfurt, US data in San Francisco. There is no mixing of data across regions.
- **You control how long your documents are kept** under **Document Processing → Documents Expiry** ([go to the setting](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Temporary OCR files** are deleted automatically after 90 minutes.
- **We are happy to help:** our team answers questions and deletion requests at **compliance@fellowpro.com**.

## Where is your data stored?

| Region | For whom | Location | Services used |
| --- | --- | --- | --- |
| **EU** | All EU customers | **Frankfurt am Main, Germany** | DigitalOcean Kubernetes (region `fra1`) with managed PostgreSQL, OpenSearch and Valkey databases (`fra1`), plus DigitalOcean Spaces for file storage |
| **USA** | US customers | **San Francisco, USA** | DigitalOcean Kubernetes (region `sfo2`) with managed PostgreSQL, OpenSearch and Valkey databases (`sfo2`) |

**Backups in the EU:** Frankfurt is the primary backup location and Amsterdam (Netherlands) the secondary one, so your backup copies also stay within the EU.

**Connected systems:** If you export documents to your ERP, Infor IDM or another target system, those copies are stored there under that system's rules and at that system's location. That stays in your own hands.

## How long is data kept?

| Data type | Retention |
| --- | --- |
| **Uploaded documents and extracted data** | Controlled by you through [Documents Expiry](../administration-and-setup/settings/document-processing/documents-expiry.md) (see below). |
| **Temporary OCR files** | Automatic cleanup after **90 minutes**. This applies only to temporary OCR storage, not to your document in DocBits. |
| **Customer-accessible logs** (viewable under [Activity Logging](../administration-and-setup/settings/log-settings/README.md)) | **30 days** |
| **Internal logs** | **3 months** |
| **Daily database backups (managed)** | **7 days**; older backups are removed automatically. |
| **Additional daily backups (SnapShooter)** | For production and sandbox databases; retention is set per environment. |
| **Cookies and browser storage** | Varies by purpose, see [Cookies and Browser Storage](cookies-and-browser-storage.md). |

We also back up daily, weekly, quarterly and yearly. We are happy to give you the exact retention periods for these backup types for your environment on request.

## How to set the retention of your documents

In Settings, open **Document Processing → Documents Expiry**. There are two settings:

- **Delete document after:** how long documents are kept.
- **Delete finished document after:** how long finished, fully processed and exported documents are kept.

The options are **Default**, **48 Hours**, **1 Week**, **2 Weeks** and **4 Weeks**. **Default** applies the system default. If you want a fixed period, simply pick one of the durations. Full details are in the [Documents Expiry guide](../administration-and-setup/settings/document-processing/documents-expiry.md).

## What happens when data is deleted?

Documents Expiry deletes your documents automatically after the period you chose. This is independent of the cleanup of temporary OCR files, the expiry of logs and the retention of backups.

Good to know:

- **Backups expire on their own schedule.** Deleting a document in the live system therefore does not remove backup copies immediately, but when the respective backup period ends.
- **Exported copies are yours.** When DocBits deletes a document, the copy in your ERP or archive remains. Plan retention there to match your own requirements.

## Questions or deletion requests? We are here for you

For information about your deployment or a deletion request, write to us at **compliance@fellowpro.com**. Please tell us your organization, the environment concerned, the data type and the scope you need. Please do not send passwords or API keys.

We are also glad to confirm:

- Your active region and effective retention settings, including the system default.
- When the deletion period starts and how often cleanup runs.
- Deletion scope for documents, extracted data, search indexes and derived data.
- Locations and retention periods of all backup types, including after contract end.

## More security information

- [Security and Compliance: locations, logs and retention](security-and-compliance-faq.md)
- [Encryption at Rest and backup scope](encryption-at-rest.md)
- [Secure Storage of Credentials](secure-storage-of-credentials.md)
- [Cookies and Browser Storage](cookies-and-browser-storage.md)
