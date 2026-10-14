# FAQ per Amministratori di WatchDog e Risoluzione dei Problemi

<figure><img src="../../../.gitbook/assets/watchdog-troubleshooting-infographic.svg" alt="Riferimento rapido per la risoluzione dei problemi di WatchDog"><figcaption></figcaption></figure>

Questa documentazione aiuta gli amministratori a comprendere i messaggi di errore di WatchDog e a risolvere i problemi.

**Posizione nell'interfaccia:** Settings → Document Processing → WatchDog

---

## 1. Pagine delle Impostazioni di WatchDog (Interfaccia)

### 1.1 Scheda General

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Scheda General di WatchDog"><figcaption></figcaption></figure>

* **Download:** Scarica l'ultima versione di WatchDog.exe
* **API Key:** Copia il comando di configurazione
* **Auto-Update Schedule:** Configura la frequenza degli aggiornamenti
* **Installation Guide:** Istruzioni di configurazione passo dopo passo

### 1.2 Scheda Configurations

* **Import Configurations:** Definiscono le cartelle da monitorare e i tipi di documento
* **Export Configurations:** Definiscono le destinazioni e i metodi di esportazione
* **Bulk Copy:** Copia le configurazioni tra le sub-organizzazioni
* **Import/Export:** Importa/esporta le configurazioni come JSON

> **Importante:** Le configurazioni di esportazione ora **richiedono un tipo di documento** (`doc_type`). Le configurazioni senza un tipo di documento valido verranno rifiutate.

### 1.3 Scheda Status

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="Stato del servizio WatchDog"><figcaption></figcaption></figure>

* Mostra in tempo reale lo stato di connessione di WatchDog
* **Nuovi campi:** `last_restart`, `version_first_seen`, `latest_version_checked_at`
* **Informazioni di sistema:** percorso di installazione, RAM libera, spazio libero su disco

### 1.4 Scheda Logs

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Log di WatchDog"><figcaption></figcaption></figure>

* Mostra tutti gli eventi di WatchDog provenienti da OpenSearch
* Filtrabile per tipo di evento, periodo di tempo, ecc.
* **Tipi di evento:**
  * `FILE_IMPORT_STARTED`: Importazione del file avviata
  * `FILE_IMPORT_COMPLETED`: Importazione riuscita
  * `FILE_IMPORT_FAILED`: Importazione non riuscita
  * `EXPORT_STARTED`: Esportazione avviata
  * `EXPORT_COMPLETED`: Esportazione riuscita
  * `EXPORT_FAILED`: Esportazione non riuscita
  * `FOLDER_VALIDATION_FAILED`: Cartella non raggiungibile
  * `CONFIG_LOADED`: Configurazione caricata
  * `SERVICE_RESTART_INITIATED`: Riavvio del servizio richiesto
  * `SERVICE_RESTART_COMPLETED`: Servizio riavviato

### 1.5 Scheda XSLT Templates

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Elenco dei template XSLT"><figcaption></figcaption></figure>

* Carica e gestisci i template di trasformazione XSLT
* Validazione in tempo reale con analisi dei campi
* Collega i template alle configurazioni di esportazione

---

## 2. Messaggi di Errore di Validazione delle Cartelle

| Errore | Significato | Soluzione |
| :--- | :--- | :--- |
| `not_found` | La cartella non esiste | Crea la cartella o correggi il percorso |
| `no_read_access` | Nessun permesso di lettura | Imposta i permessi per l'account di servizio di WatchDog |
| `no_write_access` | Nessun permesso di scrittura | Concedi i diritti di scrittura all'account di servizio |
| `not_configured` | Percorso della cartella non configurato | Inserisci il percorso nella configurazione |

**Cartelle interessate:**

* **Watch Folder (Import):** dove WatchDog cerca i nuovi file
* **Success Folder:** dove vengono spostati i file importati con successo
* **Export Folder:** dove vengono scritti i file XML/PDF esportati

---

## 3. Messaggi di Errore di Importazione

| Errore | Significato | Soluzione |
| :--- | :--- | :--- |
| `file_not_found` | Il file è stato eliminato prima dell'importazione | Fornisci di nuovo il file |
| `invalid_file_type` | Sono supportati solo file PDF | Rimuovi gli altri tipi di file |
| `api_not_accessible` | API di DocBits non raggiungibile | Controlla rete/firewall, verifica l'URL dell'API |
| `api_check_failed` | Controllo di integrità dell'API non riuscito | Controlla l'API Key e la connessione |
| `upload_failed` | Caricamento verso l'API non riuscito | Controlla API Key, rete, stato del server |

---

## 4. Messaggi di Errore di Esportazione

| Errore | Significato | Soluzione |
| :--- | :--- | :--- |
| `transformation_error` | Trasformazione XSLT non riuscita | Controlla il template XSLT, valida la struttura XML |
| `folder_error` | Cartella di esportazione non raggiungibile | Crea la cartella, controlla i permessi |
| `file_write_error` | Impossibile scrivere il file | Controlla lo spazio su disco, i permessi, i blocchi dei file |
| `permission_denied` | Nessun permesso di scrittura | Imposta i permessi dell'account di servizio |
| `creation_failed` | Impossibile creare la cartella | Controlla i permessi della cartella superiore |
| `no_config_match` | Nessuna configurazione di esportazione corrispondente | Crea una configurazione di esportazione con il tipo di documento corretto |

> **Nota:** Le configurazioni di esportazione richiedono un `doc_type`. Se vedi `no_config_match`, verifica che esista una configurazione di esportazione attiva per il tipo del documento.

---

## 5. Configurazione Disabilitata — Motivi

Quando una configurazione viene disabilitata, compare uno di questi motivi:

| Motivo della disabilitazione | Significato |
| :--- | :--- |
| `Watch folder: not_found` | La cartella di importazione non esiste |
| `Watch folder: no_read_access` | La cartella di importazione non è leggibile |
| `Export folder: not_found` | La cartella di esportazione non esiste |
| `Export folder: no_write_access` | La cartella di esportazione non è scrivibile |
| `Success folder: not_found` | La cartella dei successi non esiste |
| `Success folder: no_write_access` | La cartella dei successi non è scrivibile |

**Riattivazione automatica:** WatchDog controlla regolarmente le cartelle (ogni 60 secondi). Non appena la cartella torna raggiungibile, la configurazione viene riattivata automaticamente.

---

## 6. Cartella degli Errori (`_error`)

I file non riusciti vengono spostati nella cartella `_error`:

**Posizione:** `{import_folder}/_error/{error_type}/`

**Formato del file:** `{original_name}_{YYYYMMDD_HHMMSS}.pdf`

**File sidecar:** Ogni file non riuscito ha un file associato `.error` con:

```
Error Type: transformation_error
Error Message: XSLT template not found
Timestamp: 2026-03-26 08:30:15
Original File: invoice_001.pdf
Original Path: C:\WatchDog\Import\invoice_001.pdf
```

---

## 7. Heartbeat e Stato della Connessione

WatchDog invia un heartbeat a DocBits ogni ~10 secondi con le informazioni di sistema:

| Dati inviati | Descrizione |
| :--- | :--- |
| Timestamp | Ora corrente |
| Version | Versione di WatchDog installata |
| Last Restart | Ora dell'ultimo riavvio del servizio |
| Auto-Update Enabled | Indica se l'aggiornamento automatico è attivo |
| Latest Version | Ultima versione disponibile |
| Installation Path | Dove è installato WatchDog |
| Free RAM / Disk | Risorse di sistema disponibili |

### Stato della Connessione

| Stato | Significato |
| :--- | :--- |
| ✅ **Online** | WatchDog è connesso e attivo |
| ⚠️ **Offline** | Nessun heartbeat da oltre 30 secondi |
| ❌ **Not Installed** | WatchDog non si è mai connesso |

**Errori di heartbeat:**

* `Heartbeat failed - invalid API key` → L'API Key non è valida
* `Heartbeat failed: 401` → Autenticazione non riuscita
* `Heartbeat failed: 5xx` → Problema del server

---

## 8. Problemi Comuni e Soluzioni

### Problema: WatchDog non importa i file

1. Controlla se il servizio è in esecuzione: `services.msc` → WatchDog
2. Controlla i log: Settings → WatchDog → Logs Tab
3. Controlla i permessi delle cartelle per l'account di servizio di WatchDog
4. Testa la connessione API: `WatchDog.exe debug` nel CMD
5. Verifica che il tipo di file sia PDF

### Problema: L'esportazione non funziona

1. Esiste una configurazione di esportazione con il tipo di documento corretto?
2. Il tipo di documento corrisponde tra il documento e la configurazione?
3. Il template XSLT è collegato (per l'esportazione in cartella)?
4. La cartella di esportazione è scrivibile dall'account di servizio?
5. Per le esportazioni Infor: le credenziali ION sono configurate correttamente?

### Problema: La configurazione è disabilitata

1. Il percorso della cartella esiste?
2. Permessi per `NT AUTHORITY\LOCAL SERVICE` o per l'account di servizio?
3. L'unità di rete è raggiungibile? (Controlla i percorsi UNC)
4. WatchDog si riattiverà automaticamente quando le cartelle tornano disponibili

### Problema: La trasformazione XSLT non riesce

1. Il template XSLT è valido? (usa XSLT Templates Tab → Validate)
2. Il template è adatto al tipo di documento?
3. Controlla la struttura XML del documento
4. L'esportazione in cartella V3 usa la trasformazione lato server — controlla la connettività API

### Problema: L'esportazione REST API non riesce

1. Le credenziali ION OAuth sono configurate nella configurazione di esportazione?
2. L'endpoint API di destinazione è raggiungibile dal server di WatchDog?
3. Controlla che il formato del payload corrisponda alle aspettative dell'API di destinazione
4. Controlla la configurazione della catena di richieste per errori JSONPath

---

## 9. Comandi da Riga di Comando

```bash
# Configure API connection
WatchDog.exe -api YOUR_API_KEY

# Install Service
WatchDog.exe install

# Start Service
WatchDog.exe start

# Stop Service
WatchDog.exe stop

# Run in debug mode (console output)
WatchDog.exe debug

# Uninstall Service
WatchDog.exe remove

# Show version
WatchDog.exe --version

# List watch folders
WatchDog.exe --list-folders

# Add/remove watch folder
WatchDog.exe --add-folder "C:\Import\Invoices"
WatchDog.exe --remove-folder "C:\Import\Invoices"

# Check Windows service status
sc query WatchDog
```

---

## 10. File di Log

**Posizione:** `C:\WatchDog\logs\{module}\`

**Formato del log:**
```
INFO  - 2026-03-26 10:00:00 - module_name - Message - function=func_name - line=42
```

**Livello di log:** DEBUG, INFO, WARNING, ERROR

**Log remoti:** WatchDog invia i log anche a DocBits (visualizzabili nella scheda Logs) e, facoltativamente, al servizio di logging cloud Logtail.
