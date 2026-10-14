# Nodi

Un Advanced Workflow è un grafo di **nodi** collegati da archi. Aggiungi i nodi dal menu **+ Add** (o facendo clic con il tasto destro sul canvas) e li colleghi per definire il flusso di esecuzione.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu di aggiunta nodi con i tipi di nodo disponibili"><figcaption><p>Il menu nodi <strong>+ Add</strong> — i tipi di nodo disponibili.</p></figcaption></figure>

## Tipi di nodo

- **Start** — il punto di ingresso del workflow. Aggiunto automaticamente; ogni flusso inizia qui.
- **When** — una scheda trigger, la stessa del builder Standard.
- **And** — una scheda condizione. Restituisce vero o falso e può ramificare il flusso.
- **Then** — una scheda azione che esegue un'operazione (impostare campi, creare attività, chiamare API, …).
- **Wait ALL** — attende che *tutte* le diramazioni in entrata siano completate prima di continuare.
- **Wait ANY** — continua non appena *una qualsiasi* diramazione in entrata è completata.
- **OR** — ramifica il flusso lungo percorsi alternativi.
- **Note** — un'annotazione di testo libero sul canvas; non influisce sull'esecuzione.

I nodi **When / And / Then** utilizzano esattamente le stesse schede descritte nella sezione [Schede](../cards-overview.md).

## Collegare i nodi

I nodi sono collegati da **archi colorati**. Trascina da una maniglia sul lato **destro** di un nodo verso la maniglia di input sul lato **sinistro** di un altro nodo per creare un collegamento. Ogni colore indica un diverso esito di esecuzione:

- **Success** (blu) — il percorso predefinito seguito quando un nodo si completa con successo. Disponibile su tutti i tipi di nodo.
- **Failed Condition** (arancione) — seguito quando una condizione restituisce falso. Disponibile sui nodi **And** (condizione).
- **Error** (rosso) — seguito quando un nodo incontra un errore durante l'esecuzione. Disponibile sui nodi **And** e **Then** (azione).

## Evidenziazione del percorso di esecuzione

Fai clic su un nodo qualsiasi per vedere il suo percorso di esecuzione. Tutti i nodi che conducono a esso e tutti i nodi che lo seguono vengono evidenziati — tutto il resto viene attenuato. Per i nodi **Wait ALL**, viene mostrata ogni diramazione in entrata, così puoi vedere esattamente cosa attende il gate prima di continuare.

## Passi successivi

- Passa i dati tra i nodi con le [Variabili](variables.md).
- Controlla ed esegui il tuo flusso con [Validazione e test](validation-and-testing.md).
