# Dashboard di analisi

## Panoramica

La **Dashboard di analisi** fornisce visibilità completa sulle prestazioni di elaborazione dei documenti. Tiene traccia del tempo che i documenti trascorrono in ogni fase del loro percorso — dall'importazione all'esportazione — e ti aiuta a identificare i colli di bottiglia, confrontare le prestazioni tra organizzazioni, tipi di documento e fornitori, e a confrontare i tuoi risultati con la **Media globale DocBits**.

Ogni documento attraversa fasi distinte:

**Nuovo** (importato) → **In corso** (in elaborazione) → **Pronto per la convalida** (in attesa di revisione utente) → **In attesa di approvazione** (in attesa di approvazione) → **Esportazione** (completato ed esportato)

Il tempo trascorre in ogni fase — la Dashboard di analisi ti indica esattamente **quanto** e **dove** concentrare i tuoi miglioramenti.

### Due tipi di colli di bottiglia

La dashboard ti aiuta a distinguere tra:

* **Colli di bottiglia di sistema** — Quanto tempo DocBits è impegnato con l'elaborazione automatica (OCR ed estrazione del testo, classificazione dei documenti, estrazione dei campi, convalida automatica). Ottimizzabili tramite la configurazione e le risorse di sistema.
* **Colli di bottiglia utente** — Tempo trascorso in attesa di convalida e approvazione manuale (tempo di attesa in coda, correzione manuale dei dati, revisione e convalida, flussi di approvazione). Ottimizzabili tramite il flusso di lavoro e l'allocazione delle risorse.

## Come attivarla

La Dashboard di analisi è controllata da un'impostazione di modulo. Una volta abilitata, una voce **Dashboard di analisi** appare nella barra laterale a sinistra.

1. Naviga in **Impostazioni → Elaborazione documenti → Modulo → Dashboard e analisi**.
2. Abilita l'opzione **Dashboard di analisi**.

<mark style="color:red;">**Nota**</mark>: La Dashboard di analisi richiede un **Abbonamento al pannello di controllo analitico**.

<mark style="color:red;">**Nota**</mark>: L'accesso alla Dashboard di analisi è limitato agli utenti con diritti di **amministratore**.

## Tipi di flusso

Scegli la prospettiva giusta per la tua analisi. Ogni tipo di flusso ti offre una visione diversa degli stessi dati.

| Tipo di flusso | Scopo | Domanda chiave |
| --- | --- | --- |
| **Stato** | Traccia il ciclo di vita del documento dall'importazione all'esportazione | *"Qual è il tempo complessivo dei miei documenti dall'importazione all'esportazione?"* |
| **Elaborazione** | Analisi delle prestazioni tecniche dei moduli | *"Quali fasi di elaborazione sono colli di bottiglia?"* |
| **Interazione dell'utente** | Punti di contatto umani e tempi di attesa | *"Quanto tempo i documenti attendono gli utenti?"* |

Usa l'interruttore **Tipo di flusso** in cima alla dashboard per passare da una prospettiva all'altra.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_flow_types.png)

### Flusso di stato

Tiene traccia del percorso del documento da **Nuovo** a **Esportato** — utile per l'analisi del ciclo di vita end-to-end.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_status_flow.png)

### Flusso di elaborazione

Analizza le prestazioni di tutti i **moduli tecnici di elaborazione** (OCR, classificazione, estrazione, convalida) — utile per identificare i colli di bottiglia lato sistema.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_processing_flow.png)

### Flusso di interazione dell'utente

Si concentra sui **punti di contatto umani** — tempo di attesa in coda, convalida manuale, revisione e approvazione — utile per identificare i colli di bottiglia di flusso di lavoro e di personale.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_user_interaction_flow.png)

## Opzioni di filtro

La dashboard supporta un potente filtraggio multidimensionale. Tutti i grafici, le schede e le tabelle vengono aggiornati in tempo reale in base ai filtri attivi.

### Ricerca

Individua immediatamente qualsiasi documento tramite **nome** o **ID univoco**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_search.png)

### Fasi del flusso

Seleziona fasi specifiche per concentrare la tua analisi. L'attivazione/disattivazione delle fasi ricalcola anche le metriche temporali sugli altri componenti della dashboard.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_flow_steps.png)

### Sotto-organizzazione, Tipo di documento, Fornitore, Gruppo

Confronta le prestazioni tra:

* **Sotto-organizzazioni** — diverse unità aziendali o tenant
* **Tipi di documento** — fatture, ordini di acquisto, bolle di consegna, ecc.
* **Fornitori** — per identificare quali fornitori causano i tempi di elaborazione più lunghi
* **Gruppi** — per confrontare le prestazioni tra gruppi di utenti assegnati (disponibile per i tipi di flusso **Stato** e **Interazione dell'utente**)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_dimensions.png)

<mark style="color:red;">**Nota**</mark>: Il filtro **Gruppo** si applica solo ai documenti che sono **assegnati direttamente a un gruppo**. I documenti assegnati a un singolo utente — anche se tale utente è membro di un gruppo — **non** sono inclusi nei risultati del filtro per gruppo.

### Intervallo di tempo

Analizza qualsiasi periodo, da **7 giorni** fino a un **anno intero**, oppure imposta un **intervallo personalizzato** utilizzando il selettore di date.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_filter_time_range.png)

## Schede delle fasi del flusso

Ogni scheda rappresenta una fase del flusso in base al **Tipo di flusso** selezionato. Le schede si adattano alla tua selezione — mostrando le fasi del ciclo di vita per *Stato*, i moduli di elaborazione per *Elaborazione*, o i punti di contatto utente per *Interazione dell'utente*.

Ogni scheda mostra:

* I tempi **Minimo, Media, Massimo** per la fase
* Un confronto tra il **tuo Tempo medio** e la **Media globale DocBits** (quando l'interruttore di confronto è attivo)
* Un cerchio di selezione per **includere o escludere** la fase dai calcoli temporali aggregati utilizzati dal Grafico del tempo medio, dal Grafico di tendenza temporale e dalla Tabella dati

Un interruttore **Seleziona tutto** nell'intestazione consente di includere o escludere tutte le fasi contemporaneamente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_flow_steps_card.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_step_toggle.png)

### Confronta con la Media globale

L'interruttore **Confronta con la Media globale** controlla se la Media globale DocBits viene mostrata sulle schede e nel grafico. Quando è abilitato, il tempo medio su ciascuna scheda è colorato in base al codice cromatico:

* **Verde** — il tuo Tempo medio è uguale o inferiore alla Media globale
* **Arancione** — il tuo Tempo medio è fino al **+25%** sopra la Media globale
* **Rosso** — il tuo Tempo medio è del **+25%** o più sopra la Media globale

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_global_average_comparison.png)

## Grafico del tempo medio

Il Grafico del tempo medio visualizza come il tempo di elaborazione è distribuito tra le fasi del flusso selezionate. Usa il selettore **Raggruppa per** per confrontare tra diverse dimensioni:

* **Fasi del flusso** — vedi quali fasi consumano più tempo
* **Sotto-organizzazione** — identifica le variazioni tra le unità aziendali
* **Tipo di documento** — confronta i tempi di elaborazione tra i tipi di documento
* **Fornitore** — scopri quali fornitori hanno i tempi di elaborazione più lunghi
* **Gruppo** — confronta tra gruppi di utenti assegnati (solo per i tipi di flusso Stato e Interazione dell'utente)

Quando **Confronta con la Media globale** è abilitato, il grafico mostra anche la Media globale DocBits come riferimento di benchmark.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_average_time_chart.png)

## Documenti principali

La scheda **Documenti principali** elenca i singoli documenti corrispondenti al set di filtri attivo, classificati in base al tempo totale trascorso.

* Interruttore **Ordinamento** — passa tra **decrescente** (i più lenti per primi) e **crescente** (i più veloci per primi).
* Menu a discesa **Dimensione pagina** e paginazione — sfoglia il set di risultati.
* **Nascondi/mostra** un documento tramite l'icona dell'occhio accanto ad esso — i documenti nascosti vengono esclusi da tutti i calcoli temporali nella dashboard.
* **Nascondi/mostra tutti** i documenti nel filtro tramite l'icona dell'occhio nell'intestazione.
* **Fai clic su un documento** (nome file o barra di avanzamento) per copiare il suo ID documento negli appunti.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_top_documents.png)

## Grafico di tendenza temporale

Tieni traccia delle tendenze delle prestazioni nel tempo e individua le anomalie. Il Grafico di tendenza temporale mostra il **Tempo medio** delle fasi del flusso attualmente selezionate e può essere raggruppato per:

* **Fasi del flusso** — una riga per ogni fase selezionata
* **Sotto-organizzazione**
* **Tipo di documento**
* **Fornitore**
* **Gruppo** (disponibile per i tipi di flusso **Stato** e **Interazione dell'utente**)

Ciò rende facile rilevare un picco improvviso per uno specifico fornitore, o un aumento graduale per un determinato tipo di documento, prima che diventi un problema critico.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_time_trend.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_time_trend_grouped.png)

## Tabella dati

La Tabella dati fornisce accesso completo a tutti i dati di riga sottostanti per il set di filtri attivo.

* **Trascina le colonne nel pannello Colonne nascoste** (a sinistra della tabella) per rimuoverle dalla vista. Le colonne nascoste vengono utilizzate per l'aggregazione — i tempi **Minimo / Massimo / Media** vengono ricalcolati dinamicamente in base alle colonne visibili. Trascina nuovamente un chip nella tabella (o fai clic sull'icona **+**) per ripristinare la colonna.
* **Ordina** facendo clic sulle intestazioni delle colonne e **riordina** le colonne tramite trascinamento della selezione.
* **Scarica CSV** tramite il pulsante nell'intestazione della scheda — vengono esportate solo le colonne attualmente visibili.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table_hide_columns.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/analytics_dashboard_data_table_export.png)
