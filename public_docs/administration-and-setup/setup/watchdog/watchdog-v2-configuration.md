# WatchDog Configuration

**Legacy V2 versus current V3 configuration**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-configuration-management-part1/v1/en.mp4" %}

**Importing a V2 file and creating an import configuration**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-configuration-management-part2/v1/en.mp4" %}

**BOD mapping, overlaps and export settings**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-configuration-management-part3/v1/en.mp4" %}

**How WatchDog fetches and reloads configuration**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-configuration-management-part4/v1/en.mp4" %}

This guide explains how to configure the WatchDog service within the DocBits application. All configurations are managed directly in **Settings → Document Processing → WatchDog**.

<figure><img src="../../../.gitbook/assets/watchdog-v2-config-infographic.svg" alt="WatchDog Configuration Overview"><figcaption></figcaption></figure>

---

## 1. General Tab

**The idea, the General tab and the commands**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-remote-management-part1/v1/en.mp4" %}

**Restart, update and how commands travel**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-remote-management-part2/v1/en.mp4" %}

**Safety rules, restart files and audit trail**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-remote-management-part3/v1/en.mp4" %}

The General tab provides setup instructions, download links, and update settings.

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="WatchDog General Tab"><figcaption></figcaption></figure>

### 1.1 Download & Setup

* Download the latest `WatchDog.exe` directly from the General tab
* Copy the displayed API Key
* Run the configuration command in an Administrator Command Prompt:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

### 1.2 Auto-Update Schedule

**Where updates come from and the release channel**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-auto-update-part1/v1/en.mp4" %}

**Automatic and manual updates, step by step**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-auto-update-part2/v1/en.mp4" %}

**Health check, rollback and after the update**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-auto-update-part3/v1/en.mp4" %}

| Option | Interval |
| :--- | :--- |
| On Startup Only | Check once at start |
| Hourly | Every 3600 seconds |
| Daily | Every 86400 seconds |
| Weekly | Every 604800 seconds |

---

## 2. Configurations Tab

Create and manage import and export configurations. All configurations are created directly in DocBits — no local config files needed.

<figure><img src="../../../.gitbook/assets/watchdog_v2_03.png" alt="WatchDog Configurations Overview"><figcaption></figcaption></figure>

### 2.1 Import Configurations

**Setting up an import and how WatchDog notices files**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-import-part1/v1/en.mp4" %}

**Complete files, retries and file types**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-import-part2/v1/en.mp4" %}

**Infor BOD files and where files go afterwards**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-import-part3/v1/en.mp4" %}

**Folder checks and recap**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-import-part4/v1/en.mp4" %}

Define where WatchDog monitors for new documents.

<figure><img src="../../../.gitbook/assets/watchdog_v2_02.png" alt="WatchDog Import Configuration"><figcaption></figcaption></figure>

| Field | Description |
| :--- | :--- |
| **Name** | Display name for this configuration |
| **Watch Folder** | Directory to monitor for new documents (required) |
| **Success Folder** | Where files are moved after successful import |
| **Document Type** | INVOICE, CREDIT\_NOTE, PURCHASE\_ORDER, etc. |
| **Sub-Organisation** | Optional — route documents to a specific sub-org |

### 2.2 Export Configurations

**Export basics: finding work and matching configurations**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-export-part1/v1/en.mp4" %}

**Folder and Infor exports**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-export-part2/v1/en.mp4" %}

**GLS840MI and REST API exports**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-export-part3/v1/en.mp4" %}

**Export status and recap**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-file-export-part4/v1/en.mp4" %}

Define how and where processed documents are exported.

> **Important:** Export configurations now **require a document type** (`doc_type`). Configurations without a document type will be rejected by the system.

| Field | Description |
| :--- | :--- |
| **Name** | Display name for this configuration |
| **Document Type** | Required — INVOICE, CREDIT\_NOTE, etc. |
| **Export Method** | How documents are exported (see below) |
| **Export Folder** | Target directory for folder exports |
| **Execution Order** | Priority when multiple configs match (default: 1) |
| **XSLT Template** | Optional — XML transformation template |

### 2.3 Export Methods

| Method | Description |
| :--- | :--- |
| **Folder (watcher)** | Export PDF + XML to a local folder |
| **Infor IDM** | Upload to Infor Document Management |
| **Infor BOD** | Send BOD XML to Infor LN/M3 |
| **ION API** | Call Infor ION API endpoints |
| **GLS840MI** | M3 batch processing (via REST API) |
| **REST API** | Send to external API with ION OAuth authentication |

<figure><img src="../../../.gitbook/assets/watchdog_v2_04.png" alt="WatchDog Export Configuration"><figcaption></figcaption></figure>

### 2.4 Processing Options

* **Barcode Divider:** Automatically split multi-page documents based on barcodes
* **DocBits Operator:** Enable browser automation tasks

---

## 3. Status Tab

**Heartbeat and the status card**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-monitoring-logging-part1/v1/en.mp4" %}

**Local logs and what is sent to DocBits**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-monitoring-logging-part2/v1/en.mp4" %}

**Crash detection, alerts and the Logs tab**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-monitoring-logging-part3/v1/en.mp4" %}

Monitor WatchDog service health and activity.

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="WatchDog Service Status"><figcaption></figcaption></figure>

### Status Information

| Field | Description |
| :--- | :--- |
| **Online/Offline** | Current connection status (30s heartbeat threshold) |
| **Version** | Installed WatchDog version |
| **Version First Seen** | When this version was first reported |
| **Last Restart** | Timestamp of last service restart |
| **Auto-Update Enabled** | Whether automatic updates are active |
| **Latest Version** | Newest available version |
| **Latest Version Checked At** | When the latest version was last checked |
| **System Info** | Installation path, free RAM, free disk space |

### Health Indicator

| Status | Meaning |
| :--- | :--- |
| ✅ **Online** | WatchDog is connected and active |
| ⚠️ **Offline** | No heartbeat received for 30+ seconds |
| ❌ **Not Installed** | WatchDog has never connected to this organisation |

---

## 4. Logs Tab

View all WatchDog events stored in OpenSearch.

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="WatchDog Logs"><figcaption></figcaption></figure>

* Filter by date, event type, or keywords
* Event types: `FILE_IMPORT_STARTED`, `FILE_IMPORT_COMPLETED`, `FILE_IMPORT_FAILED`, `EXPORT_STARTED`, `EXPORT_COMPLETED`, `EXPORT_FAILED`, `FOLDER_VALIDATION_FAILED`, `CONFIG_LOADED`, `SERVICE_RESTART_INITIATED`, `SERVICE_RESTART_COMPLETED`

---

## 5. XSLT Templates Tab

**What a template is, creating and validating**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-xslt-templates-part1/v1/en.mp4" %}

**Field analysis, security and the template input**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-xslt-templates-part2/v1/en.mp4" %}

**Assigning templates, export-time process and API**

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/watchdog-xslt-templates-part3/v1/en.mp4" %}

Manage XSLT transformation templates used for XML exports.

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="XSLT Templates List"><figcaption></figcaption></figure>

* Upload and edit XSLT templates
* **Live validation** — test templates against sample XML with field analysis
* Link templates to export configurations
* View usage count (which configs use each template)

<figure><img src="../../../.gitbook/assets/watchdog_v2_07.png" alt="XSLT Template Editor"><figcaption></figcaption></figure>

---

## 6. Export Configurations Tab

Overview of all active export configurations with connection status.

* Monitor the last successful connection timestamp
* Manage configurations inline (edit, copy, delete)
* Bulk copy configurations across sub-organisations
