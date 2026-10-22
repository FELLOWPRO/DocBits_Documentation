# WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-overview-it.svg" alt="WatchDog: monitoraggio delle cartelle, elaborazione in DocBits e destinazioni di esportazione."><figcaption><p>WatchDog: monitoraggio delle cartelle, elaborazione in DocBits e destinazioni di esportazione.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/watchdog-infographic-en.png" alt="Infografica di WatchDog"><figcaption></figcaption></figure>

**WatchDog** è un servizio on-premise basato su Windows che monitora le cartelle locali alla ricerca di documenti in arrivo, li carica nel DocBits Cloud per l'elaborazione ed esporta i documenti completati in cartelle locali o sistemi ERP.

## Funzionalità Principali

* **Monitoraggio automatico delle cartelle** — controlla percorsi locali e percorsi di rete UNC alla ricerca di nuovi PDF
* **Supporto multi-configurazione** — più configurazioni di importazione/esportazione per istanza
* **6 metodi di esportazione** — Local Folder, Infor IDM, Infor BOD, ION API, GLS840MI, REST API
* **Aggiornamento automatico** — aggiornamenti di versione automatici con rollback in caso di errore
* **Gestione remota** — riavvio, aggiornamento e configurazione tramite l'interfaccia di DocBits

## Avvio Rapido

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Scheda General di WatchDog"><figcaption></figcaption></figure>

### 1. Scarica WatchDog

Scarica `WatchDog.exe` da **Settings → Document Processing → WatchDog → General Tab** nell'applicazione DocBits.

### 2. Configura tramite API Key

Apri il **Prompt dei comandi come amministratore** ed esegui:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

> **Nota:** L'API Key è disponibile nelle impostazioni di DocBits, nella scheda General di WatchDog. Collega WatchDog alla tua organizzazione DocBits.

### 3. Installa come Servizio Windows

```powershell
WatchDog.exe install
WatchDog.exe start
```

### 4. Crea le Configurazioni in DocBits

Tutte le configurazioni di importazione ed esportazione vengono create direttamente nell'**applicazione DocBits**:

**Impostazioni → Elaborazione documenti → WatchDog → Scheda Configurazioni**

* **Import Configurations** — definiscono le cartelle da monitorare e i tipi di documento
* **Export Configurations** — definiscono le destinazioni di esportazione, i template XSLT e i metodi di esportazione

> **Importante:** Le configurazioni di esportazione richiedono un **tipo di documento** (`doc_type`). Le configurazioni senza tipo di documento verranno rifiutate.

### 5. Avvio Automatico (Facoltativo)

Per avviare WatchDog automaticamente all'avvio del sistema:

1. Apri **Servizi** (`Win + R` → `services.msc`)
2. Trova **WatchDog** nell'elenco
3. Imposta **Tipo di avvio** su **Automatico (avvio ritardato)**

## Riferimento dei Comandi

| Comando | Descrizione |
| :--- | :--- |
| `WatchDog.exe -api KEY` | Configura l'API Key e si connette a DocBits |
| `WatchDog.exe install` | Installa come servizio Windows |
| `WatchDog.exe start` | Avvia il servizio |
| `WatchDog.exe stop` | Arresta il servizio |
| `WatchDog.exe debug` | Esegue in modalità console per la risoluzione dei problemi |
| `WatchDog.exe --version` | Mostra la versione corrente |
| `WatchDog.exe --list-folders` | Elenca le cartelle monitorate configurate |
| `WatchDog.exe remove` | Disinstalla il servizio |

## Ulteriori Risorse

* [Installazione di WatchDog](watchdog-installation.md)
* [Configurazione di WatchDog](watchdog-v2-configuration.md)
* [FAQ per Amministratori di WatchDog](watchdog-admin-faq.md)
