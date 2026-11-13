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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4" %}

**Video:** Successo, condizione non riuscita ed errore in un'esecuzione · 1:29 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**Quando, E, Poi in esecuzione** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=0.25)

Quando un Workflow viene eseguito, la scheda Quando lo avvia. Le schede E controllano condizioni e le schede Poi agiscono. Cosa succede dopo dipende dal risultato di ogni scheda.

**Successo, condizione non riuscita o errore** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=14.616)

Ogni scheda E finisce con uno di tre risultati. Il successo segue il percorso blu, una condizione non riuscita il percorso arancione e un errore il percorso rosso.

**I dati mancanti sono un errore** · [0:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=26.283)

I dati mancanti non sono una condizione non riuscita. Se manca un campo che serve alla scheda, una variabile o il documento, la scheda segnala un errore e prende il percorso rosso.

**Nessun percorso arancione: stop** · [0:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=40.183)

Se una condizione non riesce e il suo percorso arancione non è collegato, il Workflow si ferma su quella scheda. L'esecuzione finisce come condizione non riuscita.

**Collegato: solo un altro ramo** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=51.183)

Se il percorso arancione è collegato, una condizione non riuscita è solo un altro ramo. Il Workflow continua lì e può comunque finire con successo.

**Percorso rosso: intercettare gli errori** · [1:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=61.716)

Collega il percorso rosso a un'alternativa, per esempio un'attività per una persona, così gli errori non passano inosservati. L'alternativa viene eseguita, ma l'esecuzione resta segnata come errore.

**Come finisce un'esecuzione** · [1:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/it.mp4#t=76.316)

In breve: qualsiasi errore rende l'esecuzione un errore. Una condizione non riuscita senza percorso arancione collegato la rende una condizione non riuscita. Tutto il resto finisce con successo.

</details>

I nodi sono collegati da **archi colorati**. Trascina da una maniglia sul lato **destro** di un nodo verso la maniglia di input sul lato **sinistro** di un altro nodo per creare un collegamento. Ogni colore indica un diverso esito di esecuzione:

- **Success** (blu) — il percorso predefinito seguito quando un nodo si completa con successo. Disponibile su tutti i tipi di nodo.
- **Failed Condition** (arancione) — seguito quando una condizione restituisce falso. Disponibile sui nodi **And** (condizione).
- **Error** (rosso) — seguito quando un nodo incontra un errore durante l'esecuzione. Disponibile sui nodi **And** e **Then** (azione).

## Evidenziazione del percorso di esecuzione

Fai clic su un nodo qualsiasi per vedere il suo percorso di esecuzione. Tutti i nodi che conducono a esso e tutti i nodi che lo seguono vengono evidenziati — tutto il resto viene attenuato. Per i nodi **Wait ALL**, viene mostrata ogni diramazione in entrata, così puoi vedere esattamente cosa attende il gate prima di continuare.

## Passi successivi

- Passa i dati tra i nodi con le [Variabili](variables.md).
- Controlla ed esegui il tuo flusso con [Validazione e test](validation-and-testing.md).
