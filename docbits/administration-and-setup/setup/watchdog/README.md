# WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-overview-infographic.svg" alt="WatchDog Overview"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-infographic-en.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

**WatchDog** is a Windows-based on-premise service that monitors local folders for incoming documents, uploads them to the DocBits Cloud for processing, and exports finished documents back to local folders or ERP systems.

## Video walkthrough

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/product-tours/watchdog/2026-10-28/v1/en.mp4" %}

*1:45 min · Product UI in English · AI-generated voice and intro scene*

[Captions (VTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/product-tours/watchdog/2026-10-28/v1/en.vtt) · [Download video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/product-tours/watchdog/2026-10-28/v1/en.mp4)

## Key Features

* **Automatic folder monitoring** — watches local paths and UNC network paths for new PDFs
* **Multi-config support** — multiple import/export configurations per instance
* **6 export methods** — Local Folder, Infor IDM, Infor BOD, ION API, GLS840MI, REST API
* **Auto-Update** — automatic version updates with rollback on failure
* **Remote management** — restart, update, and configure via DocBits UI

## Quick Start

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="WatchDog General Tab"><figcaption></figcaption></figure>

### 1. Download WatchDog

Download `WatchDog.exe` from **Settings → Document Processing → WatchDog → General Tab** in the DocBits application.

### 2. Configure via API Key

Open **Command Prompt as Administrator** and run:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

> **Note:** The API Key is available in your DocBits Settings under the WatchDog General Tab. This connects WatchDog to your DocBits organisation.

### 3. Install as Windows Service

```powershell
WatchDog.exe install
WatchDog.exe start
```

### 4. Create Configurations in DocBits

All import and export configurations are created directly in the **DocBits application**:

**Settings → Document Processing → WatchDog → Configurations Tab**

* **Import Configurations** — define watch folders and document types
* **Export Configurations** — define export destinations, XSLT templates, and export methods

> **Important:** Export configurations require a **document type** (`doc_type`). Configurations without a document type will be rejected.

### 5. Auto Start (Optional)

To start WatchDog automatically on boot:

1. Open **Services** (`Win + R` → `services.msc`)
2. Find **WatchDog** in the list
3. Set **Startup Type** to **Automatic (Delayed Start)**

## Command Reference

| Command | Description |
| :--- | :--- |
| `WatchDog.exe -api KEY` | Configure API Key and connect to DocBits |
| `WatchDog.exe install` | Install as Windows Service |
| `WatchDog.exe start` | Start the service |
| `WatchDog.exe stop` | Stop the service |
| `WatchDog.exe debug` | Run in console mode for troubleshooting |
| `WatchDog.exe --version` | Show current version |
| `WatchDog.exe --list-folders` | List configured watch folders |
| `WatchDog.exe remove` | Uninstall the service |

## Further Resources

* [WatchDog Installation](watchdog-installation.md)
* [WatchDog Configuration](watchdog-v2-configuration.md)
* [WatchDog Admin FAQ](watchdog-admin-faq.md)

## Screenshots

<figure><img src="../../../.gitbook/assets/watchdog-general-en.png" alt="Status and getting started"><figcaption><p>Status and getting started</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-configurations-en.png" alt="Configurations overview"><figcaption><p>Configurations overview</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-import-dialog-en.png" alt="New import configuration"><figcaption><p>New import configuration</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-import-filled-en.png" alt="Import configuration filled in"><figcaption><p>Import configuration filled in</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-import-saved-en.png" alt="Import configuration saved"><figcaption><p>Import configuration saved</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-export-dialog-en.png" alt="New export configuration"><figcaption><p>New export configuration</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-export-filled-en.png" alt="Export configuration with a webhook as target"><figcaption><p>Export configuration with a webhook as target</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-xslt-en.png" alt="XSLT templates"><figcaption><p>XSLT templates</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-xslt-new-en.png" alt="Manage XSLT templates"><figcaption><p>Manage XSLT templates</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-logs-en.png" alt="WatchDog logs"><figcaption><p>WatchDog logs</p></figcaption></figure>
