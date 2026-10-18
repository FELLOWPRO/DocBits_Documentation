# Nodi

## Video: Nodi e percorsi

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.mp4" %}

[Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/it.vtt) · 1:53

<details>
<summary>Trascrizione</summary>

**Il ruolo di ogni nodo**

Start avvia manualmente. When definisce un evento. Nessuno dei due accetta connessioni in ingresso. And verifica una condizione. Then esegue un’azione. Entrambi i costruttori condividono il catalogo delle schede. Le note spiegano senza essere eseguite.

**Tre risultati distinti**

Trascina un’uscita sull’ingresso successivo. Nel designer, blu significa successo, arancione condizione falsa, rosso errore. And ha tre risultati; Then, successo ed errore. Le viste di esecuzione mostrano il successo in verde.

**Crea un’alternativa**

Verifica se una fattura supera la soglia. Collega blu all’approvazione, arancione all’elaborazione normale e rosso alla gestione errori. Una condizione falsa può continuare sul percorso collegato; non arresta tutti i rami.

**Unisci con Wait ALL**

Wait ALL unisce i rami. Ogni nodo sorgente deve aver seguito un percorso collegato alla giunzione. Collega entrambi i controlli richiesti e l’azione successiva. Un percorso non selezionato non fornisce il risultato necessario.

**Alternative con ANY e OR**

Wait ANY e OR uniscono i rami quando almeno una sorgente segue un percorso collegato. OR richiede due nodi sorgente distinti. Queste giunzioni non creano scelte esclusive né annullano altre azioni. Prova l’intero grafo.

**Mantieni il grafo eseguibile**

I nodi devono essere raggiungibili da un ingresso. Evita cicli e connessioni in ingresso a Start o When. Includi un’azione Then e convalida i percorsi. I nodi Delay importati richiedono una durata positiva; Aggiungi non offre Delay.

</details>

[Guarda i cinque capitoli](../advanced-workflow-videos.md)

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
