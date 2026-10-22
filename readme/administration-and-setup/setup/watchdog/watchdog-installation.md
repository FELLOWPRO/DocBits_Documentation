# Installazione di WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-installation-it.svg" alt="Installazione di WatchDog e requisiti principali."><figcaption><p>Installazione di WatchDog e requisiti principali.</p></figcaption></figure>

> **Consigliato:** Utilizza la configurazione moderna descritta di seguito. Le configurazioni di WatchDog vengono ora create direttamente nell'applicazione DocBits — non sono necessari file di configurazione locali.

## Prerequisiti

* Windows Server o Windows 10/11
* Accesso come amministratore
* Connettività di rete verso l'API di DocBits
* DocBits API Key (disponibile in Settings → WatchDog → General Tab)

## Passaggi di Installazione

### 1. Crea le Cartelle Necessarie

Crea una directory principale e le sottocartelle per WatchDog:

```
C:\WatchDog\              ← WatchDog executable
C:\WatchDog\Import\       ← Watch folder for incoming documents
C:\WatchDog\Processed\    ← Success folder for processed documents
C:\WatchDog\Export\        ← Export folder for exported files
```

> **Nota:** Si consiglia di usare percorsi locali. I percorsi di rete UNC (ad es. `\\server\share`) sono supportati, ma per un rilevamento affidabile dei file potrebbe essere necessario un Polling Observer.

### 2. Scarica WatchDog

Scarica `WatchDog.exe` dall'applicazione DocBits:

**Impostazioni → Elaborazione documenti → WatchDog → Scheda Generale → Download**

Inserisci il file `WatchDog.exe` scaricato in `C:\WatchDog\`.

### 3. Configura la Connessione API

Apri il **Prompt dei comandi (CMD)** come **amministratore** ed esegui:

```powershell
cd C:\WatchDog
WatchDog.exe -api YOUR_API_KEY
```

Questo collega WatchDog alla tua organizzazione DocBits e recupera automaticamente le configurazioni.

### 4. Installa come Servizio Windows

```powershell
WatchDog.exe install
```

### 5. Avvia il Servizio

```powershell
WatchDog.exe start
```

### 6. Crea le Configurazioni in DocBits

Vai a **Impostazioni → Elaborazione documenti → WatchDog → Scheda Configurazioni** in DocBits:

* Clicca su **New Import Configuration** per impostare le cartelle da monitorare
* Clicca su **New Export Configuration** per impostare le destinazioni di esportazione

> **Importante:** Le configurazioni di esportazione richiedono un **tipo di documento**. Tutte le configurazioni sono gestite centralmente in DocBits, non in file di configurazione locali.

### 7. Imposta l'Avvio Automatico

1. Apri **Servizi** (`Win + R` → `services.msc`)
2. Trova **WatchDog** nell'elenco dei servizi
3. Fai doppio clic per aprirne le proprietà
4. Imposta **Tipo di avvio** su **Automatico (avvio ritardato)**
5. Clicca su **OK**

## Verifica dell'Installazione

Dopo l'installazione, controlla lo stato di WatchDog in DocBits:

**Impostazioni → WatchDog → Scheda Generale**

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Scheda General di WatchDog — Stato del servizio"><figcaption></figcaption></figure>

* ✅ **Online** — WatchDog è connesso e invia gli heartbeat
* Versione, ultimo riavvio e informazioni di sistema dovrebbero essere visibili

## Riferimento dei Comandi

| Comando | Descrizione |
| :--- | :--- |
| `WatchDog.exe -api KEY` | Configura l'API Key |
| `WatchDog.exe install` | Installa come servizio Windows |
| `WatchDog.exe start` | Avvia il servizio |
| `WatchDog.exe stop` | Arresta il servizio |
| `WatchDog.exe debug` | Esegue in modalità console (per la risoluzione dei problemi) |
| `WatchDog.exe remove` | Disinstalla il servizio |
| `WatchDog.exe --version` | Mostra la versione corrente |
| `WatchDog.exe --list-folders` | Elenca le cartelle monitorate configurate |
| `WatchDog.exe --add-folder PATH` | Aggiunge una cartella monitorata |
| `WatchDog.exe --remove-folder PATH` | Rimuove una cartella monitorata |

---

## Legacy: Configurazione V1 (Obsoleta)

Il seguente metodo di configurazione V1 con file di configurazione locali è **obsoleto**. Utilizza invece la configurazione moderna basata su API descritta sopra.

<details>
<summary>Configurazione V1 (clicca per espandere)</summary>

### Configurazione di WatchDog in DocBits (V1)

1. **Accedi alle impostazioni di WatchDog**
   * Vai a **Impostazioni → Elaborazione documenti → WatchDog**
2. **Impostazioni delle cartelle**
   * Definisci i percorsi: `C:/WatchDog/Read` e `C:/WatchDog/Processed`

   <figure><img src="../../../.gitbook/assets/watchdog_folder_settings.png" alt="Impostazioni delle cartelle di WatchDog"><figcaption></figcaption></figure>

3. **Impostazioni generali**
   * Seleziona i tipi di documento, configura la destinazione di esportazione

   <figure><img src="../../../.gitbook/assets/watchdog_general_settings_doctypes.png" alt="Impostazioni generali di WatchDog"><figcaption></figcaption></figure>

4. **Configurazioni di esportazione**
   * Mostra le esportazioni configurate per l'elaborazione on-premise

   <figure><img src="../../../.gitbook/assets/watchdog_export_configurations_list.png" alt="Configurazioni di esportazione di WatchDog"><figcaption></figcaption></figure>

5. **Scarica la configurazione**
   * Scarica `watchdog-config.json` e inseriscilo in `C:\WatchDog\`

   <figure><img src="../../../.gitbook/assets/watchdog_download_configuration.png" alt="Scarica la configurazione"><figcaption></figcaption></figure>

</details>
