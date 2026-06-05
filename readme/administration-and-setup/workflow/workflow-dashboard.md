---
description: Monitor workflow performance, manage workflows, and access the Card SDK
---

# Dashboard Workflow

La Dashboard Workflow è il tuo centro di controllo per gestire e monitorare tutti i workflow in DocBits. Accedi cliccando sull'icona **Workflows** nella barra laterale sinistra.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Dashboard Workflow con totali delle esecuzioni, tassi di successo e fallimento, il grafico delle esecuzioni e l'attività recente"><figcaption><p>La Dashboard Workflow — totali delle esecuzioni, tassi di successo/fallimento e attività recente per ogni workflow.</p></figcaption></figure>

## Scheda Dashboard

La scheda Dashboard fornisce una panoramica immediata delle prestazioni dei workflow per un periodo di tempo selezionato.

### Filtri

- **Data inizio / Data fine** — Seleziona l'intervallo di tempo per le statistiche
- **Nome Workflow** — Filtra per un workflow specifico o visualizza tutti
- **Confronta** — Confronta due periodi di tempo affiancati
- **Cancella** — Reimposta tutti i filtri

### Schede Statistiche

| Metrica | Descrizione |
|---|---|
| **Workflow eseguiti oggi** | Numero totale di esecuzioni workflow oggi |
| **Workflow creati (periodo)** | Nuovi workflow creati nell'intervallo di date selezionato |
| **Esecuzioni totali** | Esecuzioni cumulative dei workflow nel periodo |
| **Esecuzioni riuscite** | Numero di esecuzioni completate senza errori |
| **Tasso di successo** | Percentuale di esecuzioni riuscite rispetto al totale |
| **Tasso di fallimento** | Percentuale di esecuzioni fallite rispetto al totale |

{% hint style="warning" %}
Un tasso di fallimento elevato (mostrato come **CRITICAL** in rosso) indica che i workflow stanno riscontrando errori. Indaga sui workflow in errore utilizzando i log di esecuzione nel [Costruttore Workflow Avanzato](advanced-workflow-builder/).
{% endhint %}

### Grafico Esecuzioni Workflow

Il grafico mostra una suddivisione mensile delle esecuzioni workflow **riuscite** (verde) e **fallite** (rosso/rosa), aiutandoti a identificare tendenze e picchi di errori.

### Attività Recente

- **Ultimi Test Workflow** — Mostra le esecuzioni di test recenti con stato superato/fallito
- **Ultimi Workflow** — Mostra i workflow creati o modificati di recente

## Scheda Elenco Workflow

La scheda Elenco Workflow mostra tutti i workflow con funzionalità di ricerca, ordinamento e gestione.

<!-- screenshot: Workflow List showing Advanced workflows with columns -->

### Colonne

| Colonna | Descrizione |
|---|---|
| **Stato** | Icona di attivazione — clicca per abilitare/disabilitare un workflow |
| **Nome** | Nome del workflow (clicca per aprire nel Costruttore Workflow) |
| **Tipo** | Badge che mostra `Advanced` per i workflow visuali |
| **Quando...** | Riepilogo della condizione di attivazione |
| **Aggiornato da** | Utente che ha modificato per ultimo il workflow |
| **Creato il** | Data e ora di creazione |
| **Aggiornato** | Data e ora dell'ultima modifica |
| **Azioni** | Menu contestuale (elimina, duplica, esporta) |

### Azioni

- **Cerca** — Filtra i workflow per nome utilizzando la barra di ricerca
- **+ AGGIUNGI WORKFLOW** — Crea un nuovo workflow (apre il [Costruttore Workflow Avanzato](advanced-workflow-builder/))
- **MODELLI** — Sfoglia e carica modelli di workflow salvati
- **IMPORTA WORKFLOW** — Importa un workflow da un file JSON

## Scheda Elenco Test Manager

L'Elenco Test Manager mostra tutte le configurazioni e i risultati dei test dei workflow. Usalo per impostare scenari di test automatizzati per i tuoi workflow.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Elenco Test Manager Workflow con scenari di test e Run All Tests"><figcaption><p>L'Elenco Test Manager — ogni scenario mostra un risultato superato/fallito; usa <strong>Run All Tests</strong> per rieseguirli tutti.</p></figcaption></figure>

## Scheda Licenza

La scheda Licenza mostra lo stato attuale della licenza DocFlow e le funzionalità disponibili.

## Scheda Card SDK

La scheda Card SDK ti permette di creare e gestire card workflow personalizzate (card partner) che estendono le funzionalità integrate di DocFlow.

<!-- screenshot: Card SDK page with Upload ZIP and Submissions tabs -->

### Carica ZIP

Carica un'app partner come file ZIP contenente:
- `app.json` — Metadati e configurazione della card
- `.docflowcompose/flow/` — File di definizione della card

Dimensione massima del file: **10 MB**. Clicca **Upload & Validate** per inviare la card per la revisione.

### Importazione da GitHub

Importa card partner direttamente da un repository GitHub invece di caricare un file ZIP.

### Invii

Visualizza e gestisci tutte le card partner inviate:

<!-- screenshot: Card SDK Submissions list with status badges -->

| Colonna | Descrizione |
|---|---|
| **Card Name** | Nome dell'app partner e della card |
| **card_type_label** | Tipo di card (`Action_card` o `Condition_card`) |
| **Version** | Numero di versione della card |
| **Submitted** | Data di invio |
| **Stato** | Stato attuale della revisione |
| **Azioni** | Azioni disponibili in base allo stato |

#### Stati delle Card

| Stato | Significato | Azioni disponibili |
|---|---|---|
| **Validated** | La card ha superato la validazione | Download, Approva, Rifiuta |
| **Approved** | La card è attiva e disponibile nei workflow | Download, Disabilita, Revoca |
| **Rejected** | La card non ha superato la revisione | Elimina |
| **Disabled** | La card è stata disattivata | Elimina |

### Scarica Modello SDK

Clicca **Download SDK Template** per ottenere un modello iniziale per creare le tue card personalizzate. Il modello include la struttura dei file richiesta e configurazioni di esempio.

{% hint style="info" %}
Le card partner possono anche essere gestite in modo programmatico tramite gli [strumenti DocFlow MCP](../../../advanced-functions-and-tools/docflow-mcp/). Usa gli strumenti MCP Card SDK per creare, validare, approvare e testare le card dal tuo IDE o da script di automazione.
{% endhint %}
