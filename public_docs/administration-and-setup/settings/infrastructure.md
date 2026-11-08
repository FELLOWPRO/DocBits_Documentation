# Infrastruttura

La pagina **Infrastructure** offre agli amministratori una panoramica aggiornata di dove viene eseguita ogni parte della piattaforma (EU o US) e se l'elaborazione è in salute. È di sola lettura, quindi qui non si configura nulla.

> **Access:** Infrastructure è una pagina riservata agli amministratori. Aprire **Settings → Organization & Access → Infrastructure**.

La pagina ha tre schede. Ognuna carica i propri dati alla prima apertura, quindi passare da una all'altra non richiede di recuperare tutto di nuovo.

| Tab | Answers |
|-----|---------|
| **Topology** | Dove viene eseguito ogni componente e come viaggia un documento attraverso DocBits? |
| **Processing** | Le fasi di elaborazione dei documenti sono in esecuzione e il lavoro si sta accumulando? |
| **Scheduled Tasks** | Le attività in background ricorrenti vengono avviate secondo la pianificazione? |

## Topology

**Topology** si apre per impostazione predefinita. Mostra la piattaforma in due viste: **Architecture** e **Process**. Con l'interruttore sopra il diagramma si passa dall'una all'altra; l'indicatore accanto mostra **live** finché la vista trasmette il proprio stato.

Un banner sopra il diagramma riassume il controllo delle regioni:

* **Green**: tutti i componenti vengono eseguiti nella regione della propria organizzazione e il banner ne indica il nome (per esempio **EU**).
* **Red**: un componente contrassegnato come critico viene eseguito fuori dalla regione della propria organizzazione.
* **Amber**: l'avviso indica componenti che si trovano in un'altra regione anche se il controllo complessivo è superato. Si tratta di una differenza di regione, non di un guasto.

### Vista dell'architettura

La vista dell'architettura rappresenta la piattaforma come corsie di schede dei componenti, per esempio Edge / Web, Core API, Import, Background Services e Modules. Le frecce mostrano le connessioni tra le schede.

Ogni scheda mostra il nome del componente, un badge di regione e, per i componenti critici, un punto di stato che diventa verde quando il componente risponde e mostra la latenza in millisecondi quando viene segnalato un valore.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | Il componente viene eseguito nella regione della propria organizzazione. |
| **SHARED** | Un componente globale come la CDN, senza una singola regione. È previsto. |
| **EU ⓘ** / **US ⓘ** | Il componente viene eseguito in un'altra regione ed è segnalato come avviso. |
| **EU ⚠** / **US ⚠** | Il componente viene eseguito in un'altra regione ed è segnalato come errore. Segnalarlo al supporto. |
| Badge grigio, senza contrassegno | La regione di questo componente non è nota. |

### Vista del processo

La vista del processo anima un singolo documento attraverso la pipeline: le sorgenti di ingresso **Email**, **FTP** e **Web** convergono su **API**, poi attraversano **OCR**, **Extraction**, **PO matching**, **Auto Accounting** e **Export**. Ogni fase è collegata a una barra degli archivi dati con **Postgres** e l'archiviazione file. Una didascalia indica la fase in animazione e il pulsante di riproduzione mette in pausa o riprende l'animazione.

PO matching e Auto Accounting sono opzionali. Quando uno dei due è disattivato per la propria organizzazione, la relativa fase è in grigio e l'animazione la salta.

### Moduli opzionali

I moduli opzionali (Full-Text Search, DocFlow, Auto-Accounting, DocNet e PO Matching) riportano sulla scheda un badge **active** o **inactive**. Un modulo disattivato offre un pulsante **Activate** che porta alla pagina in cui attivarlo: le impostazioni Modules per la maggior parte dei moduli, oppure **Document Types** per PO Matching, che viene attivato per tipo di documento.

## Processing

La scheda **Processing** elenca le fasi di elaborazione dei documenti della propria organizzazione e indica se il lavoro scorre o si accumula.

| Column | Description |
|--------|-------------|
| **Process** | La fase di elaborazione: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction e PO Match. |
| **Last run** | Quanto tempo è passato dall'ultima esecuzione della fase. Passare il mouse sopra per il timestamp esatto. **Never run** significa che nessun documento ha ancora raggiunto questa fase. |
| **Status** | Uno o più badge (vedere sotto). |

I badge di stato sono segnali indipendenti:

* Badge rosso **Errors (N)**: `N` documenti non sono riusciti di recente in questa fase.
* Badge ambra con un conteggio: `N` documenti sono in elaborazione in questa fase in questo momento.
* Badge verde **OK**: nessun errore recente e nulla in attesa.

Poiché errori e lavoro in corso vengono contati separatamente, una fase può mostrare entrambi contemporaneamente: un guasto resta quindi visibile mentre altri documenti sono ancora in esecuzione.

## Scheduled Tasks

La scheda **Scheduled Tasks** elenca le attività in background ricorrenti che mantengono DocBits in funzione, per esempio aggiornamenti della cache, avvisi di stato, timeout dei documenti e sincronizzazioni in uscita. Ogni riga indica se l'attività viene avviata puntualmente.

| Column | Description |
|--------|-------------|
| **Task** | Il nome dell'attività pianificata, con i separatori sostituiti da spazi. |
| **Last run** | Quanto tempo è passato dall'ultima esecuzione. Passare il mouse sopra per il timestamp esatto. **Never run** significa che non è ancora stata avviata. |
| **Status** | Salute della pianificazione (vedere sotto). |

| Status | Meaning |
|--------|---------|
| **On schedule** (verde) | L'attività viene eseguita all'intervallo previsto. |
| **Delayed** (rosso) | L'attività non è stata eseguita al momento previsto. Analizzarla o segnalarla al supporto. |
| **Unknown** (grigio) | Non è stato possibile determinare lo stato della pianificazione. |

Entrambe le tabelle hanno un pulsante **Refresh** che ricarica i valori attuali su richiesta.
