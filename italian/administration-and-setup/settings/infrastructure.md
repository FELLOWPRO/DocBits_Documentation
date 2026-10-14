# Infrastruttura

La pagina **Infrastruttura** offre agli amministratori una visione in tempo reale di dove viene eseguita ogni parte di DocBits (UE o USA), di come un documento attraversa il sistema e dello stato di salute dell'elaborazione in background. È di sola lettura — qui non si configura nulla; risponde alla domanda: *«è tutto operativo e i miei dati restano nella mia regione?»*

> **Accesso:** Infrastruttura è una pagina riservata agli amministratori. Apri **Impostazioni → Organizzazione e Accesso → Infrastruttura**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Pagina Infrastruttura con la scheda Topologia aperta"><figcaption><p>La pagina Infrastruttura, scheda Topologia</p></figcaption></figure>

La pagina è suddivisa in tre schede:

| Scheda | Risponde a |
|--------|------------|
| **Topologia** | Dove viene eseguito ciascun componente ed è tutto nella mia regione? |
| **Elaborazione** | Le fasi di elaborazione (OCR, estrazione, abbinamento PO …) sono in esecuzione e aggiornate? |
| **Attività pianificate** | Le attività ricorrenti in background vengono eseguite come previsto? |

## Topologia

La scheda Topologia disegna l'intera piattaforma DocBits come un diagramma, raggruppato in livelli — **Edge / Web**, **Core API**, **Importazione**, **Servizi in background**, **Datastore** e **Autenticazione**. Ogni riquadro è un componente (la Web App/CDN, il gateway API, il worker OCR, il database e così via).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Diagramma della topologia con i badge di regione"><figcaption><p>Ogni componente è etichettato con la regione in cui viene eseguito</p></figcaption></figure>

### Trasparenza della regione

Ogni componente riporta un badge di regione, così puoi confermare a colpo d'occhio la residenza dei tuoi dati:

| Badge | Significato |
|-------|-------------|
| **UE ✓** / **US ✓** | Il componente viene eseguito nella regione della tua organizzazione. |
| **SHARED** | Un componente globale (ad es. la CDN) senza una regione specifica — è previsto e non costituisce un problema. |
| **Discrepanza di regione** | Il componente viene eseguito in una regione *diversa* da quella della tua organizzazione. Viene evidenziato così puoi segnalarlo al supporto. |

Il banner in alto riassume il risultato: **«Tutti i componenti vengono eseguiti nella tua regione (UE)»** quando tutto corrisponde, oppure un avviso se un componente critico è in un'altra regione.

### Architettura vs. Riproduci processo

Usa l'interruttore sopra il diagramma per cambiare vista:

- **Architettura** — la mappa statica di tutti i componenti e di come sono collegati.
- **Riproduci processo** — anima il percorso di un documento attraverso il sistema, passo dopo passo, così vedi l'ordine in cui i componenti intervengono.

L'indicatore **● live** mostra che le informazioni sullo stato nel diagramma riflettono lo stato attuale del sistema.

### Moduli opzionali

I componenti che appartengono a un modulo opzionale (Ricerca full-text, DocFlow, Auto-Accounting, DocNet, Abbinamento PO) mostrano un badge **attivato** o **disattivato**. Facendo clic su un modulo disattivato si va direttamente alla pagina in cui attivarlo — **Impostazioni → Modulo** per la maggior parte dei moduli, oppure **Tipi di documento** per l'Abbinamento PO (che si attiva per tipo di documento).

## Elaborazione

La scheda Elaborazione mostra la pipeline di elaborazione dei documenti della **tua organizzazione** — quando ciascuna fase è stata eseguita l'ultima volta e se il lavoro scorre o si accumula.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tabella di elaborazione con i badge di stato"><figcaption><p>Stato dell'elaborazione per fase per la tua organizzazione</p></figcaption></figure>

| Colonna | Descrizione |
|---------|-------------|
| **Processo** | La fase di elaborazione — Elaborazione documenti, OCR, TR-OCR, Suddivisione tramite codice a barre, Estrazione codice a barre, Estrazione, Abbinamento PO. |
| **Ultima esecuzione** | Quanto tempo fa è stata eseguita la fase. Passa il mouse per il timestamp esatto. *«Mai eseguito»* significa che nessun documento ha ancora raggiunto questa fase. |
| **Stato** | Un badge tipo semaforo (vedi sotto). |

Badge di stato:

| Badge | Significato |
|-------|-------------|
| **OK** (verde) | Nessun errore recente e niente in attesa — la fase è sana. |
| **In corso (N)** (ambra) | `N` documenti sono attualmente in elaborazione in questa fase. |
| **Errore (N)** (rosso) | `N` documenti sono falliti di recente in questa fase. |

Gli errori e *in corso* sono segnali indipendenti, quindi una fase può mostrare entrambi i badge contemporaneamente — così vedi un errore anche mentre altro lavoro è in corso. Usa **Aggiorna** (in alto a destra) per recuperare i valori più recenti.

## Attività pianificate

La scheda Attività pianificate elenca le attività ricorrenti in background che mantengono DocBits operativo (aggiornamenti della cache, avvisi di stato, timeout dei documenti, sincronizzazioni in uscita e altro) e conferma che ciascuna venga avviata in orario.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabella delle attività pianificate"><figcaption><p>Attività ricorrenti in background e il loro stato di pianificazione</p></figcaption></figure>

| Colonna | Descrizione |
|---------|-------------|
| **Attività** | Il nome dell'attività pianificata. |
| **Ultima esecuzione** | Quanto tempo fa è stata eseguita. Passa il mouse per il timestamp esatto; *«Mai eseguito»* significa che non è ancora stata avviata. |
| **Stato** | Stato di pianificazione (vedi sotto). |

Valori di stato:

| Badge | Significato |
|-------|-------------|
| **In orario** (verde) | L'attività viene eseguita nell'intervallo previsto. |
| **In ritardo** (rosso) | L'attività non è stata eseguita quando previsto — da verificare o segnalare al supporto. |
| **Sconosciuto** (grigio) | Non è stato possibile determinare lo stato di pianificazione. |

Usa **Aggiorna** per ricontrollare lo stato di pianificazione su richiesta.
