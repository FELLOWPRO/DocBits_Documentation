# Advanced Workflow

Il builder **Advanced Workflow** è un editor a grafo di nodi per i workflow che necessitano di ramificazioni, percorsi paralleli e controllo del flusso — oltre il modello lineare When/And/Then del builder Standard. Disponi i nodi su un canvas e li colleghi per definire il flusso di esecuzione.

{% embed url="https://youtu.be/EeNFVR6z7G8" %}
Advanced Workflow Designer
{% endembed %}

## Come accedere

Apri il designer Advanced Workflow dall'area dei workflow (il canvas del builder avanzato). Parti da un nodo **Start** e costruisci il flusso aggiungendo nodi.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Canvas a grafo di nodi Advanced Workflow con barra degli strumenti"><figcaption><p>Il canvas Advanced Workflow — un grafo di nodi con controlli di zoom, esecuzione, griglia e salvataggio. Assegna un nome al workflow nella barra degli strumenti.</p></figcaption></figure>

## Aggiungere nodi

Clicca su **+ Add** per aprire il menu dei nodi. Oltre alle familiari schede **When**, **And** e **Then**, il builder avanzato aggiunge nodi di controllo del flusso:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu Add di Advanced Workflow con i tipi di nodo"><figcaption><p>Il menu dei nodi <strong>+ Add</strong>: When / And / Then più Wait ALL, Wait ANY, OR e Note.</p></figcaption></figure>

- **When / And / Then** — le stesse schede di condizione e azione del builder Standard.
- **Wait ALL** — attende che *tutte* le ramificazioni in ingresso siano completate prima di continuare.
- **Wait ANY** — continua non appena *una qualsiasi* ramificazione in ingresso è completata.
- **OR** — dirama il flusso lungo percorsi alternativi.
- **Note** — un'annotazione di testo libero sul canvas (non influisce sull'esecuzione).

Esegui il flusso con il controllo di riproduzione, validalo e salvalo con il pulsante di salvataggio nella barra degli strumenti.

## Prossimi passi

- Scopri cosa fa ogni scheda nella sezione **Cards**.
- Per automazioni lineari semplici, il builder **Standard Workflow** è più rapido da configurare.
