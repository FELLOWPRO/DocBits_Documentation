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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4" %}

**Video:** Cambiare la versione di una scheda · 0:41 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.vtt)

<details>

<summary>Trascrizione</summary>

**L'etichetta mostra la versione della scheda** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4#t=0.25)

Le schede possono avere più versioni. La piccola etichetta su una scheda, per esempio v1, indica quale versione usa. Una versione più recente fa di più.

**Clic per vedere le versioni** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4#t=12.15)

Fai clic sull'etichetta della versione per vedere le versioni della scheda.

**Versione 3: Stato dopo l'esportazione** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4#t=17.316)

Scegli la versione più recente. Questa può impostare anche lo stato del documento dopo l'esportazione.

**Impostare di nuovo i valori** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4#t=25.45)

I valori non vengono riportati. Impostali di nuovo, qui la configurazione di esportazione e lo stato.

**Convalidare e testare** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/it.mp4#t=33.183)

Poi convalida e testa il Workflow, come dopo ogni modifica. Salvalo quando fa ciò che ti aspetti.

</details>

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4" %}

**Video:** E e O: combinare le condizioni · 4:27 · [Sottotitoli (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.vtt)

<details>

<summary>Trascrizione</summary>

**E e O** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=0.25)

Le condizioni si combinano in due modi. Schede una dopo l'altra funzionano come E: devono essere tutte vere. Schede affiancate, collegate alla stessa scheda successiva, funzionano come O: basta una scheda vera. I nodi di unione lo mostrano sull'area di lavoro.

**E: schede una dopo l'altra** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=19.083)

Una scheda dopo l'altra è E: ogni scheda del percorso deve essere vera prima che parta la successiva. Questa fattura è pronta per la validazione e non in attesa di approvazione, quindi entrambe le schede sono vere e l'azione parte.

**O: schede affiancate** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=35.416)

O significa schede affiancate. Collega l'uscita verde di entrambe le schede E direttamente all'ingresso della scheda successiva. Prova: la prima scheda è falsa, la seconda vera, e basta un percorso vero perché l'azione parta. Il banner del test segnala comunque una condizione non soddisfatta, perché l'uscita arancione della scheda falsa non è collegata, ma l'azione parte.

**Lo stesso con una scheda O** · [0:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=59.85)

Puoi anche unire i percorsi con una scheda O. Fa la stessa cosa, ma rende visibile l'O sull'area di lavoro. Clic destro sull'area di lavoro, Aggiungi, poi O. Collega entrambe le schede E alla scheda O, e la scheda O all'azione.

**A O basta un caso vero** · [1:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=78.75)

Il test dà lo stesso risultato: alla scheda O basta un caso vero, quindi l'azione parte. Anche qui il banner segnala la condizione non soddisfatta della scheda falsa.

**Attendi UNO: uguale a O** · [1:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=92.75)

Attendi UNO funziona esattamente come O: aspetta ogni scheda che ha davanti e prosegue quando è stato percorso almeno un percorso. Le due sono intercambiabili, usa il nome che si legge meglio nel tuo workflow.

**E con Attendi TUTTI** · [1:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=114.45)

Per una E con schede affiancate usa Attendi TUTTI. Clic destro sull'area di lavoro, Aggiungi, poi Attendi TUTTI. Collega entrambe le schede E a questa scheda, e Attendi TUTTI all'azione. Prova: aspetta entrambe le schede, sono vere, quindi l'azione parte.

**L'ordine: come sono stati tracciati i collegamenti** · [2:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=142.816)

In che ordine viene eseguito? Il workflow elabora un elenco. Le schede dopo una scheda vengono aggiunte nell'ordine in cui sono stati tracciati i loro collegamenti, quindi prima viene eseguita la condizione in alto, poi quella in basso. La scheda O aspetta finché entrambe sono state eseguite, e l'azione viene eseguita una volta, per quante condizioni siano vere.

**Direttamente a un'azione: nessuna attesa** · [2:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=174.783)

Le schede collegate direttamente a un'azione non aspettano. L'azione viene raggiunta dal percorso breve e parte prima che l'ultima scheda del percorso lungo sia controllata, quindi quella scheda non cambia più nulla. Se l'azione deve aspettare ogni controllo, metti davanti una scheda O, Attendi UNO o Attendi TUTTI.

**Ogni uscita può portare altrove** · [3:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=196.883)

Ogni scheda ha fino a tre uscite: successo, condizione non soddisfatta ed errore. Ogni uscita può portare a una propria scheda successiva.

**Più uscite, un ingresso: ne basta una** · [3:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=208.849)

Puoi anche collegare più uscite di una scheda allo stesso ingresso. Se ne può prendere solo una, perché una scheda termina con un solo risultato, quindi la scheda successiva aspetta solo quella. Vale per qualsiasi ingresso, non solo per questi nodi di unione. Prova: la condizione non è soddisfatta e Attendi TUTTI prosegue comunque.

**Nodi di unione: quali percorsi sono stati presi** · [3:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/it.mp4#t=238.083)

I nodi di unione servono soprattutto a rendere un Workflow più leggibile. O e Attendi UNO proseguono appena è stato preso almeno un percorso collegato. Attendi TUTTI aspetta che tutte le schede precedenti siano finite e prosegue solo se sono stati presi tutti i percorsi collegati. Si può collegare qualsiasi uscita di una scheda, non solo quella verde: se una scheda termina con una condizione non soddisfatta, la sua uscita arancione conta come presa.

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
